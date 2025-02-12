"""Mock feature."""

import polars as pl

from ds_template.features.feature import Feature


class MockFeature(Feature):
    """Mock feature."""

    def __init__(self, column_name: str):
        """Initialize the feature."""
        self.column_name = column_name

    def fit(self, X: pl.DataFrame, y: pl.DataFrame | None = None) -> "MockFeature":
        """Fit the feature."""
        return self

    def transform(self, X: pl.DataFrame) -> pl.DataFrame:
        """Transform the feature."""
        return X.select(pl.col(self.column_name).str.len_chars())

    def fit_transform(self, X: pl.DataFrame, y: pl.DataFrame | None = None) -> pl.DataFrame:
        """Fit and transform the feature."""
        return self.fit(X, y).transform(X)
