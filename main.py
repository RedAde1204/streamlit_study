import streamlit as st

# st.page_link("1.py", label="introduction")
# st.page_link("https://www.google.com",label="google")
pages={
    'algorithm':[
        st.Page('1.py', title='two'),
        st.Page('2.py', title='secondone'),
        st.Page('august2.py', title='8월2일 숙제(완탐:checkbox,radio,code)')
        ]
    }
pg=st.navigation(pages)
pg.run()