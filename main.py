import streamlit as st
from rembg import remove
from PIL import Image
from io import BytesIO

def main():
    st.title("Quitar fondo")
    file = st.file_uploader("Seleccione una imagen")
    if file is not None:
        img = Image.open(file)
        img2 = remove(img,bgcolor=(255,255,255,255))
        buf = BytesIO()
        img2.save(buf,format='png')
        st.image(img2)
        st.download_button("Descargar",data=buf,file_name=file.name,mime='image/png')

if __name__ == "__main__":
    main()