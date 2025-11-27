import os
import pandas as pd

DATA_DIR = "data"
os.makedirs(DATA_DIR, exist_ok=True)

# Метаданные образцов
sample_metadata = pd.DataFrame({
    'sample_id': [f'Sample_{i}' for i in range(1, 7)],
    'cell_type': ['HEK293', 'HeLa', 'HEK293', 'U2OS', 'HeLa', 'Primary'],
    'treatment': ['Control', 'Drug_A', 'Drug_B', 'Control', 'Drug_A', 'Drug_C'],
    'replicate': [1, 1, 1, 2, 2, 1],
    'concentration_uM': [0, 10, 50, 0, 10, 100]
})

# Результаты масс-спектрометрии
mass_spec_results = pd.DataFrame({
    'sample_id': [f'Sample_{i}' for i in [1, 2, 3, 4, 7]],
    'total_proteins': [2450, 2310, 2540, 2480, 2600],
    'unique_peptides': [15200, 14800, 15600, 15400, 16200],
    'contamination_level': [0.02, 0.05, 0.03, 0.01, 0.04]
})

sample_metadata.to_csv(os.path.join(DATA_DIR, "sample_metadata.csv"), index=False)
mass_spec_results.to_csv(os.path.join(DATA_DIR, "mass_spec_results.csv"), index=False)
