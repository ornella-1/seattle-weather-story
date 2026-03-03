import streamlit as st
from utils.io import load_weather
from charts.charts import chart_dashboard

st.set_page_config(page_title="Explore", layout="wide")
df = load_weather()

st.title("Interactive Exploratory View")
st.write("Use interaction to validate and extend the story—focus on one weather type, then zoom into a time window.")

st.altair_chart(chart_dashboard(df), use_container_width=True)

st.markdown("**Guided prompts:**")
st.write("- Filter to one weather type (e.g., `sun`, `rain`)—does the temperature distribution shift?")
st.write("- Brush a specific year—do extremes cluster in particular periods?")
st.write("- Compare histogram shape across weather types—what changes most: center, spread, or tails?")

from charts.charts import chart_temp_by_year

st.header("Temperature by year")
st.write("Use the dropdown to explore how temperature trends changes across different years.")
st.altair_chart(chart_temp_by_year(df), use_container_width=True)

st.write(df.head())
st.write(df.columns.tolist())