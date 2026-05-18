# ADS1001 Malaysia Weather Project

This repository contains Chen Zimo's Member 2 notebook for the ADS1001 group project on useful weather indicators for public communication in Malaysia.

## Main Notebook

- `Chen nootbook.ipynb`

The notebook focuses on dataset overview, data cleaning, missing-value treatment, data quality checks, feature preparation, and creation of an analysis-ready weather dataset for later group analysis.

## Project Focus

The notebook prepares weather data for analysing public-facing indicators such as:

- outdoor comfort
- rainfall conditions
- wind-related risk
- UV exposure

It also documents dataset limitations, including missing values, unusual weather readings, limited location coverage, and unavailable air-quality variables.

## Expected Data Files

The notebook expects input CSV files inside the `data/` folder:

- `data/malaysia_weather_raw.csv`
- `data/malaysia_weather_member2_cleaned_submitted.csv`

It exports the final cleaned dataset to:

- `data/malaysia_weather_cleaned_final.csv`

## How To Run

1. Open `Chen nootbook.ipynb` in Jupyter Notebook, JupyterLab, or VS Code.
2. Confirm the required CSV files are in the `data/` folder.
3. Run all cells from top to bottom.
4. Check the final validation table and exported cleaned CSV.

## Dependencies

The notebook uses:

- Python
- pandas
- numpy
- matplotlib
- IPython display tools

## Output

The final dataset includes cleaned weather measurements, imputation flag columns, datetime features, location checks, and derived variables such as `temperature_difference`, `gust_difference`, `rain_event`, `pressure_change`, `uv_category`, and `high_uv`.
