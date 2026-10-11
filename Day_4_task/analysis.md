# Task 4 – Memory Estimation, Quantization and Licensing

## 1. Scenario

I considered a small local language model scenario with the following specifications:

- Available memory: 8 GB
- Example model size: 7 billion parameters (7B)
- Purpose: Running a small AI assistant
- Context length: 4K tokens

The goal is to estimate whether a model can fit within the available memory before attempting to run it.

## 2. Important Concepts

### Model Weights

Model weights are the parameters stored by a language model. Their memory requirement depends on the number of parameters and the precision used to store them. A model with more parameters generally requires more memory.

### Quantization

Quantization reduces the number of bits used to represent model weights. It can reduce memory requirements and make models suitable for systems with limited memory. However, lower precision can affect model quality.

### KV Cache and Context Length

The KV cache stores information needed to process the current context during inference. Its memory requirement generally increases with context length. This is important for an AI assistant that maintains a conversation or processes tool results.

### Model Card

A model card describes a model's architecture, intended uses, limitations, capabilities and other relevant information. It can help users understand whether a model is suitable for their application.

### Open-Weight vs Open-Source

Open-weight models make their trained weights available, but this does not automatically mean that every part of the model is open-source. The exact licence and its conditions determine how the model may be used, modified and redistributed.

## 3. Memory Estimation

For this example, I used a 7B model with 4-bit weights.

The simplified formula is:

Weights memory = Parameters × Bytes per parameter

Estimated total memory = Weights memory + KV cache

For a 7B model using an assumed 0.5 bytes per parameter:

Weights memory = 7 × 0.5 = 3.5 GB

Estimated KV cache = 1.0 GB

Estimated total = 3.5 + 1.0 = 4.5 GB

The estimated total is below the available 8 GB memory budget. Therefore, this configuration fits according to the simplified estimate.

### Memory Estimate Table

| Model configuration | Parameters (B) | Precision | Context (K) | Weights (GB) | KV cache (GB) | Total (GB) | Fits in 8 GB? |
|---|---:|---|---:|---:|---:|---:|---|
| Example 7B | 7 | 4-bit | 2 | 3.5 | 0.5 | 4.0 | Yes |
| Example 7B | 7 | 4-bit | 4 | 3.5 | 1.0 | 4.5 | Yes |
| Example 7B | 7 | 4-bit | 8 | 3.5 | 2.0 | 5.5 | Yes |
| Example 7B | 7 | 4-bit | 16 | 3.5 | 4.0 | 7.5 | Yes, by estimate |

These are illustrative estimates, not measurements from an actual model. The KV cache values are assumptions used for this comparison. Runtime overhead and other memory requirements are not included, so a configuration close to 8 GB may not fit in practice.

## 4. Context Length Comparison

The following comparison keeps the model size and quantization unchanged.

| Context length | Weights (GB) | KV cache (GB) | Total (GB) | Fits in 8 GB? |
|---|---:|---:|---:|---|
| 2K | 3.5 | 0.5 | 4.0 | Yes |
| 4K | 3.5 | 1.0 | 4.5 | Yes |
| 8K | 3.5 | 2.0 | 5.5 | Yes |
| 16K | 3.5 | 4.0 | 7.5 | Yes, by estimate |

### Observation

When context length increases, the estimated KV cache requirement increases while the weight memory remains unchanged. In this example, 16K is the largest context among the configurations tested that stays below 8 GB according to the simplified calculation. It is not a verified maximum for a real model because runtime overhead and model architecture can change the result.

## 5. Quantization Comparison

The following comparison keeps the model size at 7B parameters and the context at 4K tokens.

| Precision | Bytes per parameter (assumed) | Weights (GB) | KV cache (GB) | Total (GB) | Fits in 8 GB? |
|---|---:|---:|---:|---:|---|
| FP16 | 2.0 | 14.0 | 1.0 | 15.0 | No |
| 8-bit | 1.0 | 7.0 | 1.0 | 8.0 | Yes, before overhead |
| 4-bit | 0.5 | 3.5 | 1.0 | 4.5 | Yes, by estimate |

### Observation

Reducing the precision reduces the estimated weight memory. FP16 exceeds the available memory budget. The 8-bit configuration reaches the full 8 GB budget before runtime overhead, so it may not fit in practice. The 4-bit configuration leaves more estimated memory available, although it can involve a quality trade-off.

For this scenario, I would investigate a 4-bit model first because it leaves more room for runtime memory and other system requirements.

## 6. Open Model Comparison

The following models come from three different model families. Their official model cards and licence information should be checked before selecting a model for actual use.

| Basis for comparison | Llama 3.2 3B | Qwen2.5 3B | Gemma 3 4B |
|---|---|---|---|
| Publisher | Meta | Qwen | Google DeepMind |
| Parameters | Approximately 3.21B | Approximately 3B | 4B |
| Context window | Official text model supports up to 128K; quantized variants may have different limits | Model variant must be checked against its official card | Up to 128K for the 4B model |
| Licence | Llama 3.2 Community License | Apache 2.0 for the relevant Qwen2.5 3B release | Gemma Terms of Use |
| Commercial use | Subject to the licence and acceptable-use conditions | Generally permitted under Apache 2.0 conditions | Subject to Gemma terms |
| Extra conditions | Must follow the licence and acceptable-use policy | Preserve applicable notices and comply with Apache 2.0 | Follow Google's Gemma terms |
| Tool calling | Check the specific model card and implementation | Check the specific model card and implementation | Check the specific model card and implementation |
| Ollama/GGUF availability | Check the specific Ollama build | Check the specific Ollama build | Check the specific Ollama build |
| Actual local testing | Not performed | Not performed | Not performed |

The parameter counts, context limits, licences and available formats can differ between variants. Before making a final selection, I will record the exact model version, official model-card link, Ollama library link, quantized download size and date checked.

## 7. Model Card and Licence Verification

A model card helps identify the intended uses, limitations and capabilities of a model. The licence explains the conditions for using and redistributing it.

For example, the Llama 3.2 Community License has conditions that differ from the Apache 2.0 licence used by the relevant Qwen2.5 release. Gemma models are governed by Google's Gemma terms. Therefore, the models should not be treated as having identical licensing conditions.

The official sources to consult are:

- Meta Llama 3.2 model card: https://github.com/meta-llama/llama-models/blob/main/models/llama3_2/MODEL_CARD.md
- Qwen2.5 model collection: https://huggingface.co/Qwen
- Google Gemma 3 model card: https://ai.google.dev/gemma/docs/core/model_card_3
- Ollama model library: https://ollama.com/library

The exact model variant and its licence should be confirmed before use. The date of verification should be recorded when the official pages are checked.

## 8. Suitability and Final Recommendation

For the example 8 GB memory scenario, a 7B model using 4-bit quantization has an estimated total memory requirement of 4.5 GB at a 4K context under the assumptions used here. This leaves more estimated room for runtime requirements than the FP16 and 8-bit configurations.

For a practical small assistant, I would first investigate a small quantized model, such as a 3B or 4B variant, and verify its actual download size, quality and licence. A smaller model may be more practical than a 7B model on a memory-limited system.

The final choice depends on the intended use. If commercial use or redistribution is planned, the licence conditions must be checked before selecting a model. If the assistant needs a long context or tool calling, those capabilities must also be verified for the exact model version.

## 9. Estimate Versus Reality and Limitations

Ollama was not installed in this environment, and I chose not to install it. Therefore, I did not run `ollama list` or `ollama ps`, and I have no actual local-model memory measurement to compare with my estimate.

The results in this report are calculations based on assumed weight precision and KV cache values. They are not evidence that a real model was loaded successfully on this machine.

Actual memory usage depends on the model architecture, quantization format, KV cache settings, context length, runtime overhead and available system memory. The estimated fit should therefore be verified on the target machine before practical deployment.

## 10. Conclusion

Model size, quantization, context length and licensing all affect the suitability of an open-weight model.

Memory determines whether a configuration can run within the available hardware budget. Quantization can reduce the weight memory, while longer contexts generally increase KV cache requirements. However, a memory estimate alone does not guarantee that a model will run successfully.

Licensing determines whether a model may be used for the intended purpose, especially for commercial use or redistribution. A suitable model should therefore meet the memory requirements, provide the necessary capabilities and have licence conditions compatible with its intended use.