
BYTES_PER_PARAM = {
    "FP16": 2.00,
    "Q8_0": 1.00,
    "Q6_K": 0.81,
    "Q5_K_M": 0.68,
    "Q4_K_M": 0.57,
    "Q3_K_M": 0.43
}

KV_GB_PER_B_PER_1K = 0.02
OVERHEAD = 1.10


def estimate(params_b, precision="Q4_K_M", context_k=8):
    if precision not in BYTES_PER_PARAM:
        raise ValueError("Invalid precision")

    weights_gb = params_b * BYTES_PER_PARAM[precision]
    kv_gb = params_b * context_k * KV_GB_PER_B_PER_1K
    total_gb = (weights_gb + kv_gb) * OVERHEAD

    return weights_gb, kv_gb, total_gb


def verdict(total_gb, available_gb):
    if total_gb <= available_gb * 0.70:
        return "fits comfortably"
    elif total_gb <= available_gb:
        return "fits, but tight"
    else:
        return "does NOT fit"


def report(name, params_b, precision, context_k, available_gb):
    weights, kv, total = estimate(params_b, precision, context_k)

    print("\nModel:", name)
    print("Precision:", precision)
    print("Parameters:", params_b, "B")
    print("Context:", context_k, "K tokens")
    print("Weights:", round(weights, 2), "GB")
    print("KV cache:", round(kv, 2), "GB")
    print("Estimated total:", round(total, 2), "GB")
    print("Verdict:", verdict(total, available_gb))


if __name__ == "__main__":
    AVAILABLE_GB = 8.0

    print("Memory available:", AVAILABLE_GB, "GB")

    report("Qwen small", 1.5, "Q4_K_M", 8, AVAILABLE_GB)
    report("Granite / Qwen mid", 8, "Q4_K_M", 8, AVAILABLE_GB)
    report("Mid at FP16", 8, "FP16", 8, AVAILABLE_GB)
    report("Large local", 30, "Q4_K_M", 8, AVAILABLE_GB)
    report("Server class", 70, "Q4_K_M", 8, AVAILABLE_GB)

    print("\n--- Context length comparison: 8B Q4_K_M ---")
    for context in [4, 8, 32, 128]:
        report("8B model", 8, "Q4_K_M", context, AVAILABLE_GB)

    print("\n--- Precision comparison: 8B at 8K context ---")
    for precision in ["Q3_K_M", "Q4_K_M", "Q5_K_M", "Q8_0", "FP16"]:
        report("8B model", 8, precision, 8, AVAILABLE_GB)
