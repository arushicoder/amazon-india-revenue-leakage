
from pathlib import Path
import sys

# Add project root to Python path
PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from src.data_loader import DataLoader

# Use a local raw-data directory
RAW_PATH = PROJECT_ROOT / "data" / "raw"

loader = DataLoader(RAW_PATH)

datasets = loader.load_all_files()

print("\nDATASET VERIFICATION")
print("=" * 50)

for name, df in datasets.items():
    print(f"{name}: {df.shape}")

print("\nTotal datasets:", len(datasets))

# Generate quality report
quality_report = loader.generate_quality_report()

print("\nQUALITY REPORT")
print(quality_report.head(10))

# Generate summary
summary = loader.get_dataset_summary()

print("\nDATASET SUMMARY")
print(summary)

assert len(datasets) == 7, (
    f"Expected 7 datasets, found {len(datasets)}"
)

assert "amazon_sale_report" in datasets, (
    "Main sales dataset was not found"
)

assert len(datasets["amazon_sale_report"]) == 128975, (
    "Main sales row count does not match"
)

print("\nALL DATASET CHECKS PASSED!")
