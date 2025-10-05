# Exam Project: Business Intelligence for a Fictional Movie Production Company

Group members:
- Peter Bollhorn
- Tobias Thormod Birk Nielsen

In our exam project we will perform Business Intelligence analysis for a fictional movie production company.
This company releases some movies in theaters and others directly to streaming platforms.



We will work with movie data from TMDB, with recent movies (2000-2023) from the United States.

We will work with budget and revenue from the theatrical release of movies, because this is relevant for movies released to cinemas.

We will also work with the rating of movies (from 1-10), because this is relevant for how well movies when released to streaming.


## Question we will explore
- What budget, revenue, profit and ROI do other movies have?
- Can we make a classification machine learning model to predict movie rating?



- What age and gender do other companies cast as lead actor in their movies? (This is relevant for our fictional movie production company because we can advise them of trends in the industry.)

## Please read our notebooks in this order
- **read_tmdb_data.ipynb:** Here we read `movies.csv` and `persons.csv`
- **inflation.ipynb:** Here we explain how we adjust for inflation.
- **preparation.ipynb**: Here we read in `movies.csv` and `persons.csv` and prepare the data by doing some cleaning and adjusting budget and revenue for inflation. The prepared data is saved as `movies_prepared.csv` and `persons_prepared.csv`.
- **movie_budget_and_revenue.ipynb:**
- **predicting_movie_rating.ipynb:**
- **actor_age_and_gender:**
- **sentiment_of_movie_overview:**


## Conclusions














We will address this challenge:
- Movie Profit: Which new movies should MovieStream produce in order to make the highest profit?


## Movie Profit

When a new movie is planned, it is normal for the producers of the movie to hope to make a profit:

**_Profit (USD) = Revenue (USD) – Budget (USD)_**

We will use TMDB Data from the recent years: Perhaps 5 years, 15 years or 25 years.

We will work with American Movies with Revenue, Budget and Profit in USD.

We will adjust the amounts for inflation and analyze everything in 2025 US-Dollars.
