import streamlit as st
from PIL import Image
import streamlit.components.v1 as components

    
def main():
    st.title('INVERSIONES SEGÚN FUENTE DE ABASTECIMIENTO PARA CONSUMO DE AGUA')
    st.write("    ")
    st.markdown("<div style='text-align: justify'>La Dirección General de Promoción y Sostenibilidad Minera estimó que el uso de agua en el subsector minero representó en el 2018, el 2.0% del volumen consuntivo nacional, gracias al estudio realizado al Compendio Nacional de Estadísticas de Recursos Hídricos, publicado en el año 2019 por la Autoridad Nacional de Agua (ANA). Dicho porcentaje representa el consumo hídrico de las actividades mineras dentro de las 14 Autoridades Administrativas de Agua (AAA) distribuidas en las diferentes cuencas hídricas del Perú.</div>", unsafe_allow_html=True)
    st.write("    ")
    st.markdown("<div style='text-align: justify'>Precisamente, dentro de las actividades mineras se encuentran las que involucran la operación de una mina, por tal motivo, en esta sección se analizará a los proyectos mineros de la presente Cartera según su fuente de abastecimiento de agua futura, una vez inicien la etapa de operación.</div>", unsafe_allow_html=True)
    st.write("    ")
    link='<iframe width="1250" height="800" src="https://app.powerbi.com/view?r=eyJrIjoiMDBhMDc0ODQtYjM3Ny00MDUzLWJkZmUtM2I0N2ExNWYxZDU5IiwidCI6IjcyODk0ODA3LTJhMzctNDExNC1hZjVlLTU3MDU1ZTljNmQ5NCJ9&pageName=ReportSection19f8a6883444d0085192" frameborder="0" allowFullScreen="true"></iframe>'
    components.html(link,width=1250, height=800)
    st.write("    ")
    st.markdown("<div style='text-align: justify'>Analizando a detalle, son 29 los proyectos con fuente única de agua los cuales representan en conjunto el 69.7% de participación de la inversión total de la Cartera de Construcción 2020. A este grupo pertenecen proyectos como Quellaveco en la región Moquegua (uso de agua superficial), Pampa de Pongo en Arequipa y Mina Justa en Ica (ambos con uso de agua de mar), asimismo, Zafranal en Arequipa y Yanacocha Sulfuros en Cajamarca (ambos con uso de agua subterránea). Por otro lado, los proyectos con fuente mixta son 6 y representan en conjunto el 6.0% de participación de la inversión total de presente Cartera. En este grupo se encuentran el proyecto Ampliación Toromocho y Fosfatos Mantaro en la región Junín (ambos con uso de agua superficial y subterráneo) y Ampliación Bayóvar en Piura (uso de agua de superficial y de mar). Finalmente, la presente Cartera cuenta con 11 proyectos sin información disponible de sus fuentes de abastecimiento de agua, dado que en su mayoría se encuentran en etapas tempranas de desarrollo; estos proyectos en conjunto representan el 24.3% de participación de la inversión global de la Cartera, siendo El Galeno, Los Chancas y Michiquillay proyectos representativos de este grupo.</div>", unsafe_allow_html=True)