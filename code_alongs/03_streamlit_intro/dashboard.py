import streamlit as st
import pandas as pd
from pathlib import Path
import plotly.express as px

print('\n'*2)


def read_data():
    data_path = Path(__file__).parents[2] / 'data'
    df = pd.read_csv(data_path / 'cleaned_yh_region.csv',
                     index_col=0, parse_dates=[0])
    df.index = df.index.year
    return df


def layout():
    df = read_data()
    st.markdown('# YH dashboard')
    st.markdown('This is a simple dashboard about Yrkeshögskolan')

    st.markdown('## Raw data')
    st.markdown('Data shows started educations per region and year')
    st.dataframe(df)

    st.markdown('## Trend per region')
    region = st.selectbox('Choose region', df.columns)

    fig = px.line(data_frame=df, x=df.index, y=df[region])
    st.plotly_chart(fig)
    # st.dataframe(df[region])


# __name__ is a special variable which is equal to '__main__' when we run this script
# when we import this script from elsewhere, __name__ is the scripts name
if __name__ == '__main__':
    layout()
