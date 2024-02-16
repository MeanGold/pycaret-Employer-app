# pycaret-Employer-app
This project takes a PyCaret model that will try to predict employee retention for an employer. It saves the model and then loads it into a Streamlit web app for deployment.

You can load this Streamlit web app by going to the following link in your web browser...
https://pycaret-employer-app-2mpsnjmwthuuwg2upjv9lx.streamlit.app/

Observations on the model and the input data...
- The model tends to lean toward "Stay" as a prediction, and this is probably due to the fact that only a little more than one-fifth of the training data had "Leave" as a result
- There was no evaluation score below 0.35, so running the model with a score lower than that may result in worse output
- Average monthly hours was calculated by taking the weekly hours and multiplying by 4.3 since there are about 4.3 weeks in each month
  - The monthly hours ranged from 96 to 310, which equates to an equivalent weekly hour range from 22 to 72. Inputting values outside of this range may result in worse output
- For the salary input, I am not able to find a direct conversion from low, middle, and high to actual concrete numerical values. 
