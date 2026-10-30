# SYMPLEX

**A Neuro-Symbolic AI Agent for Reliable Task Planning, Logical Verification and Uncertainty-Aware Failure Recovery**

SYMPLEX explores how natural-language tasks can be converted into formal plans, checked against safety rules, and adapted when outcomes are uncertain. Actions with dependencies can be unsafe when those dependencies are misunderstood or ignored.

## Proposed architecture

```text
Natural-language task → task parser → formal task → classical planner
  → candidate plan → logical safety verifier → execution
  → uncertain outcome → Bayesian belief update → replanning
```

## Module mapping

- **Module 4:** First-Order Logic and Resolution for safety verification.
- **Module 5:** Bayesian belief networks for uncertainty handling.
- **Module 6:** Classical planning and dynamic replanning.

## Phase 1

This foundation provides structured task and plan models, a deterministic example parser, a mock planner, a simple placeholder safety verifier, belief-state and simulated-execution interfaces, a CLI, and tests. Interfaces are defined with protocols so implementations can be replaced through dependency injection.

The LLM, a real PDDL planner, a full resolution engine, Bayesian inference, and dynamic replanning are later-phase work. No API key is required and the executor performs no real operations.

## Setup

Requires Python 3.11 or newer.

```bash
python -m venv .venv
```

Windows activation:

```powershell
.venv\Scripts\activate
```

Install dependencies and the package:

```bash
pip install -r requirements.txt
pip install -e .
```

## Run

```bash
python -m symplex
```

Enter the database migration example when prompted to see parsing, a mock candidate plan, and the demo verifier output. Unsupported input is represented as an unsupported task and produces no plan.

## Tests

```bash
pytest
```

## Configuration

Copy `.env.example` to `.env` if you want to set local configuration values. `OPENAI_API_KEY` is optional and unused in Phase 1.
