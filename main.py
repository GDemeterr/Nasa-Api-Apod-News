import streamlit as st
import requests
import os

st.set_page_config(page_title="Nasa Api News", layout="wide")


nasa_api_key = os.getenv("NASA_API_KEY")


# Our endpoint
url = "https://api.nasa.gov/planetary/apod?" \
      f"api_key={nasa_api_key}"

# image_url =

# For the text
request = requests.get(url)
content = request.json()
# print(content)
# print(type(content))


title = content["title"]
image = content["url"]
explanation = content["explanation"]

# For the image

image_filepath = "img.png"
request2 = requests.get(image)
with open(image_filepath, "wb") as file:
    file.write(request2.content)


st.title(title)
st.image(image_filepath, width=600)
st.info(explanation)

# col1,col2,col3 = st.columns(3)
#
# with col1:
#     st.write('')
#
# with col2:
#
#     st.title(title)
#     st.image(image_filepath, width=600)
#     st.info(explanation)
#
# with col3:
#     st.write('')

