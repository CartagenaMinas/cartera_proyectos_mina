import streamlit as st
from PIL import Image
import streamlit.components.v1 as components

    
def main():
    st.title('INVERSIONES SEGÚN LA ETAPA DE AVANCE DEL PROYECTO')
    st.write("    ")
    st.markdown("<div style='text-align: justify'>Los proyectos mineros durante la fase exploratoria presentan varias solicitudes de aprobación de Instrumento de Gestión Ambiental (IGA) debido a que, conforme van desarrollando sus estudios, requieren un mayor grado de certeza para la identificación de un yacimiento mineralizado en ciertas zonas de interés, en la ampliación del área de estudio y/o para la modificación de componentes, entre otros. De esta manera, para fines de simplificación, la clasificación de los proyectos seleccionados presenta las siguientes etapas:</div>", unsafe_allow_html=True)
    st.write("    ")
    st.markdown("<div style='text-align: justify'>A. Evaluación IGA: La solicitud de aprobación de IGA del proyecto se encuentra en evaluación por la Dirección General de Asuntos Ambientales Mineros (DGAAM). En esta etapa temprana se encuentran 7 proyectos. Cabe resaltar que, todos los proyectos considerados en esta etapa en la edición 2020, ya obtuvieron la aprobación del IGA, por lo que pueden ser encontrados en las siguientes etapas.</div>", unsafe_allow_html=True)
    st.write("    ")
    st.markdown("<div style='text-align: justify'>B. Evaluación de Autorización de Exploración: Luego que el IGA ha sido aprobado y de reunir todos los requisitos, el titular está facultado para presentar la solicitud de Autorización de Inicio de Actividades de Exploración a la Dirección General de Minería (DGM). Para fines de simplificación, esta etapa contempla los proyectos desde que su IGA ha sido aprobado hasta antes de que su solicitud de Autorización de Exploración sea aprobada. En la presente edición de la Cartera se cuenta con 21 proyectos en esta etapa, entre los cuales se tiene proyectos que recientemente han presentado su solicitud de consulta preliminar, como proyectos que se encuentran en proceso de consulta previa.</div>", unsafe_allow_html=True)
    link='<iframe width="1250" height="800" src="https://app.powerbi.com/view?r=eyJrIjoiODEzNDVmMGQtOGVkYy00ZmM1LWFjZDYtOWUyNTNjMjQwMjdhIiwidCI6IjcyODk0ODA3LTJhMzctNDExNC1hZjVlLTU3MDU1ZTljNmQ5NCJ9&pageName=ReportSection23419e9c3c4403469db6" frameborder="0" allowFullScreen="true"></iframe>'
    components.html(link,width=1250, height=800)
    st.write("    ")
    st.markdown("<div style='text-align: justify'>C. Ejecutando o por ejecutar exploración Por último, en esta etapa se encuentran 32 proyectos, los cuales ya cuentan con Autorización de Exploración otorgada por la DGM del MINEM, encontrándose aptos para iniciar actividades de exploración.</div>", unsafe_allow_html=True)