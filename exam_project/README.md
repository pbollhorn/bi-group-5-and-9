# Exam Project: Business Intelligence for a Fictional Movie Production Company

Group members:
- Peter Bollhorn
- Tobias Thormod Birk Nielsen

## Introduction

In this exam project we perform Business Intelligence (BI) analysis for a fictional movie production company in order to provide insights that can benefit this company. The fictional movie production company releases movies to theaters, as well as directly to streaming platforms.

We will work with movie data from The Movie Database (TMDB) https://www.themoviedb.org/ from the United States from the years 2000-2023.

TMDB 

We will work with budget and revenue from the theatrical release of movies, because this is relevant for movies released to cinemas.

We will also work with the rating of movies (from 1-10), because this is relevant for how well movies when released to streaming.

We will adjust the amounts for inflation and analyze everything in 2023 US-Dollars.


## Question we will explore

#### Movie budget and revenue:
- What budget, revenue, profit and ROI do other movies have?

#### Lead actor age and gender:
- What age and gender do other companies cast as lead actor in their movies? 
 (We have an hypothesis that female actors are more succesful under the age of 40, while male actors are more succesful after the age of 40)

(This is relevant for our fictional movie production company because we can advise them of trends in the industry.)

#### Sentiment of movie overview:

#### Predicting movie rating:
- Predicting if a movie will be good, ok or bad
- Can we make a classification machine learning model to predict movie rating?


## Please read our notebooks in this order
- **read_tmdb_data.ipynb:** Here we read JSON data from TMDB's API and store it as `movies.csv` and `persons.csv`.
- **inflation.ipynb:** Here we explain how we adjust for inflation.
- **preparation.ipynb**: Here we read in `movies.csv` and `persons.csv` and prepare the data by doing some cleaning and adjusting budget and revenue for inflation. The prepared data is saved as `movies_prepared.csv` and `persons_prepared.csv`.
- **movie_budget_and_revenue.ipynb:**
- **predicting_movie_rating.ipynb:**
- **lead_actor_age_and_gender:**
- **sentiment_of_movie_overview:**


## Conclusions

#### Movie budget and revenue:


#### Lead actor age and gender:


#### Predicting movie rating:


#### Sentiment of movie overview:






