import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import altair as alt
import plotly.express as px
from PIL import Image
logo = Image.open('logo1.png')
#pip install pandas numpy matplotlib seaborn streamlit
#to run streamlit :   streamlit run weathertest.py 
st.set_page_config(page_title="Mobile  EDA", page_icon=":bar_chart:", layout="wide")
st.image(logo)
st.title("CSE DEPARTMENT")
st.title("Exploratory Data Analysis on Mobile Dataset")
# File upload
uploaded_file = st.file_uploader("Choose a Mobile Dataset csv")
if uploaded_file is not None:
    data=pd.read_csv(uploaded_file)
    st.dataframe(data)
# Define the list of names
    names = ["K.Keerthi", "T.Poojitha","V.N.Karthik", "K.Saran Sai","G.Sruthi","N.Durga Prasad","K.Sanjay"]

# Add the names to the sidebar
    st.sidebar.title("Project Team Members:")

    for name in names:
        st.sidebar.write(name)

    st.sidebar.title("Under The Guidance of :")
    st.sidebar.write("Dr.Bomma.Ramakrishna")
    st.title("Mobile Data Analysis")

    if st.checkbox("Show raw data"):
            st.write(data)

    if st.checkbox("Show first 25 rows"):
            st.write(data.head(25))

    if st.checkbox("Show shape"):
            st.write(data.shape)

    if st.checkbox("Show index"):
            st.write(data.index)

    if st.checkbox("Show columns"):
            st.write(data.columns)

    if st.checkbox("Show data types"):
            st.write(data.dtypes)

    if st.checkbox("Show unique values for 'Brands' column"):
            st.write(data['Brand'].unique())

    if st.checkbox("Show count of non-null values"):
            st.write(data.count())

    if st.checkbox("Show unique values count for each column"):
            st.write(data.nunique())

    if st.checkbox("Show unique models of'Apple'Brand"):
        st.write(data[data['Brand'] == 'Apple'])

    if st.checkbox("Show number of times 'ScreenSize is exactly 6.5(inches)'"):
        st.write(data[data['ScreenSize'] == '6.5'])
        
    if st.checkbox("Show number of times 'Oppo was exactly 5000(mAh) Battery Capacity'"):
        st.write(data[(data['Brand'] =='Oppo') & (data.Battery == 5000)])

    if st.checkbox("Show all instances when 'Max' was recorded"):
        st.write(data[data['Model'].str.contains('Max')])

    if st.checkbox("Show all instances when 'Storage is above 64(GB)' and 'RAM is exactly 6'"):
        st.write(data[(data['Storage'] >= 64) & (data['RAM'] == 6)])

    if st.checkbox("Show Mean value of each column against each 'RAM'"):
        st.write(data.groupby('RAM').mean())

    if st.checkbox("Show Minimum value of each column against each 'Storage'"):
        st.write(data.groupby('Storage').min())

    if st.checkbox("Show Maximum value of each column against each 'Storage'"):
        st.write(data.groupby('Storage').max())

    if st.checkbox("Show all records where 'Price' is '$799' "):
        st.write(data[data['Price($)'] == '799' ])

    if st.checkbox("Show all instances when 'Brand equal to Oneplus' or 'Price is above $599'"):
        st.write(data[(data['Brand'] == 'OnePlus') | (data['Price($)'] > '599' )])

    if st.checkbox("show the' Distribution of Brands '"):
          st.write("## Distribution of Brands")
          # Create histogram of temperatures
          fig, ax = plt.subplots()
          sns.histplot(data=data, y="Brand", ax=ax)
          ax.set_xlabel("count")
          ax.set_ylabel("Mobile Brands")
          # Display histogram
          st.pyplot(fig)
     #Is there a relationship between temperature and visibility?
     # Data visualization question
    if st.checkbox(" show the 'Relation between Storage and RAM '"):
          st.write("## Relationship between Storage and RAM")
          # Create scatterplot of temperature and visibility
          fig, ax = plt.subplots()
          sns.scatterplot(data=data, x="Storage", y="RAM", ax=ax)
          ax.set_xlabel("Storage(GB)")
          ax.set_ylabel("RAM(GB)")
          # Display scatterplot
          st.pyplot(fig) 
    
    if st.checkbox("show the custom relationships"):
          st.write("## Custom comparisions")
        #   pivot = data.pivot_table(index='RAM', columns='Price($)', values='count')
          column1 = st.selectbox('Select column 1', data.columns)
          column2 = st.selectbox('Select column 2', data.columns)

          # Create a pivot table to prepare the data for the heatmap
          pivot_table = pd.pivot_table(data, values=column1, index=[column2], aggfunc=len)

          # Create the heatmap using seaborn
          sns.heatmap(pivot_table, cmap='Reds', annot=True, fmt='g')
          st.pyplot(plt)
    
    if st.checkbox("show the custom bar graph comparisions"):
          st.write("## Custom bar graph comparisions")
          column1 = st.selectbox('Select column', data.columns)
          bar_chart = alt.Chart(data).mark_bar().encode(
            x=alt.X(column1, type='nominal'),
            y=alt.Y('count()', title='Number of Records'),
            tooltip=[column1, 'count()']
            ).interactive()
          st.altair_chart(bar_chart, use_container_width=True)
    
    if st.checkbox("show the custom pie chart comparisions"):
          st.write("## Custom pie chart comparisions")
          column1 = st.selectbox('Select column1', data.columns)
          fig = px.pie(data, names=column1)

# Show the pie chart in Streamlit
          st.plotly_chart(fig, use_container_width=True)




          


       
          









