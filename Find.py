import streamlit as st
import pandas as pd
import pydeck as pdk
from geopy.geocoders import Nominatim
from geopy.distance import geodesic

def find():
    data = pd.read_csv('./Data/반려동물.csv', encoding='949')

    value_list = data['종류'].unique()
    
    selected_value = st.selectbox('장소를 선택하세요', value_list)

    filtered_data = data[data['종류'] == selected_value]

    user_location = st.text_input('주소를 입력하세요')

    if user_location:
        geolocator = Nominatim(user_agent='my_geocoder')
        location = geolocator.geocode(user_location)

        if location is not None:
            user_lat = location.latitude
            user_lon = location.longitude

            filtered_data['거리'] = filtered_data.apply(lambda row: geodesic((user_lat, user_lon), (row['위도'], row['경도'])).km, axis=1)

            nearest_facilities = filtered_data.nsmallest(20, '거리')  

            map_data = pd.DataFrame({
                'latitude': nearest_facilities['위도'],
                'longitude': nearest_facilities['경도'],
                '이름': nearest_facilities['이름']
            })

            st.header("가장 가까운 시설 TOP 20")  

            col1, col2 = st.columns([1,1.5])

            with col1:
                for index, facility in nearest_facilities.iterrows():
                    st.subheader(f"시설명: {facility['이름']}")
                    st.write(f"거리: {facility['거리']} km")
                    st.write(f"도로명주소: {facility['도로명주소']}")
                    st.write(f"전화번호: {facility['전화번호']}")
                    st.write(f"휴무: {facility['휴무']}")
                    st.write(f"영업시간: {facility['영업시간']}")
                    st.write("---")

            with col2:
                view_state = pdk.ViewState(
                    latitude=user_lat,
                    longitude=user_lon,
                    zoom=15,
                    pitch=0
                )
                layers = [
                    pdk.Layer(
                        "ScatterplotLayer",
                        data=map_data,
                        get_position=['longitude', 'latitude'],
                        get_radius=15,
                        get_fill_color=[0, 255, 0, 70],
                        pickable=True,
                        auto_highlight=True,
                        tooltip=["이름"]
                    )
                ]
                tooltip = {"html": "<b>{이름}</b>", "style": {"backgroundColor": "white", "color": "#333333"}}
                
                st.pydeck_chart(pdk.Deck(
                    map_style="mapbox://styles/mapbox/light-v9",
                    initial_view_state=view_state,
                    layers=layers,
                    tooltip=tooltip,
                ))
                

        else:
            st.write("올바른 위치를 입력하세요")