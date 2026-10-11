def calculate_memory(params_b, bytes_per_param, kv_cache_gb):
    weights_gb = params_b * bytes_per_param
    total_gb = weights_gb + kv_cache_gb
    return weights_gb, total_gb


params_b = 7
available_gb = 8

# Context length comparison
print("=== Context Length Comparison ===")

for context, kv_cache in [
    (2, 0.5),
    (4, 1.0),
    (8, 2.0)
]:
    weights, total = calculate_memory(params_b, 0.5, kv_cache)

    print(
        "Context:", context, "K",
        "| Weights:", weights, "GB",
        "| KV Cache:", kv_cache, "GB",
        "| Total:", total, "GB",
        "| Fits:", total <= available_gb
    )


# Quantization comparison
print("\n=== Quantization Comparison ===")

context = 4

for quantization, bytes_per_param in [
    ("FP16", 2.0),
    ("8-bit", 1.0),
    ("4-bit", 0.5)
]:
    kv_cache = 1.0

    weights, total = calculate_memory(
        params_b,
        bytes_per_param,
        kv_cache
    )

    print(
        "Quantization:", quantization,
        "| Weights:", weights, "GB",
        "| KV Cache:", kv_cache, "GB",
        "| Total:", total, "GB",
        "| Fits:", total <= available_gb
    )