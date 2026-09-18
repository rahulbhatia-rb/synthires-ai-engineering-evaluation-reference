# Engineering Evaluation Reference

A compact, tested rubric engine for reviewing AI-generated technical answers. It is tailored to Synthires' remote contractor role evaluating correctness, clarity, and usefulness of engineering content.

## Demonstrates

- explicit scoring dimensions rather than opaque pass/fail decisions
- weighted, reproducible evaluation summaries
- a release threshold that identifies answers needing human revision
- dependency-free tests that can run in CI

```bash
python3 -m unittest discover -s tests -v
python3 -m src.app < examples/evaluations.jsonl
```

The JSONL rubric demonstrates a transparent weighted scoring policy and makes
the accept-versus-review threshold reproducible.

## Scope

This reference is not an evaluation of Synthires systems or models. It shows how I would make AI-evaluation criteria inspectable and consistent, informed by my cloud and GenAI/RAG delivery work.

[LinkedIn](https://www.linkedin.com/in/rahul-h-bhatia/) · [Portfolio](https://rahulhbhatia.vercel.app) · [Credly](https://www.credly.com/users/rahul-h-bhatia/badges)
