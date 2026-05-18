from pathlib import Path
import os
import textwrap

ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "poster_assets"
OUT_DIR.mkdir(exist_ok=True)
(OUT_DIR / ".mplconfig").mkdir(exist_ok=True)
os.environ["MPLCONFIGDIR"] = str(OUT_DIR / ".mplconfig")

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle
from matplotlib.lines import Line2D


DATA_PATH = ROOT / "data" / "weather_data_cleaned.csv"
PDF_PATH = OUT_DIR / "MWF-G2_A1_weather_poster.pdf"
PNG_PATH = OUT_DIR / "MWF-G2_A1_weather_poster_preview.png"


COLORS = {
    "bg": "#F7FAFB",
    "ink": "#1F2D36",
    "muted": "#58717A",
    "teal_dark": "#083D4F",
    "teal": "#0B6E78",
    "sky": "#67B7DC",
    "sky_light": "#E8F3F7",
    "yellow": "#F3C74B",
    "yellow_light": "#FFF4CC",
    "coral": "#E76F51",
    "coral_light": "#FCE4DC",
    "green": "#2A9D8F",
    "green_light": "#DDF3EE",
    "line": "#D4E3E8",
    "white": "#FFFFFF",
}


plt.rcParams.update({
    "font.family": "Arial",
    "pdf.fonttype": 42,
    "ps.fonttype": 42,
    "axes.titleweight": "bold",
    "axes.labelcolor": COLORS["ink"],
    "xtick.color": COLORS["muted"],
    "ytick.color": COLORS["muted"],
})


def add_round_box(ax, x, y, w, h, fc=COLORS["white"], ec=COLORS["line"], lw=1.4, radius=0.55, z=1):
    patch = FancyBboxPatch(
        (x, y),
        w,
        h,
        boxstyle=f"round,pad=0.018,rounding_size={radius}",
        linewidth=lw,
        edgecolor=ec,
        facecolor=fc,
        zorder=z,
    )
    ax.add_patch(patch)
    return patch


def add_panel(ax, x, y, w, h, number, title, accent=COLORS["teal"], fc=COLORS["white"]):
    add_round_box(ax, x, y, w, h, fc=fc, ec=COLORS["line"], lw=1.35, radius=0.7)
    ax.add_patch(Rectangle((x, y + h - 2.25), w, 2.25, color=accent, zorder=2))
    ax.text(x + 0.85, y + h - 1.12, number, fontsize=13, fontweight="bold",
            color=COLORS["white"], va="center", ha="left", zorder=3)
    ax.text(x + 3.1, y + h - 1.12, title, fontsize=14.5, fontweight="bold",
            color=COLORS["white"], va="center", ha="left", zorder=3)


def add_wrapped(ax, x, y, text, width=42, fontsize=10.2, color=COLORS["ink"],
                weight="normal", lineheight=1.12, va="top", z=5):
    lines = []
    for paragraph in text.split("\n"):
        if not paragraph.strip():
            lines.append("")
        else:
            lines.extend(textwrap.wrap(paragraph, width=width, break_long_words=False))
    rendered = "\n".join(lines)
    ax.text(x, y, rendered, fontsize=fontsize, color=color, fontweight=weight,
            va=va, ha="left", linespacing=lineheight, zorder=z)
    return len(lines)


def pill(ax, x, y, text, fc, color=COLORS["ink"], fontsize=9.4, weight="bold", pad=0.35):
    width = max(3.2, len(text) * fontsize * 0.018 + 2 * pad)
    height = fontsize * 0.047 + 0.42
    add_round_box(ax, x, y - height / 2, width, height, fc=fc, ec=fc, lw=0, radius=0.35, z=4)
    ax.text(x + width / 2, y, text, fontsize=fontsize, color=color, fontweight=weight,
            ha="center", va="center", zorder=5)
    return width


def chart_axes(fig, x, y, w, h):
    return fig.add_axes([x / 100, y / 70, w / 100, h / 70])


def style_small_chart(cax):
    cax.spines[["top", "right"]].set_visible(False)
    cax.spines["left"].set_color(COLORS["line"])
    cax.spines["bottom"].set_color(COLORS["line"])
    cax.tick_params(labelsize=7.2, length=2.5, color=COLORS["line"])
    cax.grid(True, axis="y", color="#EAF1F4", linewidth=0.7)


def metric(ax, x, y, value, label, color=COLORS["teal"], w=7.6):
    add_round_box(ax, x, y, w, 3.75, fc=COLORS["sky_light"], ec="#C9E1EA", lw=0.9, radius=0.45, z=3)
    ax.text(x + 0.45, y + 2.35, value, fontsize=15, fontweight="bold",
            color=color, ha="left", va="center", zorder=4)
    add_wrapped(ax, x + 0.45, y + 1.22, label, width=18, fontsize=7.4,
                color=COLORS["muted"], z=4)


def decision_badge(ax, x, y, label, fc, width=9.2):
    add_round_box(ax, x, y, width, 1.65, fc=fc, ec=fc, lw=0, radius=0.45, z=4)
    ax.text(x + width / 2, y + 0.83, label, fontsize=8.6, fontweight="bold",
            color=COLORS["ink"], ha="center", va="center", zorder=5)


def main():
    weather = pd.read_csv(DATA_PATH)

    temp_corr = weather["temperature"].corr(weather["wind_chill"])
    temp_diff_mean = weather["temperature_difference"].mean()
    temp_diff_med = weather["temperature_difference"].median()
    hum_dew_corr = weather["humidity"].corr(weather["dew_point"])

    rain_rate = weather["rain_event"].mean() * 100
    pressure_corr = weather["pressure"].corr(weather["precipitation_total"])
    pressure_groups = pd.qcut(weather["pressure"], 4, duplicates="drop")
    rain_by_pressure = weather.groupby(pressure_groups, observed=True)["rain_event"].mean() * 100

    wind_corr = weather["wind_speed"].corr(weather["gust"])
    mean_wind = weather["wind_speed"].mean()
    mean_gust = weather["gust"].mean()
    mean_gust_diff = weather["gust_difference"].mean()
    high_gust = weather["gust"].quantile(0.90)

    uv_order = ["Low", "Moderate", "High", "Very High", "Extreme"]
    uv_counts = weather["uv_category"].value_counts().reindex(uv_order).fillna(0).astype(int)
    high_uv = (weather["uv_index"] >= 6).mean() * 100
    very_high_uv = (weather["uv_index"] >= 8).mean() * 100
    extreme_uv = (weather["uv_index"] >= 11).mean() * 100
    uv_by_hour = weather.groupby("hour")["uv_index"].mean()

    fig = plt.figure(figsize=(33.11, 23.39), dpi=150, facecolor=COLORS["bg"])
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 70)
    ax.axis("off")

    # Header
    ax.add_patch(Rectangle((0, 62), 100, 8, color=COLORS["teal_dark"], zorder=0))
    ax.add_patch(Rectangle((0, 61.4), 100, 0.6, color=COLORS["yellow"], zorder=1))
    ax.text(3, 67.4, "Which Weather Indicators Matter Most", fontsize=33,
            fontweight="bold", color=COLORS["white"], ha="left", va="center")
    ax.text(3, 64.7, "for Public Communication in Malaysia?", fontsize=31,
            fontweight="bold", color=COLORS["white"], ha="left", va="center")
    ax.text(3.1, 62.75,
            "ADS1001 MWF-G2 | Client: Malaysian public weather information service | Group MWF-G2: [add member names]",
            fontsize=11.6, color="#D8EEF3", ha="left", va="center")
    add_round_box(ax, 68.0, 63.15, 28.8, 5.25, fc=COLORS["yellow"], ec=COLORS["yellow"], radius=0.7, z=2)
    ax.text(69.2, 66.6, "Big takeaway", fontsize=11.2, fontweight="bold",
            color=COLORS["teal_dark"], ha="left")
    ax.text(69.2, 65.05, "Use indicators the public can", fontsize=18,
            fontweight="bold", color=COLORS["teal_dark"], ha="left")
    ax.text(69.2, 63.65, "act on immediately.", fontsize=18,
            fontweight="bold", color=COLORS["teal_dark"], ha="left")

    # Top row
    add_panel(ax, 3, 45.5, 21.5, 13.7, "1", "Member 1: Client Problem", COLORS["teal"])
    add_wrapped(ax, 4.05, 56.45,
                "Client: a Malaysian public weather information service for residents, commuters, outdoor users and event organisers.",
                width=44, fontsize=10.4)
    add_wrapped(ax, 4.05, 53.05,
                "Problem: many raw weather variables are available, but not all are easy for the public to understand or act on.",
                width=44, fontsize=10.4)
    add_round_box(ax, 4.0, 46.55, 19.5, 3.25, fc=COLORS["green_light"], ec="#B8DDD4", lw=1.0, radius=0.45)
    add_wrapped(ax, 4.7, 48.95,
                "Research question: Which indicators best communicate comfort, rainfall, wind risk and UV exposure?",
                width=52, fontsize=10.6, weight="bold", color=COLORS["teal_dark"])

    add_panel(ax, 26, 45.5, 21.5, 13.7, "2", "Member 2: Data Pipeline", COLORS["sky"])
    ax.text(27.15, 56.25, "ADS1001 Malaysia weather records", fontsize=11,
            fontweight="bold", color=COLORS["ink"], ha="left")
    ax.text(27.15, 54.8, "Selected Kuala Lumpur + Pulau Pinang locations", fontsize=9.6,
            color=COLORS["muted"], ha="left")
    ax.text(27.15, 53.55, "2018-01-17 to 2023-08-30", fontsize=9.6,
            color=COLORS["muted"], ha="left")
    add_round_box(ax, 27.0, 49.7, 7.6, 2.9, fc=COLORS["coral_light"], ec="#F3C6B9", lw=1.0, radius=0.45)
    ax.text(30.8, 51.55, "RAW", fontsize=9, fontweight="bold", color=COLORS["coral"], ha="center")
    ax.text(30.8, 50.45, "57,475 rows\n19 columns", fontsize=8.8, color=COLORS["ink"],
            ha="center", va="center", linespacing=1.1)
    ax.add_line(Line2D([35.0, 38.4], [51.2, 51.2], color=COLORS["teal"], lw=2.2))
    ax.text(36.7, 52.0, "clean", fontsize=8.4, color=COLORS["teal"], ha="center")
    add_round_box(ax, 38.7, 49.7, 7.6, 2.9, fc=COLORS["green_light"], ec="#B8DDD4", lw=1.0, radius=0.45)
    ax.text(42.5, 51.55, "CLEAN", fontsize=9, fontweight="bold", color=COLORS["green"], ha="center")
    ax.text(42.5, 50.45, "51,693 rows\n38 columns", fontsize=8.8, color=COLORS["ink"],
            ha="center", va="center", linespacing=1.1)
    metric(ax, 27.0, 46.2, "0", "duplicate rows", COLORS["teal"], w=5.7)
    metric(ax, 33.1, 46.2, "0", "missing in main columns", COLORS["teal"], w=6.5)
    metric(ax, 40.0, 46.2, "7", "engineered features", COLORS["teal"], w=6.3)

    add_panel(ax, 50, 45.5, 47, 13.7, "CORE", "Decision Matrix: Public Communication Value", COLORS["teal_dark"])
    ax.text(51.2, 56.4, "Lead with simple, actionable measures", fontsize=14.5,
            fontweight="bold", color=COLORS["teal_dark"], ha="left")
    ax.text(51.2, 54.85,
            "The best public indicators are understandable, actionable, useful and supported by data.",
            fontsize=10.2, color=COLORS["muted"], ha="left")
    add_round_box(ax, 51.0, 47.0, 29.0, 6.8, fc=COLORS["green_light"], ec="#B8DDD4", lw=1.0, radius=0.55)
    ax.text(52.0, 52.75, "MAIN PUBLIC-FACING INDICATORS", fontsize=10.8,
            fontweight="bold", color=COLORS["green"], ha="left")
    main_badges = ["Temperature", "Humidity", "Precipitation", "Wind speed", "Gust", "UV categories"]
    for i, lab in enumerate(main_badges):
        decision_badge(ax, 52.0 + (i % 3) * 8.8, 50.5 - (i // 3) * 2.05, lab,
                       COLORS["white"], width=8.1)
    add_round_box(ax, 81.2, 47.0, 14.5, 6.8, fc=COLORS["yellow_light"], ec="#EDD98F", lw=1.0, radius=0.55)
    ax.text(82.0, 52.75, "SUPPORTING / INTERNAL", fontsize=10.4,
            fontweight="bold", color="#A67800", ha="left")
    for i, lab in enumerate(["Wind chill", "Dew point", "Pressure"]):
        decision_badge(ax, 82.0, 50.5 - i * 1.7, lab, COLORS["white"], width=12.5)
    ax.text(51.2, 46.0,
            "Final answer: prioritise temperature, humidity, precipitation rate/total, wind speed, gust and UV index categories.",
            fontsize=10.4, fontweight="bold", color=COLORS["ink"], ha="left")

    # Middle row panels
    add_panel(ax, 3, 21.2, 30.7, 21.6, "3", "Member 3: Outdoor Comfort Evidence", COLORS["green"])
    pill(ax, 4.2, 40.2, "Method: correlation + difference analysis", COLORS["green_light"], color=COLORS["teal_dark"], fontsize=8.7)
    metric(ax, 4.2, 35.9, f"{temp_corr:.3f}", "temperature vs wind chill correlation", COLORS["green"], w=8.2)
    metric(ax, 13.0, 35.9, f"{temp_diff_mean:.3f}", "mean temp difference, deg C", COLORS["green"], w=8.2)
    metric(ax, 21.8, 35.9, f"{hum_dew_corr:.3f}", "humidity vs dew point correlation", COLORS["green"], w=8.2)

    cax = chart_axes(fig, 4.6, 27.0, 12.8, 7.6)
    sample = weather.sample(min(2600, len(weather)), random_state=7)
    cax.scatter(sample["temperature"], sample["wind_chill"], s=6, alpha=0.13, color=COLORS["green"], linewidths=0)
    lo = min(weather["temperature"].min(), weather["wind_chill"].min())
    hi = max(weather["temperature"].max(), weather["wind_chill"].max())
    cax.plot([lo, hi], [lo, hi], color=COLORS["coral"], lw=1.5)
    cax.set_title("Temperature and wind chill nearly overlap", fontsize=8.5, pad=5)
    cax.set_xlabel("Temperature", fontsize=7.5)
    cax.set_ylabel("Wind chill", fontsize=7.5)
    style_small_chart(cax)

    cax = chart_axes(fig, 18.8, 27.0, 12.8, 7.6)
    labels = ["Mean humidity", "Mean dew point"]
    vals = [weather["humidity"].mean(), weather["dew_point"].mean()]
    bars = cax.bar(labels, vals, color=[COLORS["sky"], COLORS["yellow"]], width=0.55)
    cax.bar_label(bars, labels=[f"{vals[0]:.1f}%", f"{vals[1]:.1f} deg C"], fontsize=7.4, padding=2)
    cax.set_title("Humidity is more intuitive for public comfort", fontsize=8.5, pad=5)
    cax.set_ylim(0, 100)
    style_small_chart(cax)
    cax.tick_params(axis="x", labelrotation=0)

    add_round_box(ax, 4.2, 22.15, 28.2, 3.8, fc=COLORS["green_light"], ec="#B8DDD4", lw=1.0, radius=0.45)
    add_wrapped(ax, 4.9, 25.05,
                f"Conclusion: wind chill adds little routine value here (median difference {temp_diff_med:.0f} deg C). Lead public comfort messages with temperature and humidity; use dew point as technical support.",
                width=82, fontsize=9.4, weight="bold", color=COLORS["teal_dark"])

    add_panel(ax, 35.0, 21.2, 30.7, 21.6, "4", "Member 4: Risk & Warning Evidence", COLORS["coral"])
    pill(ax, 36.2, 40.2, "Method: grouped rates + warning categories", COLORS["coral_light"], color="#9D3D29", fontsize=8.7)
    metric(ax, 36.2, 35.9, f"{rain_rate:.1f}%", "rain event rate", COLORS["coral"], w=7.2)
    metric(ax, 43.9, 35.9, f"{pressure_corr:.3f}", "pressure vs precipitation corr.", COLORS["coral"], w=8.2)
    metric(ax, 52.7, 35.9, f"{wind_corr:.3f}", "wind speed vs gust corr.", COLORS["coral"], w=8.2)

    cax = chart_axes(fig, 36.4, 28.0, 8.6, 6.6)
    cax.bar(range(len(rain_by_pressure)), rain_by_pressure.values, color=COLORS["sky"], width=0.62)
    cax.set_title("Rain event rate by pressure quartile", fontsize=8.2, pad=5)
    cax.set_ylabel("% rain events", fontsize=7.4)
    cax.set_xticks(range(len(rain_by_pressure)))
    cax.set_xticklabels(["Q1", "Q2", "Q3", "Q4"], fontsize=7.2)
    cax.set_ylim(0, max(rain_by_pressure.values) + 8)
    style_small_chart(cax)

    cax = chart_axes(fig, 46.4, 28.0, 8.6, 6.6)
    bars = cax.bar(["Wind\nspeed", "Gust"], [mean_wind, mean_gust],
                   color=[COLORS["sky"], COLORS["coral"]], width=0.55)
    cax.axhline(high_gust, color=COLORS["teal_dark"], lw=1.3, linestyle="--")
    cax.text(0.1, high_gust + 0.3, "90th pct gust 9.4", fontsize=7.0, color=COLORS["teal_dark"])
    cax.bar_label(bars, labels=[f"{mean_wind:.2f}", f"{mean_gust:.2f}"], fontsize=7.4, padding=2)
    cax.set_title("Gust captures sudden wind risk", fontsize=8.2, pad=5)
    cax.set_ylim(0, 11)
    style_small_chart(cax)

    cax = chart_axes(fig, 56.2, 28.0, 7.6, 6.6)
    uv_colors = [COLORS["green"], COLORS["yellow"], "#F4A261", COLORS["coral"], COLORS["teal_dark"]]
    left = 0
    for count, color, label in zip(uv_counts.values, uv_colors, uv_counts.index):
        cax.barh([0], [count], left=left, color=color, height=0.55)
        if count > 15000:
            cax.text(left + count / 2, 0, label.split()[0], ha="center", va="center",
                     fontsize=6.5, color=COLORS["white"] if color in [COLORS["coral"], COLORS["teal_dark"], COLORS["green"]] else COLORS["ink"],
                     fontweight="bold")
        left += count
    cax.set_title("UV categories translate risk", fontsize=8.2, pad=5)
    cax.set_yticks([])
    cax.set_xticks([0, 25000, 50000])
    cax.set_xticklabels(["0", "25k", "50k"], fontsize=7.0)
    cax.spines[["top", "right", "left"]].set_visible(False)
    cax.spines["bottom"].set_color(COLORS["line"])
    cax.tick_params(length=2, color=COLORS["line"])
    cax.text(0.0, -0.38, "Counts: 41.0k low | 6.1k moderate | 2.5k high | 1.6k very high | 0.5k extreme",
             transform=cax.transAxes, fontsize=6.4, color=COLORS["muted"], ha="left", va="top")

    add_round_box(ax, 36.2, 22.15, 28.2, 4.75, fc=COLORS["coral_light"], ec="#F3C6B9", lw=1.0, radius=0.45)
    add_wrapped(ax, 36.9, 25.95,
                f"Conclusion: precipitation is clearer than pressure for rain alerts. Communicate gust separately when sudden wind risk matters. UV is strong because categories map directly to public action (high UV >= 6: {high_uv:.1f}%).",
                width=82, fontsize=9.2, weight="bold", color="#7F321F")

    add_panel(ax, 67.0, 21.2, 30.0, 21.6, "5", "Member 5: Recommendation & Next Steps", COLORS["teal_dark"])
    ax.text(68.2, 40.15, "Recommended public message stack", fontsize=13.2,
            fontweight="bold", color=COLORS["teal_dark"], ha="left")
    rec_rows = [
        ("Comfort", "Temperature + humidity", "Wind chill / dew point as context"),
        ("Rain", "Precipitation rate or total", "Pressure for internal context"),
        ("Wind", "Wind speed + gust", "Gust warning for sudden risk"),
        ("UV", "Standard UV categories", "Time-of-day support"),
    ]
    y0 = 37.15
    for i, (area, lead, support) in enumerate(rec_rows):
        y = y0 - i * 2.85
        add_round_box(ax, 68.2, y - 0.1, 27.4, 2.3, fc=COLORS["white"], ec=COLORS["line"], lw=0.9, radius=0.35)
        ax.text(69.0, y + 1.35, area, fontsize=9.4, fontweight="bold", color=COLORS["teal"], ha="left")
        ax.text(77.0, y + 1.35, lead, fontsize=9.4, fontweight="bold", color=COLORS["ink"], ha="left")
        ax.text(77.0, y + 0.35, support, fontsize=8.0, color=COLORS["muted"], ha="left")

    ax.text(68.2, 25.35, "Limitations", fontsize=11.0, fontweight="bold", color=COLORS["teal_dark"], ha="left")
    add_wrapped(ax, 68.2, 24.2,
                "Selected KL and Pulau Pinang locations only; missing values and imputation may affect patterns; uneven location representation; associations are not causation; public understanding was not directly surveyed.",
                width=73, fontsize=8.2, color=COLORS["ink"])
    ax.text(68.2, 21.95, "Future work", fontsize=11.0, fontweight="bold", color=COLORS["teal_dark"], ha="left")
    add_wrapped(ax, 76.2, 21.95,
                "expand locations; test messages with public users; add forecasting models.",
                width=58, fontsize=8.2, color=COLORS["ink"], va="top")

    # Bottom: speaking plan and references
    add_round_box(ax, 3, 6.2, 94, 11.8, fc=COLORS["white"], ec=COLORS["line"], lw=1.25, radius=0.75)
    ax.text(4.2, 16.4, "Presentation Handoff: same story, five equal 2-minute turns", fontsize=14.3,
            fontweight="bold", color=COLORS["teal_dark"], ha="left")
    handoff = [
        ("M1 0:00-2:00", "Motivation, client problem, research question."),
        ("M2 2:00-4:00", "Dataset, cleaning decisions, engineered features."),
        ("M3 4:00-6:00", "Comfort evidence: temperature, humidity, dew point."),
        ("M4 6:00-8:00", "Warnings: precipitation, gust, UV categories."),
        ("M5 8:00-10:00", "Recommendation, limitations, future work, Q&A bridge."),
    ]
    col_w = 18.0
    for i, (head, body) in enumerate(handoff):
        x = 4.3 + i * col_w
        add_round_box(ax, x, 8.0, 16.7, 6.6, fc=COLORS["sky_light"] if i % 2 == 0 else COLORS["yellow_light"],
                      ec="#D3E4EA", lw=0.8, radius=0.45)
        ax.text(x + 0.7, 13.5, head, fontsize=9.8, fontweight="bold",
                color=COLORS["teal_dark"], ha="left", va="center")
        add_wrapped(ax, x + 0.7, 12.2, body, width=34, fontsize=8.4, color=COLORS["ink"])

    ax.text(3.2, 4.4,
            "References: ADS1001 Malaysia weather dataset; ADS1001 Project Guidelines and Rubric; standard UV index public health categories.",
            fontsize=8.8, color=COLORS["muted"], ha="left", va="center")
    ax.text(96.8, 4.4, "A1 landscape poster | Print at full size",
            fontsize=8.8, color=COLORS["muted"], ha="right", va="center")

    fig.savefig(PDF_PATH, facecolor=COLORS["bg"])
    fig.savefig(PNG_PATH, dpi=160, facecolor=COLORS["bg"])
    print(f"Wrote {PDF_PATH}")
    print(f"Wrote {PNG_PATH}")


if __name__ == "__main__":
    main()
