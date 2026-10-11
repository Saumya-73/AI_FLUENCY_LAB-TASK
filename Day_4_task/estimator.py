def estimate_memory(params_b, bytes_per_param, kv_cache_gb, available_gb):
    weights_gb = params_b * bytes_per_param
    total_gb = weights_gb + kv_cache_gb

    fits = total_gb <= available_gb

    return weights_gb, total_gb, fits


# Example model
model = "Example 7B Model"
params_b = 7
bytes_per_param = 0.5
context_k = 4
kv_cache_gb = 1.0
available_gb = 8

weights, total, fits = estimate_memory(
    params_b,
    bytes_per_param,
    kv_cache_gb,
    available_gb
)

print("Model:", model)
print("Parameters:", params_b, "B")
print("Precision bytes/parameter:", bytes_per_param)
print("Context:", context_k, "K")
print("Weights:", round(weights, 2), "GB")
print("KV Cache:", kv_cache_gb, "GB")
print("Total Estimated Memory:", round(total, 2), "GB")
print("Available Memory:", available_gb, "GB")

if fits:
    print("Result: FITS")
else: 
    print("Result: DOES NOT FIT")