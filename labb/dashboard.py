import streamlit as st 
from pathlib import Path
from frontend.kpi import ContentKPI, AgeGenderKPI, Top15KPI, Viewer_geog, Op_system_views, Subs, Subs_source, Most_recent_10
from frontend.graphs import ViewsTrend
from backend.constants import Color
import altair as alt


content_kpi = ContentKPI()
views_graph = ViewsTrend()
age_kpi = AgeGenderKPI()
top_15 = Top15KPI()
top_15_plot = ViewsTrend()
viewer_geog = Viewer_geog()
op_system = Op_system_views()
subs = Subs()
subs_source = Subs_source()
recent_10 = Most_recent_10()

def layout():
    # st.set_page_config(
    # page_title="The data driven youtuber",
    # page_icon="🏂",
    # layout="wide",
    # initial_sidebar_state="expanded")

    # alt.themes.enable("dark")


    st.markdown("# The data driven youtuber")
    st.markdown("Den här dashboarden syftar till att utforska datan i min youtubekanal")

    # Skapa en meny i sidofältet
    st.sidebar.title("Huvudmeny")
    page = st.sidebar.radio("Välj en sida", ("Översikt", "Tittare", "Videor", "Tekniskt"))

    # Sida 1
    if page == "Översikt":
        st.header("KPIer för videor")
        st.markdown("Nedan visas sammanfattning för totala antal")

        content_kpi.display_content()
        views_graph.display_plot()
    # sida 2
    elif page == "Tittare":
        st.header("Antal visningar under senaste månaden")
        age_kpi.display_gender_age()
        viewer_geog.display_viewer_geog()
        #geog_plot.geo_plot()
        subs.display_subs()

    # sida 3
    elif page == "Videor":
        st.header("Topp 15 mest tittade videor")
        top_15.display_top_videos()
        top_15_plot.top_15_plot()
        recent_10.display_recent_10()

    # sida 4
    elif page == "Tekniskt":
        st.header("Vanligaste op systemen")
        op_system.display_op_sys()
        subs_source.display_subs_source()


    read_css()


def read_css():
    css_path = Path(__file__).parent / 'style.css'

    with open(css_path) as css:
        st.markdown(
            f'<style>{css.read()}</style>', unsafe_allow_html=True
        )

if __name__ == "__main__":
    layout()