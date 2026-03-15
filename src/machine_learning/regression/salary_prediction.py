import sys
from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401  (registers 3D projection)
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split, cross_val_predict


DEFAULT_CSV_PATH = Path(
    "/Users/lakshmanraghu/Downloads/AI Engineer/Multiple Linear Regression/salary.csv"
)


def load_dataset(path: Path):
    """Load CSV and choose columns for features and target.

    Strategy:
    - Read CSV using pandas.
    - Select numeric columns.
    - If there are >= 3 numeric columns: use the first two as features and the third as target
      (this mirrors the structure used in `multiple_linear_regression.py`).
    - If there are exactly 2 numeric columns: treat the first as a single feature and the
      second as target (falls back to simple linear regression behavior).
    - If fewer than 2 numeric columns raise an informative error.
    """
    if not path.exists():
        raise FileNotFoundError(f"CSV file not found at: {path}")

    df = pd.read_csv(path)
    if df.empty:
        raise ValueError("Loaded CSV is empty")

    # If the CSV has expected named columns, map them to x1, x2, Output
    expected_cols = ("YearsExperience", "Rating", "Salary")
    if all(col in df.columns for col in expected_cols):
        data = pd.DataFrame(
            {
                "x1": df["YearsExperience"].astype(float),
                "x2": df["Rating"].astype(float),
                "Output": df["Salary"].astype(float),
            }
        )
        print(f"Loaded {len(df)} rows from '{path}' using YearsExperience, Rating, Salary\n")
        return data

    # Fallback: keep only numeric columns (int/float) and create x1,x2,Output from them
    numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    if len(numeric_cols) < 2:
        raise ValueError("Need at least 2 numeric columns (features + target) to run regression.")

    if len(numeric_cols) >= 3:
        x_cols = numeric_cols[:2]
        y_col = numeric_cols[2]
    else:  # exactly 2 numeric columns
        x_cols = [numeric_cols[0]]
        y_col = numeric_cols[1]

    data = pd.DataFrame(
        {
            "x1": df[x_cols[0]].astype(float),
            "x2": df[x_cols[1]].astype(float) if len(x_cols) > 1 else df[x_cols[0]].astype(float),
            "Output": df[y_col].astype(float),
        }
    )

    print(f"Loaded {len(df)} rows from '{path}'")
    print(f"Feature columns mapped to: ['x1' -> {x_cols[0]}, 'x2' -> {x_cols[1] if len(x_cols)>1 else x_cols[0]}]")
    print(f"Target column mapped to: 'Output' -> {y_col}\n")

    return data


def train_and_evaluate(
    X: pd.DataFrame,
    y: pd.Series,
    mode: str = "self",
    test_size: float = 0.33,
    random_state: int = 42,
    cv: int = 5,
):
    """Train and evaluate LinearRegression using different evaluation modes.

    mode:
      - 'self' : train and test on the same data (original behavior)
      - 'split': train/test split (uses test_size and random_state)
      - 'cv'   : k-fold cross-validation (uses cv)

    Returns the trained model (fitted on training data or full data depending on mode)
    and the predictions used for the reported evaluation (y_pred) alongside y_true for clarity.
    """
    if mode not in ("self", "split", "cv"):
        raise ValueError("mode must be one of 'self', 'split', or 'cv'")

    model = LinearRegression()

    if mode == "self":
        # Train and test on same data
        X_train, X_test, y_train, y_test = X.copy(), X.copy(), y.copy(), y.copy()
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)

    elif mode == "split":
        # Train/test split
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=test_size, random_state=random_state
        )
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)

    else:  # cv
        # For CV, produce cross-validated predictions for evaluation, but fit final model on full data
        y_pred = cross_val_predict(LinearRegression(), X, y, cv=cv)
        # Fit model on full data to show coefficients (consistent with original approach)
        model.fit(X, y)
        # For consistency with other modes, set y_test to full y
        X_train, X_test, y_train, y_test = X, X, y, y

    # Print coefficients similar to the original script (model is fitted appropriately above)
    print("--- Model Coefficients ---")
    try:
        if model.coef_.shape[0] >= 2:
            print(f"Intercept (β0): {model.intercept_:.1f}")
            print(f"Coefficients (β1, β2): {model.coef_}")
            print(
                f"Model Equation: y = {model.intercept_:.1f} + {model.coef_[0]:.1f}*x1 + {model.coef_[1]:.1f}*x2\n"
            )
        else:
            print(f"Intercept (β0): {model.intercept_:.1f}")
            print(f"Coefficients (β1): {model.coef_}")
            print(f"Model Equation: y = {model.intercept_:.1f} + {model.coef_[0]:.1f}*x1\n")
    except Exception:
        print(f"Intercept (β0): {model.intercept_}")
        print(f"Coefficients: {model.coef_}")
        print(f"Model Equation: y = {model.intercept_} + {model.coef_}\n")

    # Evaluate
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print("--- Model Performance Evaluation ---")
    print(f"Predicted values: {y_pred}")
    print(f"Actual values:    {y_test.values}")
    print(f"Mean Squared Error: {mse:.2f}")
    print(f"R² Score: {r2:.2f}\n")

    return model, y_pred, (X_train, X_test, y_train, y_test)


def plot_results(X: pd.DataFrame, y: pd.Series, model: LinearRegression, splits=None):
    """Plot data and regression (3D when there are 2 features, 2D otherwise)."""
    n_features = X.shape[1]

    if n_features == 2:
        # 3D surface + scatter
        fig = plt.figure(figsize=(10, 7))
        ax = fig.add_subplot(111, projection="3d")

        # If splits provided and plotting for split mode, show only test points as in original
        if splits is not None:
            (_, X_test, _, y_test) = splits
            ax.scatter(X_test.iloc[:, 0], X_test.iloc[:, 1], y_test, color="blue", s=100, label="Actual Data Points")
        else:
            ax.scatter(X.iloc[:, 0], X.iloc[:, 1], y, color="blue", s=100, label="Actual Data Points")

        # Prepare grid (10 points to match original script)
        x1_surf = np.linspace(X.iloc[:, 0].min(), X.iloc[:, 0].max(), 10)
        x2_surf = np.linspace(X.iloc[:, 1].min(), X.iloc[:, 1].max(), 10)
        x1_surf, x2_surf = np.meshgrid(x1_surf, x2_surf)

        pts = pd.DataFrame({X.columns[0]: x1_surf.ravel(), X.columns[1]: x2_surf.ravel()})
        y_plane = model.predict(pts).reshape(x1_surf.shape)

        # Plot the regression plane similar to the original
        ax.plot_surface(x1_surf, x2_surf, y_plane, color="red", alpha=0.3, label='Predicted Plane')

        # Set axis labels and title to mirror multiple_linear_regression.py
        ax.set_xlabel('x1 (Total Years of Experience - equivalent)')
        ax.set_ylabel('x2 (Rating)')
        ax.set_zlabel('Salary')
        ax.set_title('Salary Prediction (3D Regression Plane)')
        ax.legend()
        plt.show()

    elif n_features == 1:
        # Simple 2D scatter + regression line
        fig, ax = plt.subplots(figsize=(8, 6))
        ax.scatter(X.iloc[:, 0], y, color="blue", s=60, label="Actual Data")

        # Build line for the model
        x_vals = np.linspace(X.iloc[:, 0].min(), X.iloc[:, 0].max(), 100)
        y_vals = model.predict(x_vals.reshape(-1, 1))
        ax.plot(x_vals, y_vals, color="red", label="Regression Line")

        ax.set_xlabel(str(X.columns[0]))
        ax.set_ylabel("Target")
        ax.set_title("Linear Regression (1 feature)")
        ax.legend()
        plt.show()

    else:
        print(
            "Plotting skipped: more than 2 features. Reduce to 2 features to visualize the regression plane."
        )


def main(csv_path: Path = DEFAULT_CSV_PATH):
    try:
        data = load_dataset(csv_path)
    except Exception as exc:
        print(f"Error loading dataset: {exc}")
        sys.exit(1)

    # Define X and y using the same names as in `multiple_linear_regression.py`
    # x1 = YearsExperience, x2 = Rating, Output = Salary
    X = data[["x1", "x2"]]
    y = data["Output"]

    # Default behavior mirrors original script (train/test on same data)
    # You can change mode via command-line args (see __main__)
    mode = getattr(main, "mode", "self")
    test_size = getattr(main, "test_size", 0.33)
    random_state = getattr(main, "random_state", 42)
    cv = getattr(main, "cv", 5)

    model, y_pred, splits = train_and_evaluate(
        X, y, mode=mode, test_size=test_size, random_state=random_state, cv=cv
    )

    # Plot results when possible
    try:
        plot_results(X, y, model, splits=splits)
    except Exception as exc:
        print(f"Plotting failed: {exc}")


if __name__ == "__main__":
    # Allow optional path override via command-line
    import argparse

    parser = argparse.ArgumentParser(description="Salary prediction using linear regression")
    parser.add_argument("csv", nargs="?", help="Path to CSV file", default=str(DEFAULT_CSV_PATH))
    parser.add_argument(
        "--mode",
        choices=("self", "split", "cv"),
        default="self",
        help="Evaluation mode: 'self' (train/test same), 'split' (train/test split), or 'cv' (k-fold CV)",
    )
    parser.add_argument("--test-size", type=float, default=0.33, help="Test size for split mode")
    parser.add_argument("--random-state", type=int, default=42, help="Random state for split")
    parser.add_argument("--cv", type=int, default=5, help="Number of folds for cross-validation")

    args = parser.parse_args()

    csv_path = Path(args.csv)

    # Attach selected options to main so main() can pick them up (keeps signature simple)
    main.mode = args.mode
    main.test_size = args.test_size
    main.random_state = args.random_state
    main.cv = args.cv

    main(csv_path)
