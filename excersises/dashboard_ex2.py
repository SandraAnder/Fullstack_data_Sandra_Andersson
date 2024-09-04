import streamlit as st
import pandas as pd
from pathlib import Path
import plotly.express as px


def read_data():
    data_path = Path(__file__).parents[1] / 'data'
    df = pd.read_csv(data_path / 'cleaned_supahcoolsoft.csv',
                     index_col=0)
    return df


def layout():
    df = read_data()

    st.markdown('# Excecutive Dashboard')

    st.markdown('## Raw data')
    st.dataframe(df)

    x = st.selectbox('Choose Columns', df.columns)

    fig = px.line(data_frame=df, x=df.index, y=df[x])
    st.plotly_chart(fig)

##############################################################
    employee_stats = df.describe()
    cols = st.columns(3)
    stats = ()
    labels = ()

    for col, stat, label in zip(cols, stats, labels):
        with col:
            st.metric(label=label, value=f'{employee_stats[stat]:.0f}')

    fig1 = px.line(data_frame=df, x=df.index,
                   y=df, title=f'Started educations in {employee_stats} 2007-2023', labels={'index': 'year', employee_stats: 'started educations'})


##############################################################
    count_emp__stat = len(df.index)
    st.markdown('## Average number of employees')
    st.markdown(f'Antal anställda: {count_emp__stat}')

    avg_age_stat = df['Age'].mean()
    st.markdown('## Average age of employees')
    st.markdown(f'Medelålder av anställda: {avg_age_stat:.2f}')

    avg_salary_stat = df['Salary_SEK'].mean()
    st.markdown('## Average salary of employees')
    st.markdown(f'Medellönen för anställda: {avg_salary_stat:.2f}')

    employee_count = df.groupby(
        'Department').size().reset_index(name='Employee count')

    st.markdown('# Number of employees across departments')  # Barchart
    fig = px.bar(data_frame=employee_count,
                 x='Department', y='Employee count')
    st.plotly_chart(fig)


if __name__ == '__main__':
    layout()

# - basic statistics on employees (total count, average age, average salary)
# - show a table with employee details
# - bar chart showing number of employees accross departments
# - histogram of salary distribution
# - box plot of salaries by department
# - histogram of age distribution
# - box plot of ages by department

# Style the dashboard to make it more exclusive for executives.
