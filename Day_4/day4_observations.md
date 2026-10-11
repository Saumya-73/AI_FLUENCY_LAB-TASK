# Day 4 — Memory Estimation Observations

## 1. System Memory
- Available memory used for estimation: 8 GB
- Estimation program: `vram_estimate.py`

## 2. Model Size Comparison

| Model | Precision | Estimated Total | Verdict |
|---|---|---:|---|
| Qwen small (1.5B) | Q4_K_M | 1.20 GB | Fits comfortably |
| Granite / Qwen mid (8B) | Q4_K_M | 6.42 GB | Fits, but tight |
| Mid (8B) | FP16 | 19.01 GB | Does NOT fit |
| Large local (30B) | Q4_K_M | 24.09 GB | Does NOT fit |
| Server class (70B) | Q4_K_M | 56.21 GB | Does NOT fit |

## 3. Context Length Comparison

For an 8B model using Q4_K_M:

- 4K context: 5.72 GB
- 8K context: 6.42 GB
- 32K context: 10.65 GB
- 128K context: 27.54 GB

**Observation:** Increasing context length increases the estimated memory requirement.

## 4. Quantization Comparison

For an 8B model using an 8K context:

- Q3_K_M: 5.19 GB
- Q4_K_M: 6.42 GB
- Q5_K_M: 7.39 GB
- Q8_0: 10.21 GB
- FP16: 19.01 GB

**Observation:** Lower-bit quantization requires less estimated memory. Higher precision requires more memory.

## 5. Recommendation

For an estimated 8 GB memory budget, the 1.5B Q4_K_M model fits comfortably. The 8B Q4_K_M model is estimated to fit, but with limited headroom. Models requiring more than 8 GB are estimated not to fit within this budget.

**Note:** These are estimates, not actual GPU VRAM measurements. System RAM and GPU VRAM are different.
## Part C — Local Model Memory Check

**Setup used:** Groq API

**Status:** Local Ollama memory measurement not performed because this task uses a hosted API rather than a locally running model.

**Next action:** Pair with a classmate who has Ollama installed and compare `ollama list` model sizes with `ollama ps` memory usage.