import numpy as np
import pandas as pd
import streamlit as st 
import sklearn
from sklearn import preprocessing
import pickle
from pycaret.classification import load_model

col = ['satisfaction_level', 'last_evaluation', 'average_montly_hours', 'time_spend_company', 'department', 'salary']
  
def main(): 
    pickled_model = load_model('modelEmployer001')
    st.title("Check your Employee Retention")
    html_temp = """
    <div style="background:#025246 ;padding:10px">
    <h2 style="color:white;text-align:center;">Employee Retention Predictor</h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html = True)
    
    name = st.text_input("Name","Employee's name") 
    department = st.selectbox("Department", ["Technical", "Sales", "Support", "HR", "IT", "Accounting", "Management", "Marketing", "Product Management", "Research and Development"])
    satisfaction_level = st.slider("Satisfaction Level", min_value=0.00, max_value=1.00, step=0.01)
    last_evaluation = st.slider("Last Evaluation Score", min_value=0.00, max_value=1.00, step=0.01)
    average_montly_hours = (4.3)*(st.number_input("How many hours does the employee work per week?"))
    time_spend_company = st.number_input("How many years has the employee been with the company?")
    salary = st.selectbox("Enter the employee's salary range", ["High", "Medium", "Low"])
    
    if st.button("Check departure status!"): 
        features = [[name, department, satisfaction_level, average_montly_hours, time_spend_company]]
        data = {'satisfaction_level': satisfaction_level, 'last_evaluation': last_evaluation, 'average_montly_hours': average_montly_hours, 'time_spend_company': time_spend_company, 'department': department, 'salary': salary}
        
        df=pd.DataFrame([list(data.values())], columns=['satisfaction_level', 'last_evaluation', 'average_montly_hours','time_spend_company', 'department', 'salary'])
        
        category_col =['satisfaction_level', 'last_evaluation', 'average_montly_hours','time_spend_company', 'department', 'salary']
            
        features_list = df.values.tolist()
        # Create a DataFrame with the new data in the same format as the training data
        new_data = pd.DataFrame([[satisfaction_level, last_evaluation, average_montly_hours, time_spend_company, department, salary]], columns=['satisfaction_level', 'last_evaluation', 'average_montly_hours','time_spend_company', 'department', 'salary'])
        
        prediction = pickled_model.predict(new_data) 

        if (prediction == 1):
          text = "Leave"
        else:
          text = "Stay"
        
        st.success('Employee departure status: {}'.format(text))
      
if __name__=='__main__': 
    main()
