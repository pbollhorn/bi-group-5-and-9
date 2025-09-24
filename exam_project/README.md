# BI Exam Project: Machine Learning for a Fictional Movie Streaming Company

Group members:
- Peter Bollhorn
- Tobias Thormod Birk Nielsen

In our exam project we will work with MovieStream, which is a fictional company that runs an online movie streaming platform.

MovieStream streams both its own movies as well as external movies (similar to Netflix, Amazon Prime Video and HBO Max).

We will address two challenges:
- Movie Recommendations: Which movies should MovieStream recommend to the users of its platform?
- Movie Profit: Which new movies should MovieStream produce in order to make the highest profit?


## Movie Recommendations
It is normal for streaming platforms to show personalized movie recommendations to their users, because they want to keep their users engaged by suggesting them movies they're likely to enjoy. These personalized recommendations can be generated using various methods:

| Method                                    | Explanation                                                                                                                                                                           |
|:------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Content-Based Filtering (CBF)             | Recommends movies to you by looking at the attributes of the movies you have already enjoyed (e.g., genre, actors, director) and suggest other movies with similar characteristics.   |
| Collaborative Filtering (CF)              | User-Based CF:<br>Recommends movies to you by looking at users who have enjoyed the same movies as you, and then suggest you other movies they have enjoyed.<br><br>Item-Based CF:<br>Recommends movies to you by looking at the "similarity" between movies. If two movies are often liked by the same users they are considered "similar". If you have enjoyed one of these movies, you are likely to get the other one recommended.                               |
| Matrix Factorization                      | (A more advanced method which will not be explained here.)                                                                                                                             |
| Deep Learning-Based Recommendations       | (A more advanced method which will not be explained here.)                                                                                                                             |
| Hybrid Systems                            | Combinations of two or more of the above methods.                                                                                                                                      |

How much a user enjoys a movie can be assessed explicitly or implicitly:
- Explicitly: E.g. a rating from 0–10 or thumbs up/thumbs down.
- Implicitly: E.g. watch time / number of times watched.

We will build a movie recommendation system for MovieStream using Content-Based Filtering and/or Collaborative Filtering. For rating system we will use a 5-star scale, with half-star increments (0.5 stars - 5.0 stars).

The categories of users that will benefit from our movie recommendation system and why:
- The end users of MovieStream - They will be suggested movies they are likely to enjoy, so when they sit down to watch a movie they will be entertained rather than bored.
- MovieStream as a company - If users tend to be entertained when they use MovieStream they are more likely to keep their subscription, and to recommend MovieStream to others.

## Movie Profit

When a new movie is planned, it is normal for the producers of the movie to hope to make a profit:

**_Profit (USD) = Revenue (USD) – Budget (USD)_**

We will use TMDB Data from the recent years: Perhaps 5 years, 15 years or 25 years.

We will work with American Movies with Revenue, Budget and Profit in USD.

We will adjust the amounts for inflation and analyze everything in 2025 US-Dollars.
