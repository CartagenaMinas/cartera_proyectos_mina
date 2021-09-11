import streamlit as st
from PIL import Image
import streamlit.components.v1 as components

    
def main():
    st.title('INVERSIONES SEGÚN EL TIPO DE EXPLORACIÓN')
    st.write("    ")
    st.markdown("<div style='text-align: justify'>En relación al tipo de exploración, estos se pueden agrupar en greenfield o brownfield. En ese sentido, la cartera presenta 43 proyectos greenfield, los cuales representan el 79.1% del total con una inversión conjunta de US$ 400 millones. Es importante resaltar que los proyectos se encuentran en diversas zonas del Perú, incluso las no consideradas tradicionalmente mineras tales como Bongará en Amazonas, Apacheta en Huancavelica, Malpaso II en Huánuco, entre otros.</div>", unsafe_allow_html=True)
    st.write("    ")
    st.markdown("<div style='text-align: justify'>En cuanto a los proyectos brownfield, se contempla un total de 17 proyectos, cuya suma de inversión alcanza los US$ 106 millones reflejando una participación del 20.9% restante. Entre los proyectos más representativos por departamento están: Caylloma (Arequipa), Pablo Sur (Ayacucho), Tantahuatay 4 (Cajamarca), Quehuincha (Cusco), Sierra Nevada y Manuelita (Junín), Yauricocha (Lima), El Porvenir (Pasco) y Quenamari (Puno).</div>", unsafe_allow_html=True)
    link='<iframe width="1250" height="800" src="https://app.powerbi.com/view?r=eyJrIjoiODEzNDVmMGQtOGVkYy00ZmM1LWFjZDYtOWUyNTNjMjQwMjdhIiwidCI6IjcyODk0ODA3LTJhMzctNDExNC1hZjVlLTU3MDU1ZTljNmQ5NCJ9&pageName=ReportSection37cef96f91e946ce4660" frameborder="0" allowFullScreen="true"></iframe>'
    components.html(link,width=1250, height=800)
    st.write("    ")
   