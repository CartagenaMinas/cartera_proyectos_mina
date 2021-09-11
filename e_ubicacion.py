import streamlit as st
from PIL import Image
import streamlit.components.v1 as components

    
def main():
    st.title('CARTERA DE PROYECTOS DE EXPLORACIÓN MINERA')
    st.markdown('### INTRODUCCIÓN')
    st.markdown("<div style='text-align: justify'>Al cierre de 2020 y pese a la pandemia generada por el COVID-19, Perú superó el ajuste de proyección de inversión minera estimada en US$ 4200 millones logrando ejecutar US$ 4334 millones. Este monto implica desembolsos en exploración, equipamiento minero, entre otros. Cabe precisar que el escenario de rápida recuperación fue posible en gran parte a la eficacia del plan de reactivación4 económica nacional impulsada por el Gobierno Central desde el mes de mayo de 2020, con la finalidad de reanudar las actividades económicas bajo estrictas medidas de seguridad sanitaria. Estas medidas permitieron al subsector minero reactivar todas las actividades durante la aplicación de las primeras 3 fases.</div>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: justify'>Precisamente, la inversión ejecutada en el rubro de exploración minera evidenció una recuperación en el mes de diciembre de 107.6% con respecto al mes de abril de 2020, el cual fue el mes de mayor afectación por la pandemia. De este modo, las medidas realizadas por el Gobierno, permitieron que en el cuarto trimestre se ejecuten US$ 70 millones alcanzando los niveles prepandemia registrados en el primer trimestre de 2020 (US$ 65 millones).</div>", unsafe_allow_html=True)
    st.write("    ")
    st.markdown('## INVERSIONES SEGÚN LA UBICACIÓN DEL PROYECTO')
    st.markdown("<div style='text-align: justify'>Las inversiones en exploración están destinadas a proyectos mineros ubicados en 16 regiones del país. Arequipa mantiene su liderazgo a nivel nacional, representando el 17.3% del monto global de inversiones con 8 proyectos (US$ 88 millones). Los proyectos Chapitos (cuprífero) de Camino Resources S.A.C. y Caylloma (argentífero) de Minera Bateas S.A.C. son los más destacados por contener en conjunto el 71.2% del presupuesto en exploración minera en la región. </div>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: justify'>Por su parte, la región de La Libertad se ubica en segundo lugar reflejando el 15.1% del presupuesto en exploración con 3 proyectos (US$ 76 millones). El proyecto más significativo es Las Defensas (aurífero) de Compañía Minera Poderosa S.A. debido a que ostenta el mayor monto de inversión en la región.</div>", unsafe_allow_html=True)
    st.write("    ")
    st.write("    ")
    link='<iframe width="1250" height="800" src="https://app.powerbi.com/view?r=eyJrIjoiODEzNDVmMGQtOGVkYy00ZmM1LWFjZDYtOWUyNTNjMjQwMjdhIiwidCI6IjcyODk0ODA3LTJhMzctNDExNC1hZjVlLTU3MDU1ZTljNmQ5NCJ9&pageName=ReportSection8da2cf3b01902030b85e" frameborder="0" allowFullScreen="true"></iframe>'
    components.html(link,width=1250, height=800)
    st.write("    ")
    st.markdown("<div style='text-align: justify'>Mientras que, el departamento de Pasco ocupa la tercera posición conteniendo el 12.1% del monto total de inversión en cartera con 5 proyectos (US$ 61 millones). Los proyectos Yumpag (argentífero) de Compañía minera Buenaventura S.A.A., San Pedro (plúmbico) de Pan American Silver Huaron S.A. y Loma Linda (aurífero) de Consorcio Minero Sunec S.A.C. destacan por representar en conjunto el 92.3% del presupuesto para actividades de exploración en la región mencionada. Por último, las regiones de Cajamarca, Lima, Moquegua, Áncash, Puno, Junín, Ayacucho, Tacna, Apurímac, Huancavelica, Huánuco, Amazonas y Cusco, representan en conjunto el 55.5% de la inversión total en cartera.</div>", unsafe_allow_html=True)