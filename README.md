# Machine Learning Experiments

A collection of machine learning models, experiments, and exercises in Python.

## Project Structure

```
MachineLearningExperiments/
├── src/
│   ├── machine_learning/      # ML models
│   │   ├── regression/        # Linear, polynomial, ridge regression
│   │   ├── classification/    # Decision trees, logistic regression
│   │   └── ensemble/          # Random forests
│   ├── preprocessing/         # Scalers, encoders, outlier detection
│   ├── analysis/              # EDA and forecasting
│   ├── exercises/             # Practice exercises (pandas, numpy)
│   ├── python_fundamentals/   # Python basics (week 1-4)
│   ├── assignments/           # Assignment files
│   └── utilities/             # Helper tools
├── testdata/                  # CSV data files
├── jpynb/                     # Jupyter notebooks
├── images/                    # Output plots
├── txt/                       # Text files
└── tests/                     # Test files
```

## Getting Started

1. Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Unix/macOS
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Install the package in development mode:
```bash
pip install -e .
```

## Recent Project Deliverables

### 1. ReneWind Neural Networks
- Notebook: `jpynb/ReneWind_neuralNetworks.ipynb`
- HTML Export: `jpynb/ReneWind_neuralNetworks.html`
- Goal: Predict wind turbine generator failures using neural-network experiments with cost-sensitive model selection.

### 2. EasyVisa Classification
- Notebook: `jpynb/EasyVisa_Classification.ipynb`
- HTML Export: `jpynb/EasyVisa_Classification.html`
- Goal: Classification modeling and comparison for visa approval outcomes.

## Export Notebook to HTML

Use the project virtual environment to export any notebook:

```bash
.venv/bin/python -m jupyter nbconvert --to html jpynb/<notebook_name>.ipynb --output-dir jpynb
```
