import streamlit as st

# st.page_link("1.py", label="introduction")
# st.page_link("https://www.google.com",label="google")
pages={
    'algorithm':[
        st.Page('1.py', title='two'),
        st.Page('2.py', title='secondone')
        ]
    }
pg=st.navigation(pages)
pg.run()