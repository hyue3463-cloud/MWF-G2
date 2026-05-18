# MWF-G2 Poster + Presentation Handoff

Use this with `MWF-G2_A1_weather_poster.pdf`. Replace `Member 1` etc. with real names before submission.

## Overall Story

The project is not just describing Malaysian weather. It is helping a public weather information service decide which indicators should be prioritised in public messages.

Main answer:

> Prioritise temperature, humidity, precipitation rate/total, wind speed, gust, and UV index categories. Use wind chill, dew point, and pressure mainly as supporting/internal indicators.

## Member 1: Client Problem & Research Question

Poster area: top-left panel.

Talk focus:
- Introduce the client: Malaysian public weather information service.
- Explain why raw weather variables can confuse public users.
- State the research question: which indicators best communicate comfort, rainfall, wind risk and UV exposure?
- Transition: "To answer this, we first cleaned the dataset and engineered indicators that match the communication problem."

Key line:
> We judged indicators by whether they are understandable, actionable, useful, and supported by the data.

## Member 2: Data, Cleaning & Feature Engineering

Poster area: top-middle data pipeline panel.

Talk focus:
- Dataset covers selected Kuala Lumpur and Pulau Pinang locations from 2018-01-17 to 2023-08-30.
- Cleaning pipeline: 57,475 raw rows and 19 columns to 51,693 cleaned rows and 38 columns.
- Mention 5,782 rows removed, no duplicate rows, and 0 missing values in main measurement columns after cleaning.
- Feature engineering: `temperature_difference`, `gust_difference`, `rain_event`, `pressure_change`, `falling_pressure`, `uv_category`, `high_uv`.
- Transition: "The first communication theme is outdoor comfort."

Key line:
> The cleaning step makes the analysis usable, but missing values and imputation still remain a limitation.

## Member 3: Outdoor Comfort Evidence

Poster area: middle-left comfort panel.

Talk focus:
- Temperature vs wind chill: correlation = 0.999, mean difference = 0.002 deg C, median difference = 0.
- Interpretation: wind chill adds little routine communication value in this tropical dataset.
- Humidity vs dew point: humidity is more intuitive for the public; dew point is useful as technical support.
- Mention humidity/dew point correlation = 0.284.
- Transition: "For warnings, we need indicators that trigger clear public action."

Key line:
> For routine public comfort messages, temperature and humidity are clearer than wind chill and dew point.

## Member 4: Public Risk & Warning Evidence

Poster area: middle-centre risk and warning panel.

Talk focus:
- Rainfall: rain event rate = 25.9%; pressure vs precipitation total correlation = 0.046.
- Interpretation: precipitation is clearer than pressure for public rainfall alerts.
- Wind: wind speed vs gust correlation = 0.600; mean gust difference = 1.70; high gust threshold = 9.4.
- Interpretation: gust should be communicated separately when sudden wind risk matters.
- UV: categories make warnings easy; high UV rate (UV >= 6) = 8.8%, very high/extreme (UV >= 8) = 4.0%, extreme (UV >= 11) = 1.0%.
- Transition: "These evidence blocks lead directly to our final indicator recommendation."

Key line:
> Warnings should use indicators that map directly to action: rain amount, gust risk, and UV categories.

## Member 5: Final Recommendation, Limitations & Future Work

Poster area: top decision matrix + middle-right recommendation panel.

Talk focus:
- Walk through the decision matrix.
- Main public-facing indicators: temperature, humidity, precipitation rate/total, wind speed, gust, UV index categories.
- Supporting/internal indicators: wind chill, dew point, pressure.
- Limitations: selected KL and Pulau Pinang locations only; missing values/imputation; uneven location representation; associations not causation; public understanding not directly surveyed.
- Future work: expand locations, test messages with public users, add forecasting models.
- Finish with the client-facing recommendation.

Closing line:
> For public communication, lead with simple, actionable measures and keep technical indicators as context.
