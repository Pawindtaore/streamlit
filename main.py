import streamlit as st
import openai
from PIL import Image

openai.api_key = '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'

st.set_page_config(
    page_title="Générer et traiter une image en saisissant du texte",
    page_icon="✨",
    layout="centered",
    initial_sidebar_state="auto",
)

@st.cache(persist=True,allow_output_mutation=True,show_spinner=False,suppress_st_warning=True)
def openai_image(prompt):
    response = openai.Image.create(
      prompt=prompt,
      n=1,
      size="256x256"
    )
    image_url = response['data'][0]['url']
    return image_url

top_image = Image.open('static/banner_top.png')
bottom_image = Image.open('static/banner_bottom.png')
main_image = Image.open('static/main_banner.png')

st.sidebar.image(top_image,use_column_width='auto')
format_type = st.sidebar.selectbox('Generer une image 😉',["ChatGPT","DALL-E 2"])
st.sidebar.image(bottom_image,use_column_width='auto')

st.image(main_image,use_column_width='auto')
st.title("Générer et traiter une image 🏜 avec du texte")

input_text = st.text_area("Enterz votre texte ici svp... 🙋",height=50)
image_button = st.button("Générer l'image 🚀")

if image_button and input_text.strip() != "":
    with st.spinner("Chargement...💫"):
        image_url = openai_image(input_text)
        st.image(image_url, caption='Générer par OpenAI')
else:
    st.warning("Veuillez saisir quelque chose! ⚠")

hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)
st.markdown("<br><hr><center>Made with ❤️ by <a href='mailto:odppawindtaore@gmail.com?subject=ChatGPT + DALL-E WebApp!&body=Please specify the issue you are facing with the app.'><strong>Prateek Ralhan</strong></a></center><hr>", unsafe_allow_html=True)
st.markdown("<style> footer {visibility: hidden;} </style>", unsafe_allow_html=True)