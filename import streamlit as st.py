import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

st.set_page_config(
    page_title="Sales Analytics Project"
    ,layout='wide'
)
st.title("Sales Analysis Project")

min_sales=st.sidebar.number_input(
    "Minimum Sales",
    min_value=1000,
    value=5000,
    key="min_sales"
)

max_sales=st.sidebar.number_input(
    "Maximum Sales",
    min_value=min_sales,
    value=20000,
    key='max_sales'
)
min_profit=st.sidebar.number_input(
    "Minimum Profit",
    min_value=100,
    value=1000,
    key="min_profit"
)

max_profit=st.sidebar.number_input(
    "Maximum Profit",
    min_value=min_profit,
    value=7000,
    key="max_profit"
)

generate_data=st.sidebar.button(
    "Generate Dataset",
    key="generate_sales_data"
)

if generate_data:
    np.random.seed(10)
    months=['jan','Feb','Apr','May','June','July','August','Sep','Oct','Nov','Dec']
    df=pd.DataFrame({
        "Month": months,
        "Sales": np.random.randint(min_sales,max_sales+1,12),
        "Profit":np.random.randint(min_profit,max_profit+1,12),
           "Orders":np.random.randint(100,1000,12),
              "Customers": np.random.randint(50,500,12)   })

    df['Profit_Margin']=(df['Profit']/df['Sales'])*100

    st.subheader("Generated DataFrame")
    st.dataframe(df)
    st.subheader("Basic Calculations")

    st.write("Average Sales")
    st.write(round(df['Sales'].mean(),2))

    st.write("Average Profit")
    st.write(round(df['Profit'].mean(),2))
    
    st.write("Total Sales")
    st.write(round(df['Sales'].sum(),2))              

    st.write("Total Profit")
    st.write(round(df['Sales'].sum(),2))

    st.write("SUMMARY STATISTICS")
    st.write(df.describe())

    st.subheader("sales Histogram")
    fig,ax=plt.subsplots()
    ax.hist(df['Sales'],
            bins=10)

    ax.set_title("sales Distribution")
    set.pyplot(fig)

    st.subheader("Profit_Histogram")
    fig,ax=plt.subsplots(),
    ax.hist(df['Profit'],
                bins=10)
    
    ax.set_title("Profit Distribution")
    set.pyplot(fig)

    st.subheader("Month Sales Trend")

    fig,ax=plt.subplots()
    ax.plot(
        df['Month'],
        df['Sales'],
        marker='o')

    ax.set_title("Monthly Sales Trend")
    st.pyplot(fig)

    st.subheader("Correlation Heatmap")   
    
    fig,ax=plt.subplots(figsize=(8,5))
    sns.heatmap(
        df.select_dtypes(including=np.number).corr(),
        annot=True,
        cmap='Blues',
        ax=ax)
    st.pyplot(fig)

    st.subheader("Sales vs profit Interactive Chart")
    fig=px.line(
        df,
        x='Month',
        y=['Sales','Profit'],
        markers=True,
        title='Sales and Profit Trend')

    st.plotly_chart(
        fig,use_container_width=True)
else:
    st.info("Select inputs from the Sidebars and Click Generate Dataset")
    
