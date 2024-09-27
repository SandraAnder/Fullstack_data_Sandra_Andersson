import streamlit as st
from utils.query_database import QueryDatabase

class ContentKPI:
    def __init__(self) -> None:
        self._content_view = QueryDatabase("SELECT * FROM marts.content_view_time;").df

    def display_content(self):
        content_df = self._content_view

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
        # st.dataframe(gender_df)
        # st.dataframe(age_df)

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


class Viewer_geog:
    def __init__(self) -> None:
        geog_df = self._content_geog = QueryDatabase("SELECT * FROM marts.content_viewer_geografy").df

    def display_viewer_geog(self):
        geog_df = self._content_geog
        st.markdown("## Mest tittade videor")

        kpis = {
            "Geografi": geog_df["Geografi"],
        }

        for col, kpi in zip(st.columns(len(kpis)), kpis):
                with col: 
                    st.write(kpi, round(kpis[kpi]))


        # top_countries = self.geog_df.sort_values(by="Totala_visningar", ascending=False).head(3)
        
        # st.markdown("### Topp 3 länder baserat på visningar")
        # # Presentera varje land som en KPI i en rad
        # for index, row in top_countries.iterrows():
        #     st.metric(label=f"{row['Geografi']}", value=f"{row['Totala_visningar']} visningar")
        

class Op_system_views:
    def __init__(self) -> None:
        op_sys_df = self._op_sys = QueryDatabase("SELECT * FROM marts.op_system_views").df

    def display_op_sys(self):
        op_sys_df = self._op_sys
        st.markdown("## Vilka operativsystem är vanligast")

        kpis = {
            "Operativsystem": op_sys_df["Operativsystem"],
            "Visningar": op_sys_df["Totala_visningar"]
        }

        for col, kpi in zip(st.columns(len(kpis)), kpis):
                with col: 
                    st.write(kpi, kpis[kpi])
              


class Subs:
    def __init__(self) -> None:
        subs_df = self._subs = QueryDatabase("SELECT * FROM marts.subscribers").df

    def display_subs(self):
        subs_df = self._subs
        st.markdown("## Prenumeranter")

        # Loopar genom prenumerationskällorna och visar information för varje rad
        for index, row in subs_df.iterrows():
            st.markdown(f"### {row['Prenumerationskälla']}")  # Visa prenumerationskällans namn som en rubrik
            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric("Totala prenumeranter", row["Totala_prenumeranter"])
            with col2:
                st.metric("Nya prenumeranter", row["Totala_nya_prenumeranter"])
            with col3:
                st.metric("Förlorade prenumeranter", row["Totala_förlorade_prenumeranter"])


class Subs_source:
    def __init__(self) -> None:
        subs_source_df = self._subs_source = QueryDatabase("SELECT * FROM marts.subs_source").df

    def display_subs_source(self):
        subs_source_df = self._subs_source
        st.markdown("## Prenumerant källa")

        kpis = {
            "Prenumerationskälla": subs_source_df["Prenumerationskälla"],
            "Prenumeranter": subs_source_df["Prenumeranter"]
        }

        for col, kpi in zip(st.columns(len(kpis)), kpis):
                with col: 
                    st.write(kpi, kpis[kpi])


class Most_recent_10:
    def __init__(self) -> None:
        recent_10_df = self._recent_10 = QueryDatabase("SELECT * FROM marts.content_10_latest_vid").df

    def display_recent_10(self):
        recent_10_df = self._recent_10
        st.markdown("## 10 senaste videorna")

        kpis = {
            "Videotitel": recent_10_df["Videotitel"],
            "Publiceringstid för video": recent_10_df["Publiceringstid för video"],
            "Visningar": recent_10_df["totala_visningar"],
            "Visningstid (timmar)": recent_10_df["Visningstid (timmar)"],
            "Prenumeranter": recent_10_df["Prenumeranter"]
        }

        for col, kpi in zip(st.columns(len(kpis)), kpis):
                with col: 
                    st.write(kpi, round(kpis[kpi]))


# create more KPIs here
class DeviceKPI:
    pass 
