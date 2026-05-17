import pandas as pd

evaluation = pd.DataFrame({
    "prompt_type": ["Zero-shot", "One-shot", "Refined"],
    "clarity_score": [3, 4, 5],
    "completeness_score": [3, 4, 5],
    "consistency_score": [2, 4, 5]
})

evaluation["average_score"] = evaluation[
    ["clarity_score", "completeness_score", "consistency_score"]
].mean(axis=1)

ranked = evaluation.sort_values("average_score", ascending=False)

print("Prompt Engineering Evaluation Demo")
print(ranked)
print(f"\nBest performing approach: {ranked.iloc[0]['prompt_type']}")
