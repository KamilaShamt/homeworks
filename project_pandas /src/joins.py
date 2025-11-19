import pandas as pd

# Чтение файлов
sample_metadata = pd.read_csv("input/sample_metadata.csv")
mass_spec_results = pd.read_csv("input/mass_spec_results.csv")

# INNER JOIN
inner_join = pd.merge(sample_metadata, mass_spec_results, on="sample_id", how="inner")
inner_join.to_csv("output/join_inner.csv", index=False)

# LEFT JOIN
left_join = pd.merge(sample_metadata, mass_spec_results, on="sample_id", how="left")
left_join.to_csv("output/join_left.csv", index=False)

# RIGHT JOIN
right_join = pd.merge(sample_metadata, mass_spec_results, on="sample_id", how="right")
right_join.to_csv("output/join_right.csv", index=False)

# OUTER JOIN
outer_join = pd.merge(sample_metadata, mass_spec_results, on="sample_id", how="outer")
outer_join.to_csv("output/join_outer.csv", index=False)
