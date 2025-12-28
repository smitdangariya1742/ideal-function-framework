# OOP Data Analysis Framework in Python

## Overview
This project implements a Python framework to:

- Select the best-fitting ideal functions from a set of candidates using least squares  
- Map test data points based on a deviation threshold (√2 × max training deviation)  
- Store results in an SQLite database  
- Visualize training, ideal, and mapped data using Bokeh  

## Requirements
- Python 3.8+  
- Install dependencies: pip install -r requirements.txt


## Usage
1. Place your CSV datasets in the project folder or update paths in `main.py`  
2. Run the program: python main.py

3. Outputs:
   - SQLite database `analysis.db`  
   - Interactive Bokeh visualization `output/result.html`

## Project Structure
main.py
data_loader.py
analyzer.py
mapper.py
database.py
visualizer.py
exceptions.py
tests/
requirements.txt
README.md