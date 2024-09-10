import streamlit as st
import pandas as pd
from pathlib import Path
import plotly.express as px


def read_data():
    data_path = Path(__file__).parents[2] / "data"
    df = pd.read_csv(data_path / "OECD_PISA_data.csv", index_col=0)
    return df


def layout():
    df = read_data()

    st.markdown("# PISA results Dashboard")
    st.markdown("## Raw data")
    st.dataframe(df)

    st.markdown("## Multiselect")
    selected_cols = st.multiselect('Select columns to display', df.columns.to_list(), default=df.columns.to_list())
    st.dataframe(df[selected_cols])
    x = st.selectbox('Choose columns', df.columns)
    fig = px.line(data_frame=df, x=df.index, y=df[x])

    st.plotly_chart(fig)


    st.markdown("## Locations")
    pisa_locations = df['LOCATION']

    fig = px.bar(data_frame=pisa_locations)
    st.plotly_chart(fig)

if __name__ == "__main__":
    layout()

# - basic statistics of the data (number of records, number of locations, subjects, and time periods)
# - show a table with sample data
# - bar chart showing average PISA scores by location
# - plot trends that can be filtered for each country 
  
# Bonus:
# - more interactive filtering to drill down to specific locations, time period, subjects, ... 
# - this filtering should be displayed on a side panel
