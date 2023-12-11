import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data_url = "./hw_1_data.csv"
data = pd.read_csv(data_url)

st.title("Exploratory Data Analysis with Streamlit")

st.subheader("Dataset Overview")
st.dataframe(data.head())

st.subheader("Dataset Info")
st.text(f"Number of rows: {data.shape[0]}")
st.text(f"Number of columns: {data.shape[1]}")
st.text("Columns:")
st.text(data.columns.tolist())

st.subheader("Feature Distributions")
selected_feature = st.selectbox("Select a feature", data.columns)
sns.histplot(data[selected_feature], kde=True)
st.set_option('deprecation.showPyplotGlobalUse', False)
st.pyplot()

#columns_to_drop = ['EDUCATION', 'MARITAL_STATUS', 'GEN_INDUSTRY', 'GEN_TITLE', 'JOB_DIR', 'FAMILY_INCOME']
#data_corr = data.drop(columns=columns_to_drop)
#st.subheader("Correlation Matrix")
#corr_matrix = data.corr()
#sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f")
#st.pyplot()

st.subheader("Target Variable vs Features")
target_variable = st.selectbox("Select the target variable", data_corr.columns)
sns.scatterplot(x=data[selected_feature], y=data[target_variable])
plt.xlabel(selected_feature)
plt.ylabel(target_variable)
st.pyplot()

st.subheader("Numerical Characteristics")
numerical_summary = data_corr.describe()
st.dataframe(numerical_summary)

if __name__ == "__main__":
    st.run_app()