# ADS1001 Group Project

## Communicating Useful Weather Indicators for Public Weather Guidance in Malaysia

This repository contains the notebook and supporting files for one component of an ADS1001 group project. The broader project investigates which weather indicators are most useful for communicating outdoor comfort, UV risk, rainfall conditions, and changing weather patterns to the public in Malaysia.

## Client context
The client is a Malaysian public weather information service that wants to communicate weather conditions more clearly to residents, commuters, and outdoor users. Although many weather variables are available, not all of them are equally useful for public-facing communication.

## My research question
**How different are temperature and wind chill readings in Malaysia, and does wind chill provide additional value in explaining outdoor thermal comfort in a tropical climate?**

## Why this analysis matters
Wind chill is often used in weather reporting to describe how cold conditions feel when wind increases heat loss from the body. However, Malaysia has a tropical climate with generally warm conditions. This analysis tests whether wind chill adds meaningful value beyond ordinary temperature when communicating thermal comfort to the public.

## Dataset summary
The dataset contains weather observations from Malaysia, including variables such as:
- place, city, and state
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

The main variables used in this notebook are:
- `temperature`
- `wind_chill`

Supporting variable (for interpretation only):
- `wind_speed`

## Repository contents
- `ADS1001 notebook Q1.ipynb` — final notebook for the temperature versus wind chill analysis
- `malaysia_weather_data.csv` — source dataset used in the notebook
- `Data_Dictionary_Weather-Forecast.docx` — data dictionary describing the weather variables

## Analysis workflow
The notebook is structured to align with the ADS1001 assessment rubric and includes:
1. project background and motivation
2. data loading and initial inspection
3. data cleaning and preparation
4. comparison of temperature and wind chill
5. summary statistics and difference analysis
6. visual analysis using distributions and scatter plots
7. grouped comparison by wind speed conditions
8. interpretation, conclusion, and recommendation

## Key findings
- Temperature and wind chill are almost identical across the dataset.
- The relationship between the two variables is extremely strong.
- Most observations show either no difference or only a very small difference.
- In Malaysian tropical conditions, wind chill provides little additional value beyond temperature for public communication.

## Conclusion
The analysis shows that temperature and wind chill readings are not meaningfully different for most observations in this Malaysian dataset. As a result, wind chill does not appear to add substantial value for explaining outdoor thermal comfort in a tropical climate.

## Recommendation
For routine public weather communication in Malaysia:
- use **temperature** as the main indicator of thermal conditions
- avoid giving strong emphasis to **wind chill** in standard reporting
- consider using humidity-related or heat-stress-related indicators when explaining how uncomfortable the weather may feel outdoors

## Group members
- LYM
- Cedric
- Xana
- Chen
- Xu Zihao

## How to run
1. Place `malaysia_weather_data.csv` in the same folder as the notebook, or update the file path in the notebook.
2. Open `ADS1001 notebook Q1.ipynb` in Jupyter Notebook, JupyterLab, or VS Code.
3. Run all cells from top to bottom.

## Suggested libraries
- pandas
- numpy
- matplotlib

## Notes
- The notebook includes visible outputs to support notebook submission, poster preparation, and presentation use.
- The analysis is written as an individual contribution within a larger group project.
