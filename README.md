# Delivery Market Analysis with SQL
## 🍕 Comparing Deliveroo, TakeAway and Uber Eats

- Duration: `1 week`
- Team: `Group`
  - Zelim: https://github.com/KhanZelim
  - Nicolaas: https://github.com/NicolaasDC
  - Moustafa: https://github.com/mgabil
  - Wouter: https://github.com/Zeegeuze

## 📖 Mission Objectives

Enhance your data engineering and analytical skills by:
- Working with SQL operations
- Exploring geospatial data analysis
- Extracting and visualizing insights from food delivery datasets
- Building data storytelling and presentation skills

## 🚀 The Mission

> We are a small start-up interested in creating a web app that compares prices and different services provided by food delivery apps in Belgium. To that end, we have hired your team to analyze databases provided by a consultant to uncover actionable insights for restaurant partners and consumers.  Our tech stack uses SQL and Python which your solution must use as well. Finally, you must present your intial findings in a week as we will meet with investors in the following week.

The objective is to explore trends, customer preferences, and market dynamics in the food delivery space. Conduct exploratory analysis, summarize findings, and present actionable insights.

## 🛢️ Data

The database provided is structured as three SQLite files.

## 🎯 Must-have Features (MVP)

Answer these key business questions:

1. What is the price distribution of menu items?
2. What is the distribution of restaurants per location?
3. Which are the top 10 pizza restaurants by rating?
4. Map locations offering kapsalons and their average price.
5. Compare restaurant distributions across UberEats, Deliveroo, and Takeaway. What are some of the market trends?

You can also answer these open ended questions:

1. How do delivery fees vary across platforms and locations?
2. Which restaurants have the best price-to-rating ratio?
3. Where are the delivery ‘dead zones’—areas with minimal restaurant coverage?
4. How does the availability of vegetarian and vegan dishes vary by area?
5. How do ratings of similar restaurants differ across Uber Eats, Deliveroo, and Takeaway?

## 📦 Repo Structure

```
├── Database_schemes/
│   ├── SQL_schema_deliveroo.png
│   ├── SQL_schema_takeaway.png
│   └── SQL_schema_ubereats.png
├── Databases/
│   ├── deliveroo.db
│   ├── georef-belgium-postal-codes@public.geojson
│   ├── takeaway.db
│   └── ubereats.db
├── Moustafa
├── Nicolaas
├── Wouter
├── Zelim
├── maps
├── .gitignore
├── main.ipynb
├── README.md
└── requirements.txt
```

## 🔧 Installation

Clone the repository to your local machine Set up your virtual enviroment and install the packages from the requirements.txt file
