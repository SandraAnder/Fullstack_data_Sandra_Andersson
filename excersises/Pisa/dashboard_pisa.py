import streamlit as st
import pandas as pd
from pathlib import Path
import plotly.express as px


def read_data():
    data_path = Path(__file__).parents[2] / 'data'
    df = pd.read_csv(data_path / 'OECD_Pisa_data.csv', index_col=0, parse_dates=[0])
    return df

def layout():
    df = read_data()

    st.write('# PISA records')

    st.write('## Number records')
    st.write(f'- Antal poster: {df.shape[0]}')
    st.write(f'- Antal platser: {df["LOCATION"].unique().shape[0]}')

    subject = ', '.join(df["SUBJECT"].unique())
    st.write(f'- Subjekt: {subject}')

    st.write(f'- Tidsperiod: {df["TIME"].min()} - {df["TIME"].max()}')

    st.markdown('## Sample data')
    st.markdown('- 10 first data samples')
    st.dataframe(df.head(10))

    st.markdown('## PISA scores by location')
    tot_subject = df[df['SUBJECT'] == 'TOT']
    avg_tot = tot_subject.groupby('LOCATION')['Value'].mean().sort_values()
    st.bar_chart(avg_tot)

    st.markdown('## Trends for each country')
    st.selectbox


if __name__ == "__main__":
    layout()


## - basic statistics of the data (number of records, number of locations, subjects, and time periods)
## - show a table with sample data
## - bar chart showing average PISA scores by location
# - plot trends that can be filtered for each country 
  
# Bonus:
# - more interactive filtering to drill down to specific locations, time period, subjects, ... 
# - this filtering should be displayed on a side panel




















# def read_data():
#     data_path = Path(__file__).parents[2] / "data"
#     df = pd.read_csv(data_path / "OECD_PISA_data.csv", index_col=0)
#     return df


# def layout():
#     df = read_data()

#     st.markdown("# PISA results Dashboard")
#     st.markdown("## Raw data")
#     st.dataframe(df)

#     st.markdown("## Multiselect")
#     selected_cols = st.multiselect('Select columns to display', df.columns.to_list(), default=df.columns.to_list())
#     st.dataframe(df[selected_cols])
#     x = st.selectbox('Choose columns', df.columns)
#     fig = px.line(data_frame=df, x=df.index, y=df[x])

#     st.plotly_chart(fig)


#     st.markdown("## Locations")
#     pisa_locations = df['LOCATION']

#     fig = px.bar(data_frame=pisa_locations)
#     st.plotly_chart(fig)

# if __name__ == "__main__":
#     layout()