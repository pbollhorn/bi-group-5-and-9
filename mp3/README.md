# Answers to questions

**Question:** Is there a linear relationship between actor age and their movie count (number of movies they have appeared in)?

**Answer:** We made a linear regression and found a R² value of 0.029. So we did not really find a linear relationship. However, we expect, that if we only looked at the actors with the top 100 movie counts, we would get a better linear relationship.

<br>

**Question 6:** Which machine learning methods did you choose to apply in the application and why?

**Answer:** For the classification we chose to make of both decision tree and random forest models. The two models performed very similarly, within <1% of each other. 
For clustering we choose the Mean Shift model, becuase of it's automatically dection of clusters. 

<br>

**Question 7:** How accurate are your solutions of prediction? Explain the meaning of the quality measures.

**Answer:** The classification prediction ended being poor, ~58-59%.

<br>

**Question 8:** What could be done for further improvement of the accuracy of the models?

**Answer:** The data of danish actors was somewhat limited, with much data too incomplete to use. As a result we were only able to train the model with age and amount of movies. If additional features had been availible the precition accuracy would likely have improved.

<br>

**Question 9:** Which were the challenges in the project development?

**Answer:** A big challenge was that it took us a long time to retrieve data from TMDB and clean it. After we had done that, we did not have much time left to analyze the data, i.e. to perform task 2, 3 and 4.
