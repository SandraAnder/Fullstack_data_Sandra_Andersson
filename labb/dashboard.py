import streamlit as st 
from pathlib import Path
from frontend.kpi import ContentKPI, AgeGenderKPI, Top15KPI
from frontend.graphs import ViewsTrend
from backend.constants import Color


# device_kpi = DeviceKPI()
content_kpi = ContentKPI()
views_graph = ViewsTrend()
age_kpi = AgeGenderKPI()
#plot_a_g = ViewsTrend()
top_15 = Top15KPI()
top_15_plot = ViewsTrend()

def layout():
    st.markdown("# The data driven youtuber")
    st.markdown("Den här dashboarden syftar till att utforska datan i min youtubekanal")
    # device_kpi.display_device_views()
    # device_kpi.display_device_summary()
    content_kpi.display_content()
    views_graph.display_plot()
    age_kpi.display_gender_age()
    #plot_a_g.plot_age_gender()
    top_15.display_top_videos()
    top_15_plot.top_15_plot()


    read_css()


def read_css():
    css_path = Path(__file__).parent / 'style.css'

    with open(css_path) as css:
        st.markdown(
            f'<style>{css.read()}</style>', unsafe_allow_html=True
        )

if __name__ == "__main__":
    layout()