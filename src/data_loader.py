
import os
import re
import logging
from pathlib import Path

import pandas as pd


logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s"
)

logger = logging.getLogger(__name__)


class DataLoader:
    """
    Load CSV and Excel datasets and perform initial
    data quality checks.
    """

    SUPPORTED_EXTENSIONS = {".csv", ".xlsx", ".xls"}

    def __init__(self, data_path):
        self.data_path = Path(data_path)
        self.datasets = {}
        self.quality_report = None

    @staticmethod
    def standardize_column(column):
        """Convert column names to snake_case."""
        column = str(column).strip().lower()
        column = re.sub(r"[^a-z0-9]+", "_", column)
        column = re.sub(r"_+", "_", column)

        return column.strip("_")

    def load_file(self, file_path):
        """Load a CSV or Excel file."""

        extension = file_path.suffix.lower()

        if extension == ".csv":
            try:
                return pd.read_csv(file_path)
            except UnicodeDecodeError:
                return pd.read_csv(
                    file_path,
                    encoding="latin1"
                )

        if extension in {".xlsx", ".xls"}:
            return pd.read_excel(file_path)

        return None

    def load_all_files(self):
        """Discover and load all supported files."""

        if not self.data_path.exists():
            raise FileNotFoundError(
                f"Dataset folder not found: {self.data_path}"
            )

        for file_path in sorted(self.data_path.rglob("*")):

            if not file_path.is_file():
                continue

            if file_path.suffix.lower() not in self.SUPPORTED_EXTENSIONS:
                continue

            if file_path.name.startswith("~$"):
                continue

            df = self.load_file(file_path)

            if df is None:
                continue

            df.columns = [
                self.standardize_column(col)
                for col in df.columns
            ]

            dataset_name = self.standardize_column(
                file_path.stem
            )

            if dataset_name in self.datasets:
                logger.warning(
                    "Duplicate dataset name: %s", dataset_name
                )
                continue

            self.datasets[dataset_name] = df

            logger.info(
                "%s | Shape: %s | Missing: %s | Duplicates: %s",
                file_path.name,
                df.shape,
                df.isna().sum().sum(),
                df.duplicated().sum()
            )

        logger.info(
            "Total datasets loaded: %d",
            len(self.datasets)
        )

        return self.datasets

    def generate_quality_report(self):
        """Create a column-level quality report."""

        reports = []

        for dataset_name, df in self.datasets.items():

            for column in df.columns:

                null_count = int(df[column].isna().sum())

                null_percentage = (
                    null_count / len(df) * 100
                    if len(df) else 0
                )

                reports.append({
                    "dataset": dataset_name,
                    "column": column,
                    "data_type": str(df[column].dtype),
                    "null_count": null_count,
                    "null_percentage": round(
                        null_percentage, 2
                    ),
                    "unique_values": int(
                        df[column].nunique()
                    ),
                    "duplicate_rows": int(
                        df.duplicated().sum()
                    )
                })

        self.quality_report = pd.DataFrame(reports)

        return self.quality_report

    def get_dataset_summary(self):
        """Return a dataset-level summary."""

        summary = []

        for name, df in self.datasets.items():

            summary.append({
                "dataset": name,
                "rows": len(df),
                "columns": len(df.columns),
                "duplicate_rows": int(
                    df.duplicated().sum()
                ),
                "total_missing_values": int(
                    df.isna().sum().sum()
                )
            })

        return pd.DataFrame(summary)

