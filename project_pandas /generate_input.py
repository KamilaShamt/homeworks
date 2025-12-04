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
quality_metrics.to_csv(os.path.join(INPUT_DIR, "quality_metrics.csv"), index=False)

