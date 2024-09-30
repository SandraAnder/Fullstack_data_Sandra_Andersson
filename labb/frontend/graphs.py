from utils.query_database import QueryDatabase
import plotly.express as px
import streamlit as st
import pycountry
from backend.constants import Color

class ViewsTrend:
    def __init__(self) -> None:
        self.df = QueryDatabase("SELECT * FROM marts.views_per_date").df
        self.age_df = QueryDatabase("SELECT * FROM marts.content_age_viewers").df
        self.gender_content = QueryDatabase("SELECT * FROM marts.content_gender_viewers").df
        self.content_top15 = QueryDatabase("SELECT * FROM marts.content_top_15_viewed").df
        self.content_geog = QueryDatabase("SELECT * FROM marts.content_viewer_geografy").df
        self._recent_10 = QueryDatabase("SELECT * FROM marts.content_10_latest_vid").df
        self._op_sys = QueryDatabase("SELECT * FROM marts.op_system_views").df
        self._content_geog = QueryDatabase("SELECT * FROM marts.content_viewer_geografy").df
        
        print(self.df)

    def display_plot(self):
        fig = px.line(self.df, x="Datum", y="Visningar")
        st.markdown("## Antal visningar under senaste månaden")
        #st.plotly_chart(fig)

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
        self.content_top15 = self.content_top15.sort_values(by='Antal_visningar', ascending=False)

        st.markdown("### Topp 15 mest tittade videor")
        fig = px.bar(
            self.content_top15.iloc[1:].head(15),
            y='Titel',
            x='Antal_visningar',
            #title='Top 15 mest tittade videor',
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
            yaxis=dict(autorange="reversed"),  # Omvänd y-axel för att få den mest tittade videon högst upp
            plot_bgcolor='rgba(0, 0, 0, 0)',  # Ändra bakgrundsfärg för diagrammet till vit
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
                labels={"totala_visningar": "", "Videotitel": ""}, # labels={"totala_visningar": "Totala Visningar", "Videotitel": "Titel"}
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
        op_sys_df = self._op_sys[:-1].sort_values(by="Totala_visningar", ascending=True).reset_index(drop=True)
        
        #st.markdown("## Vilka operativsystem är vanligast")

        fig = px.bar(
            op_sys_df, 
            x='Totala_visningar', 
            y='Operativsystem', 
            orientation='h',
            color='Totala_visningar',
            color_continuous_scale='Peach',
            title='Vanligaste operativsystemet baserat på totala visningar',
            labels={'Totala_visningar': 'Antal visningar', 'Operativsystem': 'Operativsystem'},
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
            locations="Geografi_ISO3",  # Kolumnen med länderkoder (t.ex. "SE", "IN", "MT") är nu omgjort till 3 SWE, IND, MLT för att coropleth kartan inte kan ta ISO-2
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
            plot_bgcolor='rgba(0, 0, 0, 0)',  # Transparent bakgrund för själva plotområdet
            paper_bgcolor='rgba(0, 0, 0, 0)',
            coloraxis_colorbar=dict(
            title="Totala Visningar",
            x=0.75,  # Adjust this value to move the colorbar closer to the map
            xanchor='left') 
   
        )

        st.plotly_chart(fig, use_container_width=True)




    # def make_heatmap(input_df, input_y, input_x, input_color, input_color_theme):
    #     heatmap = alt.Chart(input_df).mark_rect().encode(
    #             y=alt.Y(f'{input_y}:O', axis=alt.Axis(title="Year", titleFontSize=18, titlePadding=15, titleFontWeight=900, labelAngle=0)),
    #             x=alt.X(f'{input_x}:O', axis=alt.Axis(title="", titleFontSize=18, titlePadding=15, titleFontWeight=900)),
    #             color=alt.Color(f'max({input_color}):Q',
    #                             legend=None,
    #                             scale=alt.Scale(scheme=input_color_theme)),
    #             stroke=alt.value('black'),
    #             strokeWidth=alt.value(0.25),
    #         ).properties(width=900
    #         ).configure_axis(
    #         labelFontSize=12,
    #         titleFontSize=12
    #         ) 
    #     # height=300
    #     return heatmap


    #     def make_donut(input_response, input_text, input_color):
            # if input_color == 'blue':
            #     chart_color = ['#29b5e8', '#155F7A']
            # if input_color == 'green':
            #     chart_color = ['#27AE60', '#12783D']
            # if input_color == 'orange':
            #     chart_color = ['#F39C12', '#875A12']
            # if input_color == 'red':
            #     chart_color = ['#E74C3C', '#781F16']
                
            # source = pd.DataFrame({
            #     "Topic": ['', input_text],
            #     "% value": [100-input_response, input_response]
            # })
            # source_bg = pd.DataFrame({
            #     "Topic": ['', input_text],
            #     "% value": [100, 0]
            # })
                
            # plot = alt.Chart(source).mark_arc(innerRadius=45, cornerRadius=25).encode(
            #     theta="% value",
            #     color= alt.Color("Topic:N",
            #                     scale=alt.Scale(
            #                         #domain=['A', 'B'],
            #                         domain=[input_text, ''],
            #                         # range=['#29b5e8', '#155F7A']),  # 31333F
            #                         range=chart_color),
            #                     legend=None),
            # ).properties(width=130, height=130)
                
            # text = plot.mark_text(align='center', color="#29b5e8", font="Lato", fontSize=32, fontWeight=700, fontStyle="italic").encode(text=alt.value(f'{input_response} %'))
            # plot_bg = alt.Chart(source_bg).mark_arc(innerRadius=45, cornerRadius=20).encode(
            #     theta="% value",
            #     color= alt.Color("Topic:N",
            #                     scale=alt.Scale(
            #                         # domain=['A', 'B'],
            #                         domain=[input_text, ''],
            #                         range=chart_color),  # 31333F
            #                     legend=None),
            # ).properties(width=130, height=130)
            # return plot_bg + plot + text

    # def gain_loss():
    # col = st.columns((1.5, 4.5, 2), gap='medium')
    # with col[0]:
    # st.markdown('#### Gains/Losses')

    # df_population_difference_sorted = calculate_population_difference(df_reshaped, selected_year)

    # if selected_year > 2010:
    #     first_state_name = df_population_difference_sorted.states.iloc[0]
    #     first_state_population = format_number(df_population_difference_sorted.population.iloc[0])
    #     first_state_delta = format_number(df_population_difference_sorted.population_difference.iloc[0])
    # else:
    #     first_state_name = '-'
    #     first_state_population = '-'
    #     first_state_delta = ''
    # st.metric(label=first_state_name, value=first_state_population, delta=first_state_delta)

    # if selected_year > 2010:
    #     last_state_name = df_population_difference_sorted.states.iloc[-1]
    #     last_state_population = format_number(df_population_difference_sorted.population.iloc[-1])   
    #     last_state_delta = format_number(df_population_difference_sorted.population_difference.iloc[-1])   
    # else:
    #     last_state_name = '-'
    #     last_state_population = '-'
    #     last_state_delta = ''
    # st.metric(label=last_state_name, value=last_state_population, delta=last_state_delta)

    
    # st.markdown('#### States Migration')

    # if selected_year > 2010:
    #     # Filter states with population difference > 50000
    #     # df_greater_50000 = df_population_difference_sorted[df_population_difference_sorted.population_difference_absolute > 50000]
    #     df_greater_50000 = df_population_difference_sorted[df_population_difference_sorted.population_difference > 50000]
    #     df_less_50000 = df_population_difference_sorted[df_population_difference_sorted.population_difference < -50000]
        
    #     # % of States with population difference > 50000
    #     states_migration_greater = round((len(df_greater_50000)/df_population_difference_sorted.states.nunique())*100)
    #     states_migration_less = round((len(df_less_50000)/df_population_difference_sorted.states.nunique())*100)
    #     donut_chart_greater = make_donut(states_migration_greater, 'Inbound Migration', 'green')
    #     donut_chart_less = make_donut(states_migration_less, 'Outbound Migration', 'red')
    # else:
    #     states_migration_greater = 0
    #     states_migration_less = 0
    #     donut_chart_greater = make_donut(states_migration_greater, 'Inbound Migration', 'green')
    #     donut_chart_less = make_donut(states_migration_less, 'Outbound Migration', 'red')

    # migrations_col = st.columns((0.2, 1, 0.2))
    # with migrations_col[1]:
    #     st.write('Inbound')
    #     st.altair_chart(donut_chart_greater)
    #     st.write('Outbound')
    #     st.altair_chart(donut_chart_less)

    #     #col 2
    #     with col[1]:
    # st.markdown('#### Total Population')
    
    # choropleth = make_choropleth(df_selected_year, 'states_code', 'population', selected_color_theme)
    # st.plotly_chart(choropleth, use_container_width=True)
    
    # heatmap = make_heatmap(df_reshaped, 'year', 'states', 'population', selected_color_theme)
    # st.altair_chart(heatmap, use_container_width=True)

    # #col3
    # with col[2]:
    # st.markdown('#### Top States')

    # st.dataframe(df_selected_year_sorted,
    #              column_order=("states", "population"),
    #              hide_index=True,
    #              width=None,
    #              column_config={
    #                 "states": st.column_config.TextColumn(
    #                     "States",
    #                 ),
    #                 "population": st.column_config.ProgressColumn(
    #                     "Population",
    #                     format="%f",
    #                     min_value=0,
    #                     max_value=max(df_selected_year_sorted.population),
    #                  )}
    #              )
    
    # with st.expander('About', expanded=True):
    #     st.write('''
    #         - Data: [U.S. Census Bureau](<https://www.census.gov/data/datasets/time-series/demo/popest/2010s-state-total.html>).
    #         - :orange[**Gains/Losses**]: states with high inbound/ outbound migration for selected year
    #         - :orange[**States Migration**]: percentage of states with annual inbound/ outbound migration > 50,000
    #         ''')