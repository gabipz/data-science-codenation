import streamlit as st

def main():
    st.title('Hello World')
    st.header('This is a header')
    st.subheader('This is a subheader')
    st.text('This is a text')
    st.image('logo.png')
    #st.audio('')
    #st.video('')
    
    #button
    st.markdown('Button')
    button = st.button('Button')
    if button:
        st.markdown('Clicked')
        
    #check box
    st.markdown('Checkbox')
    check = st.checkbox('Checkbox')
    if check:
        st.markdown('Clicked')
        
    st.markdown('Selectbox')
    select = st.selectbox('Choose opt', ('Opt 1', 'Opt 2'))
    if select == 'Opt 1':
        st.markdown('Opt 1')
    if select == 'Opt 2':
        st.markdown('Opt 2')
    
    st.markdown('Radio')
    radio = st.radio('Choose the options: ', ('Opt 1', 'Opt 2'))
    if radio == 'Opt 1':
        st.markdown('Opt 1')
    if radio == 'Opt 2':
        st.markdown('Opt 2')
    
    st.markdown('Multi')    
    multi = st.multiselect('Choose: ', ('Opt 1', 'Opt 2'))
    if multi == 'Opt 1':
        st.markdown('Opt 1')
    if multi == 'Opt 2':
        st.markdown('Opt 2')
        
    st.markdown('File uploader')
    file = st.file_uploader('Choose your file', type = 'csv')
    if file is not None:
        st.markdown('It is not empty')
     
    
if __name__ == '__main__':
    main()