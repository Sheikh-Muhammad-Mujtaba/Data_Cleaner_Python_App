


import streamlit as st
import pandas as pd
import os
from io import BytesIO

# Set up the page
st.set_page_config(
    page_title="🧹 Data Cleaner Pro 🧹",
    page_icon="✨",
    layout="wide"
)

# Title and Description
st.title("🧹 Data Cleaner Pro 🧹")
st.write("""
✨ Welcome to **Data Cleaner Pro**! ✨  
This tool helps you clean and transform data files (CSV, XLSX, Markdown, HTML).  
Upload a file, clean it, and download it in a different format!

🚀 **Start by uploading your file below!**
""")

# File Uploader
uploaded_files = st.file_uploader(
    "📤 Upload your file(s)",
    type=["csv", "xlsx", "md", "html"],
    accept_multiple_files=True
)

if uploaded_files:
    for file in uploaded_files:
        file_extension = os.path.splitext(file.name)[-1].lower()
        df = None  # Initialize dataframe

        # Read the uploaded file
        if file_extension == ".csv":
            df = pd.read_csv(file)
        elif file_extension == ".xlsx":
            df = pd.read_excel(file, engine="openpyxl")
        elif file_extension == ".md":
            df = pd.read_table(file)
        elif file_extension == ".html":
            df = pd.read_html(file)[0]  # Extract first table
        else:
            st.error(f"❌ File type not supported: {file_extension}")
            continue

        st.write(f"**📂 File Name:** {file.name}")
        st.write(f"**📄 File Type:** {file_extension}")
        st.write(f"**📊 File Size:** {file.size / 1024:.2f} KB")

        st.write("📋 **Preview of the Data**")
        st.dataframe(df.head())

        # Data Cleaning Options
        st.subheader(f"🧹 Data Cleaning for {file.name}")

        if st.checkbox(f"🧹 Clean Data for {file.name}"):
            col1, col2 = st.columns(2)

            with col1:
                if st.button(f"❌ Remove Duplicates from {file.name}"):
                    df.drop_duplicates(inplace=True)
                    st.success("✅ Duplicates Removed Successfully!")

            with col2:
                if st.button(f"🛠️ Fill Missing Values for {file.name}"):
                    numeric_cols = df.select_dtypes(include="number").columns
                    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
                    st.success("✅ Missing Values Filled Successfully!")

            # Column selection
            st.subheader(f"✂️ Select Columns for {file.name}")
            selected_columns = st.multiselect(
                "Select Columns to Keep",
                options=df.columns,
                default=list(df.columns)
            )
            if selected_columns:
                df = df[selected_columns]
                st.success("✅ DataFrame Updated with Selected Columns")

            # Data Visualization
            st.subheader(f"📊 Data Visualization for {file.name}")
            if st.checkbox(f"📊 Show Visualization for {file.name}"):
                st.bar_chart(df.select_dtypes(include="number").iloc[:, :2])

            # File Conversion
            st.subheader(f"🔁 Convert {file.name} to another format")
            conversion_format = st.selectbox(
                f"Convert {file.name} To:",
                ["CSV", "Excel", "Markdown", "HTML"]
            )

            if st.button(f"Convert {file.name} to {conversion_format}"):
                buffer = BytesIO()

                if conversion_format == "CSV":
                    df.to_csv(buffer, index=False)
                    file_name = file.name.replace(file_extension, ".csv")
                    mime_type = "text/csv"

                elif conversion_format == "Excel":
                     df.to_excel(buffer, index=False)
                     file_name = file.name.replace(file_extension, ".xlsx")
                     mime_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"

                elif conversion_format == "Markdown":
                    markdown_content = df.to_markdown(index=False)
                    buffer.write(markdown_content.encode("utf-8"))
                    file_name = file.name.replace(file_extension, ".md")
                    mime_type = "text/markdown"

                elif conversion_format == "HTML":
                    html_content = df.to_html(index=False)
                    buffer.write(html_content.encode("utf-8"))
                    file_name = file.name.replace(file_extension, ".html")
                    mime_type = "text/html"

                buffer.seek(0)

                # Ensure session state variables exist
                if "file_converted" not in st.session_state:
                    st.session_state.file_converted = False
                if "download_clicked" not in st.session_state:
                    st.session_state.download_clicked = False

                # Mark the file as converted
                st.session_state.file_converted = True

                # Download Button
                download_clicked = st.download_button(
                    label=f"📥 Click Here to Download {file_name} 💾",
                    data=buffer,
                    file_name=file_name,
                    mime=mime_type
                )

                if download_clicked:
                    st.session_state.download_clicked = True
                    st.success(f"🎉 {file_name} Converted and Downloaded Successfully! 🎉")
                elif st.session_state.file_converted:
                    st.info("⚠️ Your file has been converted! Please click the download button to save it.")
