import streamlit as st
from PIL import Image
import streamlit.components.v1 as components

    
def main():
    st.title('INVERSIONES SEGÚN MACRORREGIÓN DEL PROYECTO')
    st.write("    ")
    st.markdown("<div style='text-align: justify'>En el análisis por macrorregiones, el sur se caracteriza por ser principalmente cuprífero y ostentar la mayor inversión en exploración, representando el 37.2% del presupuesto total con 20 proyectos (US$ 188 millones). Las regiones más representativas son: Arequipa con el proyecto Chapitos de Camino Resources S.A.C. con una inversión de US$ 41 millones, Moquegua con el proyecto Pampa Negra de Minera Pampa de Cobre S.A.C con US$ 45 millones, y Puno con el proyecto Berenguela de Sociedad Minera Berenguela S.A. de US$ 11 millones. Por su parte, las macrorregiones centro y norte de naturaleza esencialmente aurífera, se posicionan en segundo y tercer lugar respectivamente, ambas representando el 31.4% de participación, con una inversión de US$ 159 millones.</div>", unsafe_allow_html=True)
    st.write("    ")
    st.markdown("<div style='text-align: justify'>Por un lado, la macrorregión centro contempla 26 proyectos, siendo las regiones más resaltantes: Pasco con el proyecto Yumpag de Compañía de Minas Buenaventura S.A.A. reflejando una inversión de US$ 49 millones, Lima con el proyecto Romina 2 de Compañía Minera Chungar S.A.C. con US$ 28 millones y Junín con el proyecto Carhuacayán también de Compañía Minera Chungar S.A.C. de US$ 11 millones. Por otro lado, la macrorregión norte ostenta 14 proyectos, entre sus regiones resalta La Libertad con el proyecto Las Defensas de Compañía Minera Poderosa S.A. con una inversión de US$ 69 millones, Cajamarca con el proyecto Tantahuatay 4 de Compañía Minera Coimolache S.A. de US$ 28 millones y Áncash con el proyecto Coloso de Huarmy Colosal S.A.C. de US$ 12 millones.</div>", unsafe_allow_html=True)
    st.write("    ")
    link='<iframe width="1250" height="800" src="https://app.powerbi.com/view?r=eyJrIjoiODEzNDVmMGQtOGVkYy00ZmM1LWFjZDYtOWUyNTNjMjQwMjdhIiwidCI6IjcyODk0ODA3LTJhMzctNDExNC1hZjVlLTU3MDU1ZTljNmQ5NCJ9&pageName=ReportSectione52bebae32d083e3d4d5" frameborder="0" allowFullScreen="true"></iframe>'
    components.html(link,width=1250, height=800)

  