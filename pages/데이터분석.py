
import streamlit as st
import pandas as pd
import plotly.express as px

# Set page configuration
st.set_page_config(page_title="Student Grades Visualization", layout="wide")

# Title and description
st.title("Student Grades Visualization")
st.write("Visualizing student grades in Korean, English, Math, and Info subjects using Plotly Express")

# Create DataFrame from the provided data
data = {
    'name': ['lee', 'park', 'kim'],
    'grade': [2, 2, 2],
    'number': [1, 2, 3],
    'kor': [90, 80, 90],
    'eng': [91, 85, 85],
    'math': [80, 90, 70],
    'info': [100, 100, 100]
}
df = pd.DataFrame(data)

# Display the raw data
st.subheader("Raw Data")
st.dataframe(df)

# Create a bar chart using Plotly Express
fig = px.bar(
    df,
    x='name',
    y=['kor', 'eng', 'math', 'info'],
    barmode='group',
    title='Student Grades by Subject',
    labels={'value': 'Score', 'name': 'Student Name', 'variable': 'Subject'},
    color_discrete_map={
        'kor': '#636EFA',
        'eng': '#EF553B',
        'math': '#00CC96',
        'info': '#AB63FA'
    }
)

# Customize the layout
fig.update_layout(
    xaxis_title="Student Name",
    yaxis_title="Score",
    legend_title="Subject",
    yaxis_range=[0, 100],
    template='plotly_white'
)

# Display the plot
st.subheader("Grades Bar Chart")
st.plotly_chart(fig, use_container_width=True)

# Add some basic statistics
st.subheader("Basic Statistics")
st.write("Average scores per subject:")
st.write(df[['kor', 'eng', 'math', 'info']].mean().round(2))
