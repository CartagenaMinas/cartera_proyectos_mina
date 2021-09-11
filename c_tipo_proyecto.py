import streamlit as st
from PIL import Image
import streamlit.components.v1 as components

    
def main():
    st.title('INVERSIONES SEGÚN EL TIPO DE PROYECTO')
    st.write("    ")
    st.markdown("<div style='text-align: justify'>En línea general, los proyectos según tipo de mina se pueden dividir en a) proyectos nuevos o greenfield, aquellos sin antecedentes de actividad productiva dentro de las concesiones mineras que la componen y b) proyectos brownfield, se desarrollan en el mismo lugar y en paralelo al proceso productivo en curso. Cabe mencionar que los proyectos brownfield se subdividen en: proyectos de ampliación y de reposición.</div>", unsafe_allow_html=True)
    st.write("    ")
    st.markdown("<div style='text-align: justify'>Por lo mencionado, la presente Cartera de Construcción cuenta con un total de 46 proyectos, de los cuales 36 son proyectos de minas nuevas o greenfield y suman una inversión conjunta de US$ 51,100 millones, representando el 91% de la inversión global de la Cartera. Los proyectos que sobresalen en este grupo son: Quellaveco (US$ 5,300 millones) y Mina Justa (US$ 1,600 millones) por encontrarse en etapa de construcción y ser considerados proyectos de interés nacional.</div>", unsafe_allow_html=True)
    st.write("    ")
    link='<iframe width="1250" height="800" src="https://app.powerbi.com/view?r=eyJrIjoiMDBhMDc0ODQtYjM3Ny00MDUzLWJkZmUtM2I0N2ExNWYxZDU5IiwidCI6IjcyODk0ODA3LTJhMzctNDExNC1hZjVlLTU3MDU1ZTljNmQ5NCJ9&pageName=ReportSection62ed3671d07212514633" frameborder="0" allowFullScreen="true"></iframe>'
    components.html(link,width=1250, height=800)
    st.write("    ")
    st.markdown("<div style='text-align: justify'>Por otro lado, 10 proyectos son de tipo brownfield con una inversión conjunta de US$ 5,058 millones, lo cual representa el 9% del monto global de inversión de la Cartera. De este grupo, 5 son proyectos de Reposición con un monto de inversión conjunto de US$ 3,026 millones y, por otro lado, 5 proyectos de Ampliación, con una inversión acumulada de US$ 2,033 millones. De los proyectos brownfield sobresalen Yanacocha Sulfuros (proyecto de Reposición) con una inversión estimada de US$ 2,100 millones y Ampliación Toromocho (proyecto de Ampliación) con una inversión estimada de US$ 1,355 millones.</div>", unsafe_allow_html=True)