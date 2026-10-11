# Day 5 - vLLM Paper Alternative

## Reason

vLLM was not executed locally because this Day 5 implementation uses
a cloud API instead of Ollama, and a local NVIDIA GPU was not available
for the vLLM demonstration.

Therefore, the vLLM section was completed using the paper alternative
provided in the lab manual.

## 1. What is the primary advantage of vLLM?

vLLM is designed for efficient serving of language models.
Its main advantage is high-throughput inference and efficient memory
management when serving models.

## 2. What is continuous batching and why does it matter?

Continuous batching allows new requests to be added to an ongoing batch
while other requests are still being processed.

This improves GPU utilization and helps increase serving throughput.

## 3. When would you choose vLLM over a simple Ollama setup?

vLLM would be useful when serving language models for multiple users
or applications where high throughput and efficient GPU utilization
are important.

A simple Ollama setup is more suitable for local experimentation and
easy model usage.

## 4. What are the trade-offs?

vLLM generally requires more setup and suitable GPU resources.

Ollama provides a simpler local model-running experience, while vLLM
is more focused on efficient model serving and higher-throughput
inference.

## Implementation Note

These answers are the paper alternative for the vLLM portion of the
Day 5 lab. No local vLLM performance measurements are claimed.