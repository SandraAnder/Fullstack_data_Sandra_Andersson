from utils.query_database import QueryDatabase
import plotly.express as px
import streamlit as st
import pycountry
from backend.constants import Color


class ViewsTrend:
    def __init__(self) -> None:
        self.df = QueryDatabase("SELECT * FROM marts.views_per_date").df
        self.age_df = QueryDatabase(
            "SELECT * FROM marts.content_age_viewers").df
        self.gender_content = QueryDatabase(
            "SELECT * FROM marts.content_gender_viewers").df
        self.content_top15 = QueryDatabase(
            "SELECT * FROM marts.content_top_15_viewed").df
        self.content_geog = QueryDatabase(
            "SELECT * FROM marts.content_viewer_geografy").df
        self._recent_10 = QueryDatabase(
            "SELECT * FROM marts.content_10_latest_vid").df
        self._op_sys = QueryDatabase("SELECT * FROM marts.op_system_views").df
        self._content_geog = QueryDatabase(
            "SELECT * FROM marts.content_viewer_geografy").df

        print(self.df)

    def display_plot(self):
        fig = px.line(self.df, x="Datum", y="Visningar")
        st.markdown("## Antal visningar under senaste månaden")
        # st.plotly_chart(fig)

        fig.update_layout(
            plot_bgcolor='rgba(0, 0, 0, 0)',
            paper_bgcolor='rgba(0, 0, 0, 0)',
        )

        fig.update_traces(
            line=dict(
                width=2,
                color=Color.GRAPH))

        st.plotly_chart(fig, use_container_width=True)

    def top_15_plot(self):
        self.content_top15 = self.content_top15.sort_values(
            by='Antal_visningar', ascending=False)

        st.markdown("### Topp 15 mest tittade videor")
        fig = px.bar(
            self.content_top15.iloc[1:].head(15),
            y='Titel',
            x='Antal_visningar',
            # title='Top 15 mest tittade videor',
            labels={'Antal_visningar': 'Visningar', 'Titel': 'Videotitel'},
            color='Antal_visningar',  # Färg baserat på visningsantal
            color_discrete_sequence=px.colors.qualitative.Plotly,  # Färgpalett för staplarna
            height=600,  # Höjd på grafen
            orientation='h',  # Gör stapeldiagrammet liggande,
            range_color=[0, 120]  # Sätter intervall för färgskalan till 0-120
        )
        # Anpassa layouten på grafen
        fig.update_layout(
            xaxis_title="Antal visningar",
            yaxis_title="Videotitel",
            xaxis_tickangle=0,  # Rotera x-ticks för bättre läsbarhet
            # Omvänd y-axel för att få den mest tittade videon högst upp
            yaxis=dict(autorange="reversed"),
            # Ändra bakgrundsfärg för diagrammet till vit
            plot_bgcolor='rgba(0, 0, 0, 0)',
            paper_bgcolor='rgba(0, 0, 0, 0)'  # Transparent bakgrund
        )
        # Begränsar x-axelns maxvärde
        fig.update_xaxes(range=[0, 120])

        st.plotly_chart(fig)

    def recent_10_plot(self):
        self.recent_10 = self._recent_10
        st.markdown("## 10 senaste videorna")
        fig = px.bar(
            self.recent_10,
            x="totala_visningar",
            y="Videotitel",
            orientation='h',
            # labels={"totala_visningar": "Totala Visningar", "Videotitel": "Titel"}
            labels={"totala_visningar": "", "Videotitel": ""},
            title="Totala visningar av de 10 senast uppladdade videorna",
            color="totala_visningar",
            color_continuous_scale=px.colors.sequential.Peach
        )

        fig.update_layout(
            yaxis=dict(autorange="reversed"),  # Inverterar ordningen
            plot_bgcolor='rgba(0, 0, 0, 0)',  # Ändrar bakgrundsfärg
            paper_bgcolor='rgba(0, 0, 0, 0)')

        st.plotly_chart(fig, use_container_width=True)

    def op_sys_plot(self):
        # Tar bort sista raden och sorterar DataFramen efter antalet visningar i fallande ordning
        op_sys_df = self._op_sys[:-1].sort_values(
            by="Totala_visningar", ascending=True).reset_index(drop=True)

        # st.markdown("## Vilka operativsystem är vanligast")

        fig = px.bar(
            op_sys_df,
            x='Totala_visningar',
            y='Operativsystem',
            orientation='h',
            color='Totala_visningar',
            color_continuous_scale='Peach',
            title='Vanligaste operativsystemet baserat på totala visningar',
            labels={'Totala_visningar': 'Antal visningar',
                    'Operativsystem': 'Operativsystem'},
            height=600
        )

        fig.update_layout(
            xaxis_title="",
            yaxis_title="",
            plot_bgcolor='rgba(0, 0, 0, 0)',
            paper_bgcolor='rgba(0, 0, 0, 0)',
        )

        st.plotly_chart(fig, use_container_width=True)

    def geog_map_plot(self):
        geog_df = self._content_geog

        def convert_to_iso3(iso2):
            try:
                return pycountry.countries.get(alpha_2=iso2).alpha_3
            except AttributeError:
                return None

        geog_df['Geografi_ISO3'] = geog_df['Geografi'].apply(convert_to_iso3)

        # Filter out rows where conversion failed
        geog_df = geog_df.dropna(subset=['Geografi_ISO3'])

        # choropleth ger oss vår vackra karta
        fig = px.choropleth(
            geog_df,
            # Kolumnen med länderkoder (t.ex. "SE", "IN", "MT") är nu omgjort till 3 SWE, IND, MLT för att coropleth kartan inte kan ta ISO-2
            locations="Geografi_ISO3",
            locationmode="ISO-3",  # Pekar på att Geografi innehåller landkoder
            color="Visningar",  # Kolumnen som används för att färgsätta kartan
            hover_name="Geografi",  # Landet visas när pilen är över landet
            color_continuous_scale=px.colors.sequential.Plasma,  # Färgskalan
            title="Visningar per land",
            labels={'Visningar': 'Totala Visningar'}
        )

        # Anpassar layouten för kartan
        fig.update_layout(
            title={
                'text': "Visningar per land",
                'x': 0.5,  # 0 is left, 1 is right
                'xanchor': 'center',  # Anchors the title in the center
                'yanchor': 'top'  # Positioning from top
            },

            geo=dict(
                showframe=False,
                showcountries=True,
                projection_type="equirectangular",
                resolution=50,
                showcoastlines=True,
                coastlinecolor="gray",
                countrycolor="black",
                center=dict(lat=45, lon=25),
                lataxis_range=[20, 60],
                lonaxis_range=[-20, 40]
            ),
            margin={"r": 0, "t": 40, "l": 0, "b": 0},
            height=500,  # Justera höjden på kartan
            # Transparent bakgrund för själva plotområdet
            plot_bgcolor='rgba(0, 0, 0, 0)',
            paper_bgcolor='rgba(0, 0, 0, 0)',
            coloraxis_colorbar=dict(
                title="Totala Visningar",
                x=0.85,  # Adjust this value to move the colorbar closer to the map
                xanchor='left')

        )

        st.plotly_chart(fig, use_container_width=True)
