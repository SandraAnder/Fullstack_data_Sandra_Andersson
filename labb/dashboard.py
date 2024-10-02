import streamlit as st
from pathlib import Path
from frontend.kpi import ContentKPI, AgeGenderKPI, Viewer_geog, Op_system_views, Subs, Subs_source, Most_recent_10
from frontend.graphs import ViewsTrend
from backend.constants import Color
import altair as alt
from streamlit_elements import elements, media
from streamlit_extras.let_it_rain import rain


st.set_page_config(
    page_title="The data driven youtuber",  # Titel på browserfliken
    page_icon="🦜",  # Icon på browserfliken
    layout="wide",  # Ger en fullskärms upplevelse
    initial_sidebar_state="expanded",  # Sidebaren startar i utfällt läge
)


content_kpi = ContentKPI()
views_graph = ViewsTrend()
age_kpi = AgeGenderKPI()
top_15_plot = ViewsTrend()
viewer_geog = Viewer_geog()
viewer_geog_plot = ViewsTrend()
op_system = Op_system_views()
op_system_plot = ViewsTrend()
subs = Subs()
subs_source = Subs_source()
recent_10 = Most_recent_10()
recent_10_plot = ViewsTrend()


def layout():

    st.markdown("""
    <div class="header-container">
        <h1>The data driven youtuber 📹👑</h1>
        <p>Den här dashboarden syftar till att utforska datan i min youtubekanal</p>
    </div>
    """, unsafe_allow_html=True)

    # Skapar en meny i sidofältet till vänster
    st.sidebar.title("Meny")
    page = st.sidebar.radio(
        label="Välj sida",
        options=["Översikt", "Tittare", "Videor", "Tekniskt"])

    # Sida 1
    if page == "Översikt":
        st.markdown("## KPIer för videor")
        st.markdown("Nedan visas sammanfattning för totala antal")

        content_kpi.display_content()
        views_graph.display_plot()
    # sida 2
    elif page == "Tittare":
        st.markdown("## Tittarstatistik")
        age_kpi.display_gender_age()
        viewer_geog.display_viewer_geog()
        viewer_geog_plot.geog_map_plot()
        subs.display_subs()

    # sida 3
    elif page == "Videor":

        rain(
            emoji="🍂",
            font_size=24,
            falling_speed=5,
            animation_length="infinite",
        )
        st.header("Videostatistik")
        top_15_plot.top_15_plot()
        st.markdown("## Populäraste videon")

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("### Populäraste videon")
            with elements("media_player_1"):
                media.Player(
                    url="https://www.youtube.com/watch?v=i454nHjdMAc&ab_channel=AIgineer",
                    controls=True,
                    width="100%",  # Låt spelaren ta upp hela bredden
                    height="400px",  # höjden
                    frameborder="0"
                )

        with col2:
            st.markdown("### Senaste Videon")
            with elements("media_player_2"):
                media.Player(
                    url="https://www.youtube.com/watch?v=2vvHu06wM4g&t=763s&ab_channel=AIgineer",
                    # TESTA ÄVEN DENNA ;) - url="https://www.youtube.com/watch?v=iik25wqIuFo",
                    controls=True,
                    width="100%",
                    height="400px",
                )

        recent_10_plot.recent_10_plot()
        recent_10.display_recent_10()

    # sida 4
    elif page == "Tekniskt":
        st.header("Statistik")
        op_system.display_op_sys()
        op_system_plot.op_sys_plot()
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
