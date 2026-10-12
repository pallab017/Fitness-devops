# ACEest Fitness Application

## Overview
ACEest Fitness is a Python Flask application that provides fitness
program information and fitness-related calculations.

## Technologies
- Python and Flask
- Pytest
- Docker
- Jenkins
- GitHub Actions
- Git and GitHub

## Project Files
- app.py: Flask application
- test_app.py: Automated tests
- requirements.txt: Python dependencies
- Dockerfile: Docker image configuration
- .github/workflows/ci.yml: GitHub Actions workflow

## Run Locally
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install pytest
python app.py
