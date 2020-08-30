import streamlit as st

def main():
    st.title("Hello Streamlit")
    st.subheader("Welcome to my first streamlit app")
    st.text("Deploy the Application in Heroku")
    
     # Add a selectbox to the sidebar:
    add_selectbox = st.sidebar.selectbox(
        'Navigation',
        ('Home', 'About', 'Help')
    )

    if add_selectbox == 'About':
        st.write('You have selected about page')
    elif add_selectbox == 'Home':
        st.write('you have selected Home page')
    else:
        st.write('you have selected help page')
        
    st.balloons()

if __name__ == "__main__":
    main()
