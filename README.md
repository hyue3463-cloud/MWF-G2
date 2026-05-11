# Xu Zihao - UV Index Analysis

This branch contains Xu Zihao's individual contribution to the ADS1001 Malaysia Weather Forecast group project.

## Research question

**Which weather conditions correspond to the highest UV index values, and at what threshold should public UV warnings be issued?**

## Files

- `xu_zihao_uv_index_analysis.ipynb`: completed notebook for the UV Index research question.
- `data/malaysia_weather_cleaned.csv`: cleaned weather dataset used by the notebook.
- `metadata.json`: dataset metadata.

## Main findings

- The highest UV Index values are mainly concentrated from late morning to mid-afternoon.
- High UV tends to occur with warmer temperature, lower humidity than low-UV periods, and little or no current rainfall.
- Weather variables such as temperature and humidity are useful context, but they should not replace the UV Index itself.
- The recommended public UV warning threshold is **UV Index >= 6**.
- A lighter sun-protection reminder can begin at **UV Index >= 3**, while stronger alerts can be used at **UV Index >= 8** and **UV Index >= 11**.
