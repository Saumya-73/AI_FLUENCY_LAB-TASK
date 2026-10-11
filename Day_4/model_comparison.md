# Day 4 — Four Model Comparison Table

**Date checked:** 10 October 2026

| Detail | Qwen | Mistral | IBM Granite | OpenAI gpt-oss |
|---|---|---|---|---|
| Full model name/version | Qwen3-4B | Mistral-7B-Instruct-v0.3 | Granite-4.0-Micro | gpt-oss-20b |
| Publisher | Alibaba / Qwen Team | Mistral AI | IBM | OpenAI |
| Available model sizes | Multiple sizes in the Qwen3 family | Multiple sizes in the Mistral family | Multiple sizes in the Granite family | 20B and 120B |
| Size selected | 4B | 7B | Granite-4.0-Micro | 20B |
| Total/active parameters | 4B total, dense | 7B total, dense | 3B total, dense | 20.9B total, 3.6B active, MoE |
| Context window | 32K (up to 131K with YaRN) | 32K tokens | 128K | 131,072 tokens (128K) |
| Exact licence name | Apache License 2.0 | Apache License 2.0 | Apache License 2.0 | Apache License 2.0 |
| Commercial use allowed? | Yes, under Apache 2.0 terms | Yes, under Apache 2.0 terms | Yes, under Apache 2.0 terms | Yes, under Apache 2.0 terms |
| Extra licence conditions | Preserve licence and copyright notices; state changes | Preserve licence and copyright notices; state changes | Preserve licence and copyright notices; state changes | Preserve licence and copyright notices; state changes |
| Tool/function calling supported? | Yes | Yes | Yes — verify selected model card | Yes |
| GGUF/Ollama version available? | Not checked | Not checked | Not checked | Not checked |
| Q4 download size | N/A - Ollama not used | N/A - Ollama not used | N/A - Ollama not used | N/A - Ollama not used |
| Estimated total memory (Q4, 8K context) | Approx. 3.21 GB | Approx. 5.62 GB | Approx. 2.41 GB | Approx. 16.06 GB* |
| Runs on my machine? (Y/N) | N — not tested locally | N — not tested locally | N — not tested locally | N — not tested locally |

## Licence Comparison

1. Do models within the same family have different licences?
   Yes. Models within the same family can have different licences depending on the model version. Therefore, we should check the exact licence of each model before using it.
2. Which models can be used commercially, and under what conditions?
 The selected models list Apache License 2.0 in their model cards. They can generally be used commercially under its terms. Users must follow the licence conditions, preserve required copyright and licence notices, and state significant changes where required. Always verify the exact licence of the selected model version.
3. Which model has specific licence restrictions?
    The selected model cards list Apache License 2.0, which generally permits commercial use under its terms. However, licence terms can differ between versions, so the exact model card and licence should always be checked before use.
4. Which model cards mention tool/function calling?
   The selected Qwen, Mistral, IBM Granite, and OpenAI gpt-oss model documentation describes tool or function calling capabilities. The exact support and usage format should be checked in each selected model's official documentation.
5. Which model card describes its limitations most clearly?
   The model card that clearly explains limitations, intended use, and safety considerations is the most useful for choosing a model. I would compare the official Qwen, Mistral, IBM Granite, and OpenAI gpt-oss model cards before deciding which one describes its limitations most clearly.

## Part E — Model Recommendations

### Scenario 1: 8 GB laptop, no GPU

I recommend a small quantized model that fits within the available memory. It should support tool calling and use an Apache 2.0 or MIT licence. Memory requirements should be checked before running it locally.

### Scenario 2: Server with a 24 GB GPU serving 20 students

I recommend testing a model that fits within the GPU memory while leaving enough memory for the context cache and multiple users. Benchmark concurrent requests before choosing the final model.

### Scenario 3: Public capstone project on GitHub

I recommend a model with a clearly documented licence that permits the intended use. Include the model card link, licence details, setup instructions, and any required notices in the repository.

## Sources

- Qwen3-4B: https://huggingface.co/Qwen/Qwen3-4B
- Mistral-7B-Instruct-v0.3: https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.3
- IBM Granite-4.0-Micro: https://huggingface.co/ibm-granite/granite-4.0-micro
- OpenAI gpt-oss-20b: https://huggingface.co/openai/gpt-oss-20b

- Ollama model pages: Not used