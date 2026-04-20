# ADS1001 Group Project

## Project title
**Communicating Useful Weather Indicators for Public Weather Guidance in Malaysia**

## Group members
- LYM
- Cedric
- Xana
- Chen
- Xu Zihao

## Project overview
This project investigates which weather indicators are most useful for public weather communication in Malaysia. The client is a Malaysian public weather information service that wants clearer and more practical ways to communicate outdoor comfort, UV risk, rainfall conditions, and changing weather patterns.

Our group addresses this aim through five research questions, each focusing on a different part of the dataset.

## My individual focus question
**How different are temperature and wind chill readings in Malaysia, and does wind chill provide additional value in explaining outdoor thermal comfort in a tropical climate?**

## Why this question matters
Wind chill is commonly reported in weather information, but it is mainly designed for colder environments where wind increases heat loss from the human body. Malaysia has a tropical climate with generally warm conditions, so this analysis examines whether wind chill adds meaningful value beyond ordinary temperature for public communication.

## Dataset
The dataset contains weather-related variables collected in Malaysia, including:
- place, city, state
- temperature
- pressure
- dew point
- humidity
- wind speed
- gust
- wind chill
- UV index
- precipitation rate and precipitation total
- date and time fields

For this notebook, the main variables used are:
- `temperature`
- `wind_chill`
- `wind_speed`

## Repository contents
- `ADS1001_Q1_Temperature_vs_WindChill_Notebook_Final_Fixed.ipynb` — final notebook for the temperature vs wind chill analysis
- `malaysia_weather_data (1)(2).csv` — source dataset
- `Data_Dictionary_Weather-Forecast (3)(2).docx` — variable descriptions

## Analysis steps
The notebook follows these main steps:
1. Load and inspect the dataset
2. Check data structure and time coverage
3. Clean the variables used for analysis
4. Compare temperature and wind chill directly
5. Calculate the difference between the two variables
6. Use summary statistics, distributions, scatter plots, and grouped comparisons by wind speed
7. Interpret whether wind chill provides additional communication value in a tropical climate

## Key findings
- Temperature and wind chill are almost identical in the dataset.
- The correlation between temperature and wind chill is extremely high.
- Nearly all observations show either exact equality or only a very small difference between the two variables.
- This suggests that wind chill adds very limited extra information in Malaysian conditions.

## Conclusion
Temperature and wind chill readings in Malaysia are not meaningfully different in most observations. Based on this dataset, wind chill does **not** provide substantial additional value for explaining outdoor thermal comfort in a tropical climate.

## Recommendation to the client
For routine public weather communication in Malaysia:
- use **temperature** as the main indicator of thermal conditions
- avoid placing strong emphasis on **wind chill** in standard public reporting
- consider using humidity-related or heat-stress-related indicators when the goal is to communicate how uncomfortable the weather feels outdoors

## How to run the notebook
1. Make sure the CSV dataset is in the same folder as the notebook, or update the file path inside the notebook.
2. Open the notebook in Jupyter Notebook, JupyterLab, or VS Code.
3. Run all cells from top to bottom.

## Suggested Python libraries
- pandas
- numpy
- matplotlib

## Notes
- The notebook is written to align with the ADS1001 rubric, including background, data understanding, data cleaning, analysis, interpretation, section conclusion, and recommendations.
- Outputs are displayed in the notebook so it can support both presentation and poster preparation.