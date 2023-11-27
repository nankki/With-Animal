import streamlit as st
from PIL import Image
from Find import find
from Cause import cause

def main():
    st.set_page_config(layout="wide")
    
    image = Image.open('./Data/강아지.png')

    st.image(image.resize((200,200)))
    
    st.markdown("<h1 style='text-align: center; font-size: 100px;'>With Animal</h1>", unsafe_allow_html=True)
    
    st.markdown("<h2 style='text-align: center; font-size: 30px; font-family:Nanum Myeongjo;'>-동물동반시설검색-</h2>", unsafe_allow_html=True)

    menu_list = ['시 설 검 색', '제 작 동 기']
    
    choice = st.sidebar.selectbox('M E N U', menu_list)
    
    if choice == menu_list[0]:
        find()
    elif choice == menu_list[1]:
        cause()

if __name__ == '__main__':
    main()
