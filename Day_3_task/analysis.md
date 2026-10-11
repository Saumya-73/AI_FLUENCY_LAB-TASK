# Plain LLM vs LLM with One External Tool

## Scenario

In this task, I used a college fee and calculation scenario. I compared a plain LLM with the same LLM when it had access to one external calculator tool.

The external tool used in this project is a calculator. It performs basic arithmetic operations such as addition and subtraction.

## Plain LLM

The plain LLM was given the questions without access to any external tool.

For the AI202 fee question, the LLM could not provide the exact fee because the information was not available in its own knowledge.

For the arithmetic questions, the LLM was able to calculate the answers directly.

## LLM with One Tool

In the tool-enabled version, the LLM was given access to the calculator tool.

For the question "What is 12000 + 18000?", the LLM called the calculator tool with the expression:

12000 + 18000

The tool returned 30000, and the LLM used this result to give the final answer.

For the question "What is the difference between 15000 and 12000?", the LLM called the calculator tool with:

15000 - 12000

The tool returned 3000, and the LLM gave the final answer as 3000.

For the AI202 fee question, the LLM did not call the calculator because a calculator cannot provide course fee information.

## Comparison

| Question | Plain LLM | LLM with Calculator |
|---|---|---|
| Fee for AI202 | Could not provide the exact fee | No tool call because calculator cannot provide fee information |
| 12000 + 18000 | Answered 30000 | Called calculator and got 30000 |
| Difference between 15000 and 12000 | Answered 3000 | Called calculator and got 3000 |

## Observations

1. A plain LLM can answer simple arithmetic questions without using an external tool.

2. When a calculator tool is available, the LLM can recognize when the tool is useful and call it for arithmetic calculations.

3. The tool-enabled LLM did not call the calculator for the AI202 fee question because the calculator cannot provide course information.

4. An external tool does not automatically give the LLM all types of information. The tool is useful only for the task it was designed to perform.

5. The tool result is passed back to the LLM, which then uses the result to produce the final answer.

## When is a Tool Useful?

A tool is useful when the task requires an operation that the LLM should perform using an external function.

For example, the calculator tool is useful for arithmetic calculations. A different tool, such as a database lookup or file reader, would be more suitable for retrieving specific college fee information.

## Conclusion

The experiment shows the difference between a plain LLM and an LLM with access to an external tool. A plain LLM can answer many questions using its existing knowledge, but it may not have specific information or may not be the best choice for reliable calculations.

With one external calculator tool, the LLM can identify calculation questions, call the tool, receive the result, and use that result in its final answer.

Therefore, tools extend the capabilities of an LLM, but the usefulness of a tool depends on what the tool is designed to do.