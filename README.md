# End-to-End-MLOps-Project

## Workflows

1. Update config.yaml
2. Update schema.yaml
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline
8. Update the main.py
9. Update the app.py

## Pipelines

1. Data Ingestion
2. Data Validation
3. Data Transformation
4. Model Trainer
5. Model Evaluation

## STEPS

Clone the repository

```bash
git clone https://github.com/CodeWithCharan/End-to-End-MLOps-Project.git
```
### STEP 01: Create a conda environment after opening the repository

```bash
conda create -n mlopsenv python=3.8 -y
```

```bash
conda activate mlopsenv
```


### STEP 02: install the requirements
```bash
pip install -r requirements.txt
```

### STEP 03: run app.py
```bash
python app.py
```

### STEP 04: After running the app.py, it will be available at:

- `http://127.0.0.1:8000`
- `http://localhost:8000`


## MLFlow

[Documentation](https://mlflow.org/docs/latest/index.html)

### CMD
```bash
mlflow ui
```

## DagsHub

[Documentation](https://dagshub.com/)

### Tracking URI:

- MLFLOW_TRACKING_URI = https://dagshub.com/CodeWithCharan/End-to-End-MLOps-Project.mlflow

- MLFLOW_TRACKING_USERNAME = CodeWithCharan

- MLFLOW_TRACKING_PASSWORD = YourAccessToken

### Run this to export as env variables:

```bash
export MLFLOW_TRACKING_URI=https://dagshub.com/CodeWithCharan/End-to-End-MLOps-Project.mlflow
```
```bash
export MLFLOW_TRACKING_USERNAME=CodeWithCharan
``` 
```bash
export MLFLOW_TRACKING_PASSWORD=YourAccessToken
```