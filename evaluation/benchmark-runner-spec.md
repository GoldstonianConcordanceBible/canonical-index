# GCB Benchmark Runner Spec

Purpose:
Evaluate GCB retrieval and answer quality across core biblical question categories.

## Benchmark Stages

1. Retrieve top 10 sources
2. Score source relevance
3. Generate answer bundle
4. Compare answer bundle to gold answer
5. Record metrics

## Scored Metrics

- Top-1 hit rate
- Top-3 hit rate
- Canonical correctness
- Ethiopian canon awareness
- Concept linkage quality
- Media bundle quality
- Transcript support quality

## Output artifacts

- run-history.csv
- scorecards/*.json
- failure-analysis/*.md