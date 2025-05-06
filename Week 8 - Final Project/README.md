# COVID-19 Global Data Tracker Project

## Overview
This project is a comprehensive analysis of global COVID-19 data, developed as the final project for the Feb-2025 Python Sessions (Week 8). Implemented in a Jupyter Notebook (`covid-19-analysis.ipynb`), it leverages Python libraries to create interactive visualizations and dashboards, offering insights into the pandemic's global impact.

## Features
- **Data Visualizations**:
  - Doughnut chart for vaccination status.
  - Line chart for cumulative vaccinations over time.
  - Bar chart for daily new cases across countries.
  - Heatmap for correlations between COVID-19 metrics.
  - Choropleth map for total cases by country.
- **Interactive Dashboard**:
  - Filterable by country, year, and month, with table and chart view options.
- **Robust Data Handling**:
  - Downloads and processes large datasets with retry mechanisms.
- **Summary Insights**:
  - Consolidates key findings on vaccination disparities, case trends, and correlations.

## Requirements
- **Python 3.12.7** or later
- Required libraries:
  - `pandas`
  - `numpy`
  - `matplotlib`
  - `seaborn`
  - `requests`
  - `tqdm`
  - `plotly.express`
  - `ipywidgets`
  - `IPython`
- Jupyter Notebook environment
- Internet connection for data download

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Brian-Masheti/Feb-2025-Python-Sessions.git
   cd Feb-2025-Python-Sessions/Week_8
   ```

2. Set up a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies using the requirements.txt file included in the repository:
   ```bash
   pip install -r requirements.txt
   ```
   
   This will install all necessary packages (latest versions).
   
   Alternatively, you can install the key packages individually:
   ```bash
   pip install pandas numpy matplotlib seaborn requests tqdm plotly ipywidgets ipython jupyter
   ```

4. Ensure Jupyter Notebook is installed:
   ```bash
   pip install jupyter
   ```

## Usage
1. Open the Jupyter Notebook file using one of these methods:
   - **Classic Jupyter Notebook**:
     ```bash
     jupyter notebook
     ```
   - **VS Code/Cursor**: Open the file with VS Code/Cursor with Jupyter extension installed
   - **Anaconda Navigator**: Launch Jupyter Notebook or JupyterLab from Anaconda
   - **Google Colab**: Upload the notebook to Google Colab
   - **Jovian**: Upload to Jovian.ai
   - Any other Python environment with Jupyter support

2. Run all cells to:
   - Download and process the COVID-19 dataset.
   - Generate visualizations and the interactive dashboard.
   - Explore the "Summary of Key Insights" section.
3. Use the dashboard to filter data by country, year, month, and metrics, switching between "Table" and "Chart" views.

## Data Source
- **Source**: Our World in Data COVID-19 Dataset
- **Details**: Includes daily and cumulative metrics (e.g., total cases, new cases, total deaths, total vaccinations) and demographic indicators.
- **Download**: Handled programmatically within the notebook.

## Key Insights
- **Vaccination Coverage**: 82.6% of the population is unvaccinated, with only 17.4% vaccinated, indicating low global vaccination turnout.
- **Cumulative Vaccinations**: India leads with over 2 billion vaccinations by 2024, while Kenya lags at 0.1 billion.
- **Daily New Cases**: India and Brazil peaked at 2.5 million and 2 million cases in 2021, respectively, while Kenya peaked at 0.5 million.
- **Correlations**: Strong correlations (1.00) between total cases/deaths and new cases/deaths, with weak correlations (0.04–0.33) between vaccinations and case/death metrics.
- **Geographic Distribution**: Choropleth map shows varying total case impacts globally.
- **Dashboard Insights**: Highlights Kenya's lower cases and vaccinations compared to India and the USA.

## File Structure
- `covid-19-analysis.ipynb`: Main notebook for the project.
- `owid-covid-data.csv`: Locally saved dataset (generated after running the notebook).
- `requirements.txt`: List of required Python packages.
- `README.md`: This file.

## Acknowledgments
- Data provided by Our World in Data.
- Built with Python, Jupyter Notebook, and data science libraries.
- Thanks to the Feb-2025 Python Sessions instructors and peers for guidance.

## Contact
For questions or contributions, please contact savatiabrian92@gmail.com.