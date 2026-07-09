# Tourism Industry Analytics

Visitor Trends, Seasonal Demand, Economic Impact, and Travel Pattern Analysis

## Project Overview

The tourism industry plays a major role in economic growth and employment generation worldwide. This project analyzes tourism and hospitality data to identify meaningful patterns in tourist arrivals, hotel occupancy, tourism revenue, customer behavior, and travel trends — helping tourism organizations improve business strategy, customer satisfaction, and revenue generation.

## Dataset

**Source:** `Tourism_Hospitality_Industry_Analysis.csv`
**Size:** 500 records × 23 columns
**Coverage:** 20 countries, 56 cities, years 2020–2024

Key fields include tourist arrivals, purpose of visit, average stay, spending, hotel occupancy/rating/price, tourism revenue, employment, GDP contribution, flights, airport traffic, eco-tourism revenue, and carbon footprint.

## Objectives

- Analyze visitor trends across destinations
- Identify seasonal tourism demand
- Study tourist spending behavior
- Analyze hotel occupancy and ratings
- Examine tourism revenue patterns
- Discover economic impact of tourism
- Build an interactive analytics dashboard

## Technologies Used

- Python (pandas, numpy)
- Matplotlib, Seaborn, Plotly (visualization)
- Jupyter Notebook (analysis)
- Streamlit (interactive dashboard)

## Project Structure

```text
Tourism-Industry-Analytics/
│
├── data/
│   ├── raw/                        # Original dataset
│   └── cleaned/                    # Cleaned dataset with engineered features
├── notebooks/
│   └── tourism_analysis.ipynb      # Full EDA + 20 visualizations + insights
├── dashboard/
│   └── app.py                      # Streamlit interactive dashboard
├── visuals/                        # 20 exported PNG charts
├── report/                         # Final written report
├── presentation/                   # Slide deck
├── requirements.txt
└── README.md
```

## Installation

```bash
pip install -r requirements.txt
```

## Running the Notebook

```bash
jupyter notebook notebooks/tourism_analysis.ipynb
```

## Running the Dashboard

```bash
cd dashboard
streamlit run app.py
```

## Key Insights

1. China draws the largest tourist volume and leads eco-tourism revenue.
2. Hotel quality drives revenue — 5-star properties post the highest average tourism revenue.
3. January is the peak demand month; August is the weakest.
4. Tourism revenue is driven mainly by tourist spending and eco-tourism revenue, not flight capacity.
5. Tourism employment has stayed stable (~26–27.5K jobs on average) across 2020–2024 despite revenue volatility.
6. Higher-revenue destinations tend to carry a larger carbon footprint — a sustainability trade-off worth monitoring.

## Business Recommendations

1. Increase marketing and promotional pricing during the August low season.
2. Upgrade unrated and 1-star hotel stock, since rating is tied to revenue performance.
3. Expand eco-tourism offerings in high-traffic markets like China.
4. Prioritize transport infrastructure upgrades in the lowest-scoring cities.
5. Target high-spending segments (e.g., business travel) with tailored packages.
6. Track and offset carbon footprint growth in high-revenue destinations.
