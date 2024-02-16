import numpy as np
import pandas as pd
import streamlit as st 
import sklearn
from sklearn import preprocessing
import pickle
from pycaret.classification import load_model

def main(): 
    # Load the saved model from the pickle file generated by the Jupyter notebook
    pickled_model = load_model('modelEmployer001')
    # Website title
    st.title("Check your Employee Retention")
    # Basic website styling
    html_temp = """
    <div style="background:#025246 ;padding:10px">
    <h2 style="color:white;text-align:center;">Employee Retention Predictor</h2>
    </div>
    """
    # Add styling to webpage
    st.markdown(html_temp, unsafe_allow_html = True)
    
    # ----------------------------------------------------------------------------------------------
    # Declaring the fields for the input form on the web application
    # ----------------------------------------------------------------------------------------------

    # Accepting input for the name field
    name = st.text_input("Name","") 
    # Dropdown input for the employee's department
    department = st.selectbox("Department", ["Technical", "Sales", "Support", "HR", "IT", "Accounting", "Management", "Marketing", "Product Management", "Research and Development"])
    # Slider input for the employee's satisfaction level
    satisfaction_level = st.slider("Satisfaction Level", min_value=0.00, max_value=1.00, step=0.01)
    # Slider input for the employee's last evaluation score
    last_evaluation = st.slider("Last Evaluation Score", min_value=0.00, max_value=1.00, step=0.01)
    # Text input that takes the employee's weekly hours and calculates their average monthly hours
    average_montly_hours = (4.3)*(st.number_input("How many hours does the employee work per week?"))
    # Text input for the number of years that the employee has been with the company
    time_spend_company = st.number_input("How many years has the employee been with the company?")
    # Dropdown input for the employee's salary range
    salary = st.selectbox("Enter the employee's salary range", ["High", "Medium", "Low"])
    
    # Button to submit form results and produce prediction
    if st.button("Check departure status!"): 
        # Dictionary that holds the features from the form that we want to pass to the model
        # data = {'satisfaction_level': satisfaction_level, 'last_evaluation': last_evaluation, 'average_montly_hours': average_montly_hours, 'time_spend_company': time_spend_company, 'department': department, 'salary': salary}
        
        # List with the columns titles that are in the model's dataframe
        # category_col =['satisfaction_level', 'last_evaluation', 'average_montly_hours','time_spend_company', 'department', 'salary']
        # Convert the dictionary data to a pandas dataframe
        # df=pd.DataFrame([list(data.values())], columns=category_col)
            
        # Create a DataFrame with the new data in the same format as the training data
        new_data = pd.DataFrame([[satisfaction_level, last_evaluation, average_montly_hours, time_spend_company, department, salary]], columns=['satisfaction_level', 'last_evaluation', 'average_montly_hours','time_spend_company', 'department', 'salary'])
        
        # Run the form data in the model and predict if the employee will leave or stay
        prediction = pickled_model.predict(new_data) 

        if (prediction == 1):
          text = "Leave"
        else:
          text = "Stay"
        
        # Display the prediction on the web app screen
        st.success('Employee departure status: {}'.format(text))
      
if __name__=='__main__': 
    main()
