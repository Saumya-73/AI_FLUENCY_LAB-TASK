# Day 5 - Analysis

## Title

Serving Models: Cloud API Demonstration and Model Comparison

## Objective

The objective of this lab is to understand model serving, API-based
generation, streaming responses, model comparison, and the concepts
behind efficient model serving.

## Implementation

The original lab uses Ollama for local model serving and includes a
vLLM demonstration.

For this implementation, Ollama was not installed. Instead, the
OpenAI-compatible Groq Cloud API was used.

The following components were implemented:

- API generation
- Streaming response measurement
- Time measurement
- Two-model comparison
- Custom system-prompt demonstration
- vLLM paper alternative

## API Generation Results

Provider: Groq

Model: openai/gpt-oss-20b

Normal API generation time: 0.94 seconds

Streaming TTFT: 0.52 seconds

Streaming total time: 0.59 seconds

The API successfully generated a response explaining what an AI agent
is.

## Model Comparison

Two available Groq models were compared:

1. openai/gpt-oss-20b
2. openai/gpt-oss-120b

Both models were tested using the same prompts.

### Results

| Model | Prompt 1 | Prompt 2 | Prompt 3 |
|---|---:|---:|---:|
| gpt-oss-20b | 0.57 s | 0.68 s | 0.70 s |
| gpt-oss-120b | 1.12 s | 0.48 s | 1.01 s |

Prompt 1 tested exact instruction following.

Prompt 2 tested explanation of an AI agent.

Prompt 3 tested percentage calculation and step-by-step reasoning.

Both models successfully followed the instructions and produced relevant
responses.

## Custom Model Demonstration

The custom model section was implemented using system prompts through
the Groq API.

Two behaviors were demonstrated:

- Fee Assistant
- Student Welcome Assistant

This demonstrates how a system prompt can define the behavior and role
of the same underlying language model.

This is a cloud API equivalent of the Modelfile demonstration in the
original lab. It is not an Ollama Modelfile execution.

## vLLM Section

vLLM was not executed locally.

The paper alternative from the lab manual was completed instead.

The main concepts covered were:

- Efficient model serving
- Continuous batching
- High-throughput inference
- GPU utilization
- Trade-offs between simple local serving and high-throughput serving

No local vLLM performance measurements are claimed.

## Key Observations

1. Cloud APIs can provide OpenAI-compatible interfaces for model serving.
2. Streaming can provide a lower time-to-first-token compared with waiting
   for the complete response.
3. Different models can have different response times for different
   prompts.
4. A larger model does not necessarily produce the fastest response for
   every prompt.
5. System prompts can be used to create different assistant behaviors.
6. Local Ollama-specific measurements such as loaded memory and local
   GPU usage were not available in this cloud implementation.

## Conclusion

The lab demonstrated model serving through a cloud API, API generation,
streaming responses, model comparison, and system-prompt-based
customization.

The Ollama and local vLLM portions were not executed and were clearly
replaced with the corresponding cloud API implementation and paper
alternative.