import streamlit as st
import pandas as pd


def main():
    st.title('Streamlit and Pandas')
    file = st.file_uploader('Upload your file', type='csv') #you can use 'pd.read_csv('file_name.csv')' direct 
    if file is not None:
        st.markdown('Slider')
        slider = st.slider('Values', 1,100)
        df = pd.read_csv(file)
        st.dataframe(df.head(slider))
        st.markdown('Slider: table format')
        st.table(df.head(slider))
        st.markdown('Dataframe columns')
        st.write(df.columns)
        st.markdown('Mean')  
        st.table(df.groupby('species')['petal_width'].mean()) #to file 'IRIS.csv'
    
if __name__ == '__main__':
    main()