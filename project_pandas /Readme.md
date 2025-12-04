скрипт в generate_input.py

import os
import pandas as pd

INPUT_DIR = "input"
os.makedirs(INPUT_DIR, exist_ok=True)

# Метаданные образцов
sample_metadata = pd.DataFrame({
    'sample_id': ['Sample_1', 'Sample_2', 'Sample_3', 'Sample_4', 'Sample_5', 'Sample_6'],
    'cell_type': ['HEK293', 'HeLa', 'HEK293', 'U2OS', 'HeLa', 'Primary'],
    'treatment': ['Control', 'Drug_A', 'Drug_B', 'Control', 'Drug_A', 'Drug_C'],
    'replicate': [1, 1, 1, 2, 2, 1],
    'concentration_uM': [0, 10, 50, 0, 10, 100]
})

# Результаты масс-спектрометрии
mass_spec_results = pd.DataFrame({
    'sample_id': ['Sample_1', 'Sample_2', 'Sample_3', 'Sample_4', 'Sample_7'],
    'total_proteins': [2450, 2310, 2540, 2480, 2600],
    'unique_peptides': [15200, 14800, 15600, 15400, 16200],
    'contamination_level': [0.02, 0.05, 0.03, 0.01, 0.04]
})

# Данные о качестве
quality_metrics = pd.DataFrame({
    'sample_id': ['Sample_2', 'Sample_3', 'Sample_4', 'Sample_5', 'Sample_8'],
    'rin_score': [8.5, 7.2, 9.1, 6.8, 8.9],
    'pcr_duplication': [0.12, 0.18, 0.09, 0.25, 0.11],
    'mapping_rate': [0.95, 0.87, 0.96, 0.82, 0.94]
})

sample_metadata.to_csv(os.path.join(INPUT_DIR, "sample_metadata.csv"), index=False)
mass_spec_results.to_csv(os.path.join(INPUT_DIR, "mass_spec_results.csv"), index=False)
quality_metrics.to_csv(os.path.join(INPUT_DIR, "quality_metrics.csv"), index=False


скрипт в join.py, который лежит в src

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


скрипт в Dockerfile

FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ ./src

CMD ["python", "src/joins.py"]

Требования:
requirements.txt: pandas==2.3.3

Открыть доступ к outer - в терминале:
chmod 777 output 

Сборка image и joins - в терминале:

docker build -t pandas-joins .

docker run --rm -v "$(pwd)/input:/input" -v "$(pwd)/output:/output" joiner-image