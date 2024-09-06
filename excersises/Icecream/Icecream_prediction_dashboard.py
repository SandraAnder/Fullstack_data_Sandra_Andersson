import streamlit as st
import pandas as pd
from pathlib import Path
import plotly.express as px
import joblib

# Create a simple app in streamlit that lets the user enter a temperature 
# in celsius and it outputs the revenue prediction. You can for example
# use random forest regression to predict the revenue.

def read_data():
    data_path = Path(__file__).parents[2] / 'data' 
    df = pd.read_csv(data_path / 'cleaned_Icecream.csv', index_col=0)
    return df

read_data()

def load_model():
    model_path = Path(__file__).parent / 'random_forest_revenue_model.pkl'
    if model_path.exists():
        model = joblib.load(model_path)
        return model
    else:
        st.error(f'Model file not found: {model_path}')
        return None
    
def layout():
    df = read_data()
    model = load_model()
    
    st.markdown('# Icecream predictions')
    st.markdown('## Raw data')
    st.dataframe(df)

    user_choice = st.text_input('Enter a temperature in celsius: ', placeholder='Enter your number')
    
    if user_choice:
        try:
            user_choice = float(user_choice)
            st.write(f'You entered {user_choice:.1f} degrees celsius')

            revenue_prediction = model.predict([[user_choice]])
            st.write(f'Predicted revenue: {revenue_prediction[0]:.2f} SEK')
        except ValueError:
            st.write('Please enter a valid number')
    else:
        st.write('Please enter a number.')


if __name__ == "__main__":
    layout()
