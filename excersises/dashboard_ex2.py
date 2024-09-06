import streamlit as st
import pandas as pd
from pathlib import Path
import plotly.express as px


def read_data():
    data_path = Path(__file__).parents[1] / "data"
    df = pd.read_csv(data_path / "cleaned_supahcoolsoft.csv", index_col=0)
    return df


def layout():
    df = read_data()

    st.markdown("# Excecutive Dashboard")
    st.markdown("## Raw data")
    st.dataframe(df)

##############################################################

    # Beräkna statistik
    count_emp_stat = len(df.index)  # Antal anställda
    avg_age_stat = df["Age"].mean()  # Medelålder
    avg_salary_stat = df["Salary_SEK"].mean()  # Medellön

    labels = [
        "### Antal anställda",
        "### Medelålder av anställda",
        "### Medellön av anställda",
    ]
    formatted_stats = [
        f"{count_emp_stat}",
        f"{avg_age_stat:.2f}",
        f"{avg_salary_stat:.2f} SEK",
    ]

    cols = st.columns(3)
    # Loopar över kolumner och mätvärden
    for col, label, stat in zip(cols, labels, formatted_stats):
        with col:
            st.markdown(label)
            st.markdown(stat)


##############################################################

    # Låt användaren välja vilka kolumner de vill visa
    selected_columns = st.multiselect("Choose Columns to Display", df.columns.tolist(), default=df.columns.tolist())

    # Visa tabellen med valda kolumner
    st.dataframe(df[selected_columns])
    x = st.selectbox("Choose Columns", df.columns)

    fig = px.line(data_frame=df, x=df.index, y=df[x])
    st.plotly_chart(fig)

###########################

    employee_count = df.groupby("Department").size().reset_index(name="Employee count")

    st.markdown("## Number of employees across departments")  # Barchart
    fig = px.bar(data_frame=employee_count, x="Department", y="Employee count")
    st.plotly_chart(fig)

###########################

    st.markdown("## Salary Distribution")
    fig = px.histogram(
        df,
        x="Salary_SEK",
        nbins=30,
        labels={"Salary_SEK": "Salary_SEK"},
    )
    fig.update_traces(marker_line_width=1.5, marker_line_color='darkblue')

    st.plotly_chart(fig)

###########################

    salary_by_dep = df["Department"]

    for salary in salary_by_dep:
        print(salary)
    st.markdown("## Salary Distribution by Department")
    fig=px.box(data_frame=df, x="Department", y="Salary_SEK")

    st.plotly_chart(fig)

###########################

    st.markdown("## Age Distribution")
    fig = px.histogram(
        df,
        x="Age",
        nbins=30,
        labels={"Age": "Age"},
    )
    fig.update_traces(marker_line_width=1.5, marker_line_color='darkblue')
    
    st.plotly_chart(fig)

###########################

    age_by_dep = df["Age"]

    for age in age_by_dep:
        print(age)
    
    st.markdown("## Age Distribution by Department")
    fig=px.box(data_frame=df, x="Department", y="Age")

    st.plotly_chart(fig)

###########################

if __name__ == "__main__":
    layout()

    # - basic statistics on employees (total count, average age, average salary)
    # - show a table with employee details
    # - bar chart showing number of employees accross departments
    # - histogram of salary distribution
    # - box plot of salaries by department
    # - histogram of age distribution
    # - box plot of ages by department

# Style the dashboard to make it more exclusive for executives.