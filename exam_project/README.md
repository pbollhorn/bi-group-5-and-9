# Exam Project: Business Intelligence for a Fictional Movie Production Company

Group members:
- Peter Bollhorn
- Tobias Thormod Birk Nielsen

## Introduction

In this exam project we will perform Business Intelligence (BI) analysis for a fictional movie production company, in order to provide insights that can benefit this company for their planning of new movies. The fictional movie production company releases movies to theaters, as well as directly to streaming platforms.

We will work with movie data from The Movie Database (TMDB) https://www.themoviedb.org/ from the United States from the years 2000-2023.

From TMDB we get this information which can be used to asses the success of the movies:
- budget 
- revenue (from theatical run)
- vote_average (average score as voted 1-10 from TMDB users)

The movie budgets and revenues are given by TMDB in USD without adjusting for inflation.
We will adjust the amounts for inflation and analyze everything in 2023 USD.

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
In our data we found out that a lot of movies don't have budget and revenue information.
xxxx movies have this information, and of these movies 61% made a profit and 39% made a loss.
However, we also discovered that revenue is not reliable to predict a movies success.
Instead we looked at budget vs. vote_average and found a weak linear relationship.

#### Lead actor age and gender:


#### Predicting movie rating:
We took all the 6200 movies that have budget information and tried to predict the movie rating (good, ok, bad)

#### Sentiment of movie overview:






