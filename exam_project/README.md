# Exam Project: Business Intelligence for a Fictional Movie Production Company

Group members:
- Peter Bollhorn
- Tobias Thormod Birk Nielsen

## Introduction

In this exam project we will perform Business Intelligence (BI) analysis for a fictional movie production company, which has not produced any movies yet, but want to begin producing movies. Our goal is to provide insights to this company, which they can benefit from when planning their new movies.

In order to do this, we will analyze movie data from The Movie Database (TMDB) https://www.themoviedb.org/ from the United States from the years 2000-2023.

From TMDB we get this information which can be used to assess the success of the movies:
- **budget:** How much it cost to produce the movie.
- **revenue:** Box office from theatrical run, i.e. money earned from ticket sales in cinemas.
- **vote_average:** Average score (1-10) as voted by TMDB users.

The budgets and revenues are given by TMDB in USD without adjusting for inflation.
We will adjust the amounts for inflation and analyze everything in 2023 USD.

## What we will explore

#### Movie budget and revenue:
- What budget, revenue, profit and ROI (Return on Investment) do the movies from TMDB have?
- How many movies make a profit or breakeven, and how many movies make a loss?

#### Movie budget and vote_average:
- Is there a correlation between budget and vote_average?

#### Predicting vote_average:
- Can we make a classification machine learning model that predicts vote_average from budget, runtime and genres?


#### Lead actor age and gender:
- What age and gender do other companies cast as lead actor in their movies? 
- We have an hypothesis that female actors are more succesful under the age of 40, while male actors are more succesful after the age of 40.
- This is relevant for our fictional movie production company because we can advise them of trends in the industry.

#### Sentiment of movie overview:




## Please read our notebooks in this order
- **read_tmdb_data.ipynb:** Here we read JSON data from TMDB's API and store it as `movies.csv` and `persons.csv`.
- **inflation.ipynb:** Here we explain how we adjust for inflation.
- **preparation.ipynb**: Here we read in `movies.csv` and `persons.csv` and prepare the data by doing some cleaning and adjusting budget and revenue for inflation. The prepared data is saved as `movies_prepared.csv` and `persons_prepared.csv`.
- **movie_budget_and_revenue.ipynb:**
- **movie_budget_and_vote_average.ipynb:**
- **predicting_movie_rating.ipynb:**
- **lead_actor_age_and_gender:** 
- **sentiment_of_movie_overview:**


## Conclusions

#### Movie budget and revenue:

- We found that a lot of movies don't have budget and revenue information. Only 4042 movies had this information.
- For these movies we calculated profit and ROI.
- We found out that 61% of movies made a profit or breakeven, and 39% of movies made a loss.
- However, we discovered a trend of big budget movies being released to streaming after a very limited theatrical run. This means that we can not rely on revenue to be a reliable predictor of a movies success.

#### Movie budget and vote_average:
- Since we cannot rely on revenue to be a reliable predictor of a movies success, we instead looked at vote_average.
- For the 6200 movies that have budget information we looked at the relationship between budget and vote_average.
- We found a weak (R=0.3291) linear relationship: **_vote_average = 0.000000006579 × budget + 5.60_**

#### Predicting vote_average:
- We took all the 6200 movies that have budget information and made a classification machine learning model for predicting vote_average from budget, runtime and genres.
- In order to do this we introduced the categorial value rating, which maps ranges of vote_average to the categories "good", "ok", "bad"
- The machine learning model we trained had an accuracy of 0.71.

#### Lead actor age and gender:
- We found that female actors show a clear decline in leading roles after the age of 40. Of all the females leading roles, 77,68% were held by actresses under the age of 40 while only 22,33% was above the age of 40
- Male actors didn't follow this trend and achieved roughly the same amount of success before (51,60%) and after (48,40%) 40.


#### Sentiment of movie overview:
- While the sentiment analysis pipeline does provide a sentiment score for each movie based on its overview, the available overviews are unfortunately quite short, limiting the accuracy of the sentiment results.