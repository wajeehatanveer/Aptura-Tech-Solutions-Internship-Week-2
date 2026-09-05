import streamlit as st
import pandas as pd

from api_processor import (
    fetch_data,
    process_data,
    calculate_statistics,
    export_to_csv
)


st.set_page_config(
    page_title="API Data Processor",
    page_icon="📊",
    layout="wide"
)


#Custom CSS

st.markdown("""
<style>
    .main-title {
        font-size: 38px;
        font-weight: 700;
        margin-bottom: 5px;
    }

    .subtitle {
        font-size: 17px;
        color: #666;
        margin-bottom: 25px;
    }

    .metric-card {
        padding: 20px;
        border-radius: 12px;
        border: 1px solid #ddd;
        background-color: #fafafa;
    }
</style>
""", unsafe_allow_html=True)


# Header 

st.markdown(
    '<div class="main-title">📊 API Data Processing</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Fetch, clean, analyze and export JSON API data.</div>',
    unsafe_allow_html=True
)


# Fetch Data

if st.button("🔄 Fetch & Process API Data", use_container_width=True):

    with st.spinner("Fetching data from API..."):

        data = fetch_data()

        if not data:
            st.error("Unable to fetch data from the API.")
            st.stop()

        processed_data = process_data(data)

        if not processed_data:
            st.warning("No valid data available for processing.")
            st.stop()

        statistics = calculate_statistics(processed_data)

        st.session_state["processed_data"] = processed_data
        st.session_state["statistics"] = statistics

    st.success(
        f"Successfully processed {len(processed_data)} records!"
    )


# Display Results

if "processed_data" in st.session_state:

    processed_data = st.session_state["processed_data"]
    statistics = st.session_state["statistics"]

    st.markdown("---")

    # Statistics

    st.subheader("📈 Summary Statistics")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Total Records",
            statistics["total_records"]
        )

    with col2:
        st.metric(
            "Unique Users",
            statistics["unique_users"]
        )

    with col3:
        st.metric(
            "Avg. Title Length",
            statistics["average_title_length"]
        )

    with col4:
        st.metric(
            "Avg. Body Length",
            statistics["average_body_length"]
        )

    st.markdown("---")

    # Data Table

    st.subheader("📋 Processed Data")

    df = pd.DataFrame(processed_data)

    st.dataframe(
        df,
        use_container_width=True,
        height=450
    )

    # Export

    st.subheader("📥 Export Data")

    csv_data = df.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="⬇️ Download CSV",
        data=csv_data,
        file_name="output.csv",
        mime="text/csv",
        use_container_width=True
    )

    st.success("Your processed data is ready to download.")