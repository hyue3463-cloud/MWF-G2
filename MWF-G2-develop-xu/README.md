# ADS1001 Project - Xu Zihao Branch

This branch contains Xu Zihao's individual work for the ADS1001 group project.

## Branch Purpose

- Branch name: `develop-xu`
- Main task: develop the analysis for the research question on `uv_index`
- Goal: identify which weather conditions correspond to the highest UV Index values and decide a practical public UV warning threshold

## My Research Question

**Which weather conditions correspond to the highest UV index values, and at what threshold should public UV warnings be issued?**

## Main Files

- Notebook: `xu_zihao_uv_index_analysis.ipynb`
- Dataset: `data/malaysia_weather_cleaned.csv`
- Metadata: `metadata.json`

## Research Focus

This branch focuses on the following main variable:

- `uv_index`

Supporting variables used for interpretation:

- `temperature`
- `humidity`
- `dew_point`
- `pressure`
- `wind_speed`
- `gust`
- `precipitation_rate`
- `precipitation_total`
- `hour`
- `month`

## Key Findings

- The highest UV Index values are mainly concentrated from late morning to mid-afternoon.
- High UV conditions tend to occur with warmer temperatures, lower humidity, and little or no current rainfall.
- Temperature and humidity are useful context variables, but they should not replace the UV Index itself.
- The recommended public UV warning threshold is **UV Index >= 6**.
- A lighter sun-protection reminder can begin at **UV Index >= 3**, and stronger alerts can be used at **UV Index >= 8**.

## How To Use

1. Open `xu_zihao_uv_index_analysis.ipynb`.
2. Run the notebook from top to bottom.
3. Make sure `data/malaysia_weather_cleaned.csv` stays in the `data` folder.
4. Check that all code cells run without error before committing changes.

## Notes

- Missing UV Index values are not changed to zero.
- This branch is for Xu Zihao's individual analysis before merging into the final group notebook.
- Final formatting may be adjusted later to match the full group submission.
