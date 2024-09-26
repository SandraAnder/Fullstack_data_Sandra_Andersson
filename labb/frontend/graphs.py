from utils.query_database import QueryDatabase
import plotly.express as px
import streamlit as st 
from backend.constants import Color

class ViewsTrend:
    def __init__(self) -> None:
        self.df = QueryDatabase("SELECT * FROM marts.views_per_date").df
        self.age_df = QueryDatabase("SELECT * FROM marts.content_age_viewers").df
        self.gender_content = QueryDatabase("SELECT * FROM marts.content_gender_viewers").df
        self.content_top15 = QueryDatabase("SELECT * FROM marts.content_top_15_viewed").df
        print(self.df)

    def display_plot(self):
        fig = px.line(self.df, x="Datum", y="Visningar")
        st.markdown("## Antal visningar under senaste månaden")
        st.plotly_chart(fig)

        fig.update_traces(
        line=dict(
            width=4,
            color=Color.PRIMARY))

    #def plot_age_gender(self):

    def top_15_plot(self):
        self.content_top15 = self.content_top15.sort_values(by='Antal_visningar', ascending=False)

        fig = px.bar(
            self.content_top15,
            y='Titel',   # Videotitlar på y-axeln
            x='Antal_visningar',  # Visningsantal på x-axeln
            title='Top 15 mest tittade videor',
            labels={'Antal_visningar': 'Visningar', 'Titel': 'Videotitel'},
            color='Antal_visningar',  # Färg baserat på visningsantal
            color_discrete_sequence=px.colors.qualitative.Plotly,  # Färgpalett för staplarna
            height=600,  # Höjd på grafen
            orientation='h',  # Gör stapeldiagrammet liggande,
            range_color=[0, 120]  # Sätt intervall för färgskalan till 0-120
        )
        # Anpassa layouten på grafen
        fig.update_layout(
            xaxis_title="Antal visningar",
            yaxis_title="Videotitel",
            xaxis_tickangle=0,  # Rotera x-ticks för bättre läsbarhet
            yaxis=dict(autorange="reversed"),  # Omvänd y-axel för att få den mest tittade videon högst upp
            plot_bgcolor='white',  # Ändra bakgrundsfärg för diagrammet till vit
            paper_bgcolor='white'  # Transparent bakgrund
        )
        # Begränsa x-axelns maxvärde
        fig.update_xaxes(range=[0, 120])  # Ändra detta till lämpligt maxvärde

        # Visa diagrammet i Streamlit
        st.plotly_chart(fig)

# create more graphs here

