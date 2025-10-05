# Exam Project: Business Intelligence for a Fictional Movie Production Company

Group members:
- Peter Bollhorn
- Tobias Thormod Birk Nielsen

In our exam project we will perform Business Intelligence analysis for a fictional movie production company.
This company releases some movies in theaters and others directly to streaming platforms.



We will work with movie data from TMDB, with recent movies (2000-2023) from the United States.

We will work with budget and revenue from the theatrical release of movies, because this is relevant for movies released to cinemas.

We will also work with the rating of movies (from 1-10), because this is relevant for how well movies when released to streaming.

We will adjust the amounts for inflation and analyze everything in 2023 US-Dollars.


## Question we will explore
- What budget, revenue, profit and ROI do other movies have?
- Can we make a classification machine learning model to predict movie rating?


### Lead Actor Age and Gender
- What age and gender do other companies cast as lead actor in their movies? 
 (We have an hypothesis that female actors are more succesful under the age of 40, while male actors are more succesful after the age of 40)

(This is relevant for our fictional movie production company because we can advise them of trends in the industry.)

## Please read our notebooks in this order
- **read_tmdb_data.ipynb:** Here we read JSON data from TMDB's API and store it as `movies.csv` and `persons.csv`.
- **inflation.ipynb:** Here we explain how we adjust for inflation.
- **preparation.ipynb**: Here we read in `movies.csv` and `persons.csv` and prepare the data by doing some cleaning and adjusting budget and revenue for inflation. The prepared data is saved as `movies_prepared.csv` and `persons_prepared.csv`.
- **movie_budget_and_revenue.ipynb:**
- **predicting_movie_rating.ipynb:**
- **lead_actor_age_and_gender:**
- **sentiment_of_movie_overview:**


## Conclusions














