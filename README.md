# AI_RESEARCHER

AI_RESEARCHER ek **CPU-first Autonomous Research Engine** hai jo
LLM + agents + memory + evaluation ke through
**efficient AI research** karta hai.

## Core Goals
- CPU-friendly LLM research
- Existing techniques ko extreme efficiency tak push karna
- Long-running autonomous research
- Jarvis / external interface se controllable

## What this is NOT
- General superintelligence
- Physics-breaking AI
- Fully self-modifying unsafe system

## Architecture Overview
- Controller: central decision maker
- Agents: planner, researcher, critic, efficiency
- Memory: short-term + long-term learning
- Tools: controlled execution
- Training: LoRA / quantization / pruning (optional)

## How it runs
main.py → Controller → Agents → Memory → Evaluation → Loop

## Requirements
- Python 3.10+
- CPU-based LLM (llama.cpp recommended)
- Linux / Windows / WSL

## Run
```bash
python main.py
