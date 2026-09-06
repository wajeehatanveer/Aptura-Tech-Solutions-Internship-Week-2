import streamlit as st
import pandas as pd

from api_processor import (
    fetch_data,
    process_data,
    calculate_statistics
)


# PAGE CONFIG

st.set_page_config(
    page_title="API Data Processor",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)


# CUSTOM CSS

st.markdown("""
<style>

    /* Main container */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
        max-width: 1400px;
    }

    /* Header */
    .hero {
        padding: 2rem 2.2rem;
        border-radius: 18px;
        background: linear-gradient(
            135deg,
            #111827 0%,
            #1f2937 100%
        );
        margin-bottom: 1.5rem;
    }

    .hero-title {
        font-size: 2.3rem;
        font-weight: 700;
        color: white;
        margin-bottom: 0.4rem;
    }

    .hero-subtitle {
        font-size: 1rem;
        color: #d1d5db;
        margin-bottom: 0;
    }

    /* Section headings */
    .section-title {
        font-size: 1.35rem;
        font-weight: 650;
        margin-top: 1.5rem;
        margin-bottom: 0.8rem;
    }

    /* Info cards */
    .info-card {
        padding: 1.2rem 1.3rem;
        border-radius: 14px;
        border: 1px solid #e5e7eb;
        background-color: #ffffff;
        min-height: 115px;
    }

    .card-label {
        font-size: 0.85rem;
        color: #6b7280;
        margin-bottom: 0.4rem;
    }

    .card-value {
        font-size: 1.8rem;
        font-weight: 700;
        color: #111827;
    }

    /* API status */
    .status-box {
        padding: 0.8rem 1rem;
        border-radius: 10px;
        background-color: #f3f4f6;
        border: 1px solid #e5e7eb;
        color: #374151;
        font-size: 0.9rem;
        margin-bottom: 1.2rem;
    }

    /* Download box */
    .download-box {
        padding: 1.2rem 1.4rem;
        border-radius: 14px;
        border: 1px solid #e5e7eb;
        background-color: #f9fafb;
        margin-top: 1rem;
        margin-bottom: 0.8rem;
    }

    .download-title {
        font-size: 1rem;
        font-weight: 650;
        color: #111827;
        margin-bottom: 0.2rem;
    }

    .download-text {
        font-size: 0.85rem;
        color: #6b7280;
    }

    /* Sidebar */
    [data-testid="stSidebar"] {
        border-right: 1px solid #e5e7eb;
    }

    /* Buttons */
    .stButton > button {
        border-radius: 10px;
        font-weight: 600;
        padding: 0.65rem 1rem;
    }

    /* Dataframe */
    [data-testid="stDataFrame"] {
        border-radius: 12px;
        overflow: hidden;
    }

    /* Footer */
    .footer {
        text-align: center;
        color: #9ca3af;
        font-size: 0.8rem;
        margin-top: 3rem;
        padding-top: 1rem;
        border-top: 1px solid #e5e7eb;
    }

</style>
""", unsafe_allow_html=True)


# SIDEBAR

with st.sidebar:

    st.markdown("## 📊 Data Processor")

    st.caption("API Data Processing Dashboard")

    st.markdown("---")

    st.markdown("### Navigation")

    page = st.radio(
        "Go to",
        [
            "Dashboard",
            "Processed Data",
            "Export Data"
        ],
        label_visibility="collapsed"
    )

    st.markdown("---")

    st.markdown("### About")

    st.caption(
        "Fetch JSON data from a public API, "
        "process selected fields, calculate statistics, "
        "and export the results to CSV."
    )


# HEADER

st.markdown("""
<div class="hero">

    <div class="hero-title">
        📊 API Data Processing
    </div>

    <div class="hero-subtitle">
        Fetch, clean, analyze and export JSON API data
        through a simple interactive dashboard.
    </div>

</div>
""", unsafe_allow_html=True)


# FETCH DATA

if st.button(
    "🔄 Fetch & Process API Data",
    use_container_width=True
):

    with st.spinner("Fetching and processing API data..."):

        data = fetch_data()

        if not data:
            st.error(
                "Unable to fetch data from the API. "
                "Please check your internet connection and try again."
            )
            st.stop()

        processed_data = process_data(data)

        if not processed_data:
            st.warning(
                "The API returned data, but no valid records "
                "were available for processing."
            )
            st.stop()

        statistics = calculate_statistics(processed_data)

        st.session_state["processed_data"] = processed_data
        st.session_state["statistics"] = statistics

    st.success(
        f"Successfully processed {len(processed_data)} records."
    )


# NO DATA STATE

if "processed_data" not in st.session_state:

    st.info(
        "👆 Click **Fetch & Process API Data** to retrieve "
        "and analyze the latest API data."
    )

    st.markdown("""
    <div class="status-box">
        <strong>Ready to process data</strong><br>
        The application will fetch JSON data, clean valid records,
        calculate statistics, and prepare the data for CSV export.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="footer">
        API Data Processing • Python & Streamlit
    </div>
    """, unsafe_allow_html=True)

    st.stop()


# LOAD SESSION DATA

processed_data = st.session_state["processed_data"]
statistics = st.session_state["statistics"]

df = pd.DataFrame(processed_data)


# DASHBOARD

if page == "Dashboard":

    st.markdown(
        '<div class="section-title">📈 Summary Statistics</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown(f"""
        <div class="info-card">
            <div class="card-label">Total Records</div>
            <div class="card-value">
                {statistics["total_records"]}
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div class="info-card">
            <div class="card-label">Unique Users</div>
            <div class="card-value">
                {statistics["unique_users"]}
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown(f"""
        <div class="info-card">
            <div class="card-label">Avg. Title Length</div>
            <div class="card-value">
                {statistics["average_title_length"]}
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown(f"""
        <div class="info-card">
            <div class="card-label">Avg. Body Length</div>
            <div class="card-value">
                {statistics["average_body_length"]}
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown(
        '<div class="section-title">🔗 API Processing Status</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="status-box">
        <strong>✓ Processing completed successfully</strong><br>
        API data was fetched, cleaned, validated and processed.
    </div>
    """, unsafe_allow_html=True)

    st.markdown(
        '<div class="section-title">📋 Data Preview</div>',
        unsafe_allow_html=True
    )

    st.dataframe(
        df.head(10),
        use_container_width=True,
        hide_index=True,
        height=350
    )


# PROCESSED DATA

elif page == "Processed Data":

    st.markdown(
        '<div class="section-title">📋 Processed API Data</div>',
        unsafe_allow_html=True
    )

    st.caption(
        f"Showing {len(df)} processed records."
    )

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True,
        height=550
    )


# EXPORT DATA

elif page == "Export Data":

    st.markdown(
        '<div class="section-title">📥 Export Processed Data</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="download-box">

        <div class="download-title">
            Download processed data
        </div>

        <div class="download-text">
            Export the processed API records as a CSV file.
        </div>

    </div>
    """, unsafe_allow_html=True)

    csv_data = df.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="⬇️ Download output.csv",
        data=csv_data,
        file_name="output.csv",
        mime="text/csv",
        use_container_width=True
    )

    st.success(
        "Your processed data is ready to download."
    )


# FOOTER

st.markdown("""
<div class="footer">
    API Data Processing Dashboard • Built with Python & Streamlit
</div>
""", unsafe_allow_html=True)
