import streamlit as st
from simulation import main
import plotly.graph_objects as go

st.set_page_config(page_title="Liverpool Vs. Real Madrid Penalty Shoutout Simulation", page_icon="🏆", layout="centered", initial_sidebar_state="expanded")

hide_streamlit_style = """
            <style>
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

st.markdown("<h1 style='text-align: center'>Penalty Shootout Simulation</h1>", unsafe_allow_html=True)

st.markdown("<h3 style='text-align: center;'>Simulation Results</h3>", unsafe_allow_html=True)

lp_wins, lp_win_prob = st.columns(2)

with lp_wins:
    st.markdown(f"<p style='margin: 1rem; text-align: center; border: 1px solid gray; border-radius: 5px;'>Liverpool Wins</p>", unsafe_allow_html=True)

    liverpool_wins = st.empty()

with lp_win_prob:
    st.markdown(f"<p style='margin: 1rem; text-align: center; border: 1px solid gray; border-radius: 5px;'>Liverpool FC Win Probability</p>", unsafe_allow_html=True)

    liverpool_win_probs = st.empty()

rm_wins, rm_win_prob = st.columns(2)

with rm_wins:
    st.markdown(f"<p style='margin: 1rem; text-align: center; border: 1px solid gray; border-radius: 5px;'>Real Madrid Wins</p>", unsafe_allow_html=True)

    real_madrid_wins = st.empty()

with rm_win_prob:
    st.markdown(f"<p style='margin: 1rem; text-align: center; border: 1px solid gray; border-radius: 5px;'>Real Madrid Win Probability</p>", unsafe_allow_html=True)

    real_madrid_win_probs = st.empty()

chart = st.empty()

with st.sidebar:
    st.markdown("<h3 style='text-align: center;'>Simulation Parameters</h3>", unsafe_allow_html=True)
    with st.form('Enter the number of simulations to run'):
        number_of_simulations = st.number_input("Number of simulations", min_value=1, max_value=1000000, value=1000)


        button = st.form_submit_button("Run Simulation")
        # If hover over any button it will darken the button
        st.markdown('<style>button:hover {box-shadow: 0 5px 15px rgba(0, 0, 0, 0.8);transition: all 0.25s ease-in-out}</style>', unsafe_allow_html=True)


        if button: 
            results = main(number_of_simulations)

            liverpool_stats = results[0]
            real_madrid_stats = results[1]

            liverpool_win_count = liverpool_stats[0]
            liverpool_win_probability = liverpool_stats[1]

            real_madrid_win_count = real_madrid_stats[0]
            real_madrid_win_probability = real_madrid_stats[1]


            liverpool_wins.markdown(f"""<p style='font-size: 5rem; border-radius:5px; text-align: center; padding: 0.5rem;'>{liverpool_win_count.__format__(',.0f')}</p>""", unsafe_allow_html=True)

            liverpool_win_probs.markdown(f"<p style='font-size: 5rem; border-radius:5px; text-align: center; padding: 0.5rem;' margin:1rem;'>{str(liverpool_win_probability.__format__('.2f'))}%</p>", unsafe_allow_html=True)

            real_madrid_wins.markdown(f"""<p style='font-size: 5rem; border-radius:5px; text-align: center; padding: 0.5rem;' margin:1rem;'>{real_madrid_win_count.__format__(',.0f')}</p>""", unsafe_allow_html=True)

            real_madrid_win_probs.markdown(f"<p style='font-size: 5rem; border-radius:5px; text-align: center; padding: 0.5rem;'>{str(real_madrid_win_probability.__format__('.2f'))}%</p>", unsafe_allow_html=True)

            

            fig = go.Figure(data=[go.Bar(x=['Liverpool Wins', 'Real Madrid Wins'], y=[liverpool_win_count, real_madrid_win_count], name='Wins')])
            fig.update_layout(title_text='Wins', xaxis_title='Results', yaxis_title='Count')
            
            # Change the color of each bar
            fig.update_traces(marker_color=['#F0544F', '#C6D8D3', '#D81E5B'])

            fig.update_layout(title_text="Simulation Results", title_x=0.5)

            chart.plotly_chart(fig)




            

