import streamlit as st
from utils.query_database import QueryDatabase

class ContentKPI:
    def __init__(self) -> None:
        self._content_view = QueryDatabase("SELECT * FROM marts.content_view_time;").df

    def display_content(self):
        content_df = self._content_view
        st.markdown("## KPIer för videor")
        st.markdown("Nedan visas KPIer för totalt antal")

        kpis = {
            "videor": len(content_df),
            "visade timmar": content_df["Visningstid_timmar"].sum(),
            "prenumeranter": content_df["Prenumeranter"].sum(),
            "exponeringar": content_df["Exponeringar"].sum()
        }

        for col, kpi in zip(st.columns(len(kpis)), kpis):
            with col: 
                st.metric(kpi, round(kpis[kpi]))
        #st.dataframe(df)


class AgeGenderKPI:
    def __init__(self) -> None:
        self._gender_content = QueryDatabase("SELECT * FROM marts.content_gender_viewers").df
        self._age_content = QueryDatabase("SELECT * FROM marts.content_age_viewers").df

    def display_gender_age(self):
        gender_df = self._gender_content
        age_df = self._age_content

        st.markdown("## Data per tittare")
        st.markdown("Nedan visas KPIer för kön och ålder")
        #st.dataframe(gender_df)
        #st.dataframe(age_df)

        gender_kpis = {
            "Tittarnas ålder": gender_df["Kön"],
            "Genomsnittlig visningslängd": gender_df["Genomsnittlig visningslängd"],
            "Genomsnittlig procent som har visats": gender_df["Genomsnittlig_%_visat"],
        }

        age_kpis = {
            "Tittarnas kön": age_df["Ålder"],
            "Genomsnittlig visningslängd": age_df["Genomsnittlig visningslängd"],
            "Genomsnittlig procent som har visats": age_df["Genomsnittlig_%_visat"],
        }

        st.markdown("### KPI:er för ålder")


        selected_gender = st.selectbox("Välj en ålderskategori:", gender_df["Kön"].unique())

        # Filtrera datan baserat på användarens val
        filtered_gender_df = gender_df[gender_df["Kön"] == selected_gender]

        # Visa data för den valda ålderskategorin
        if not filtered_gender_df.empty:
            st.markdown(f"### Data för ålderskategori: {selected_gender}")
            st.write(f"- Genomsnittlig visningslängd: {filtered_gender_df['Genomsnittlig visningslängd'].values[0]}")
            st.write(f"- Genomsnittlig procent som har visats: {filtered_gender_df['Genomsnittlig_%_visat'].values[0]}")

        # Låter användaren välja en viss könskategori från selectbox
        st.markdown("### KPI:er för kön")
        selected_age = st.selectbox("Välj en könskategori:", age_df["Ålder"].unique())

        # Filtrera datan baserat på användarens val
        filtered_age_df = age_df[age_df["Ålder"] == selected_age]

        # Visa data för den valda könskategorin
        if not filtered_age_df.empty:
            st.markdown(f"### Data för kön: {selected_age}")
            st.write(f"- Genomsnittlig visningslängd: {filtered_age_df['Genomsnittlig visningslängd'].values[0]}")
            st.write(f"- Genomsnittlig procent som har visats: {filtered_age_df['Genomsnittlig_%_visat'].values[0]}")




        # for col, kpi in zip(st.columns(len(gender_kpis)), gender_kpis):
        #     with col:
        #         value = round(gender_kpis[kpi], 2)
        #         st.write(f"**{kpi}:** {value}")

        # st.markdown("### KPIer för ålder")
        # for col, kpi in zip(st.columns(len(age_kpis)), age_kpis):
        #     with col:
        #         value = round(age_kpis[kpi], 2)
        #         st.write(f"**{kpi}:** {value}")

class Top15KPI:
    def __init__(self) -> None:
        top_15_df = self._content_top15 = QueryDatabase("SELECT * FROM marts.content_top_15_viewed").df

    def display_top_videos(self):
        top_15_df = self._content_top15
        st.markdown("## Mest tittade videor")

        kpis = {
            "Videotitel": top_15_df["Titel"],
            "Visningar": top_15_df["Antal_visningar"],
        }

        for col, kpi in zip(st.columns(len(kpis)), kpis):
                with col: 
                    st.write(kpi, round(kpis[kpi]))




# create more KPIs here
class DeviceKPI:
    pass 
