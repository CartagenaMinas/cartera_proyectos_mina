import streamlit as st
from PIL import Image
import streamlit.components.v1 as components

    
def main():
    st.title('CARTERA DE PROYECTOS DE CONSTRUCCIÓN DE MINA')
    st.markdown('### INTRODUCCIÓN')
    st.markdown("<div style='text-align: justify'>A lo largo de la historia peruana, desde la lejana época incaica hasta el día de hoy, la importancia de la actividad minera siempre se ha manifestado positivamente en los diversos indicadores macroeconómicos.</div>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: justify'>De esta manera la minería representó en el Perú el 9.1% del Producto Bruto Interno, es más, si consideramos el efecto multiplicador de la actividad minera en otros sectores de la economía se estima una participación de 15.9% del PBI nacional . Asimismo, las exportaciones mineras conformadas en un 97.9% por productos metálicos (cobre, oro zinc, plomo entre otros) y 2.1% de productos no metálicos, representaron el 60.2% del valor total de las exportaciones nacionales. Además, a nivel de recaudación fiscal, el subsector minero contribuyó, el 8.1% de los ingresos internos totales recaudados por la SUNAT.</div>", unsafe_allow_html=True)
    st.write("    ")
    st.markdown('## INVERSIONES SEGÚN UBICACIÓN DEL PROYECTO')
    st.markdown("<div style='text-align: justify'>Respecto a las inversiones según ubicación del proyecto, se contemplan proyectos mineros localizados en 17 regiones a nivel nacional; siendo Cajamarca la región líder con el mayor monto global de inversiones de la Cartera, representando el 31.9% (US$ 17,900 millones) y un total de 5 proyectos en esta región norteña. Precisamente de entre estos cinco proyectos localizados en esta parte del país, destaca Yanacocha Sulfuros debido a su inicio de construcción estimado para el año 2021.</div>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: justify'>En segunda posición se encuentra la región Apurímac con un monto de inversión equivalente a US$ 10,243 millones, lo cual representa el 18.2% de la inversión global, distribuidos en 7 proyectos. De estos siete proyectos destacan Hierro Apurímac y Los Chancas por poseer los mayores montos de inversión con US$ 2,900 millones y US$ 2,600 millones, respectivamente. Además, es importante mencionar que Chalcobamba Fase I, correspondiente a un tajo nuevo en explotación de la actual Minera Las Bambas, estaría iniciando construcción en 2021.</div>", unsafe_allow_html=True)
    st.write("    ")
    st.write("    ")
    link='<iframe width="1250" height="800" src="https://app.powerbi.com/view?r=eyJrIjoiMDBhMDc0ODQtYjM3Ny00MDUzLWJkZmUtM2I0N2ExNWYxZDU5IiwidCI6IjcyODk0ODA3LTJhMzctNDExNC1hZjVlLTU3MDU1ZTljNmQ5NCJ9" frameborder="0" allowFullScreen="true"></iframe>'
    components.html(link,width=1250, height=800)
    st.write("    ")
    st.markdown("<div style='text-align: justify'>En tercer lugar, se ubica la región Moquegua con una inversión de US$ 6,377 millones, representando el 11.4% de la inversión total, distribuidos en 3 proyectos. Siendo Quellaveco el proyecto más representativo de la región con una inversión estimada en US$ 5,300 millones, el cual inició construcción en el 2018 y tiene previsto culminar en el 2022. Asimismo, las regiones de Arequipa (4 proyectos) y Piura (3 proyectos), con inversiones de US$ 5,463 millones y US$ 3,631 millones respectivamente, representan en conjunto el 16.2% de la inversión total en la cartera de construcción. De estas dos regiones, en Piura se sitúan proyectos no metálicos de explotación de fosfatos como la Ampliación Bayóvar y Fosfatos Pacíficos con US$ 1,131 millones y en Arequipa con el mayor monto de inversión el proyecto de hierro Pampa de Pongo con US$ 2,200 millones. Por su parte, las regiones de Junín y Cusco contienen 4 proyectos cada uno englobando una inversión de US$ 2,421 millones y US$ 2,296 millones, respectivamente. Ambas regiones en conjunto representan el 8.4% de la inversión global en cartera. En relación a estas dos regiones, los proyectos más significativos son Ampliación Toromocho que inició construcción en 2018, con un monto de inversión estimado en US$ 1,355 millones y el proyecto Pampacancha, correspondiente a la explotación de un nuevo tajo de la actual Unidad Constancia (US$ 70 millones) el cual fue incorporado en la presente edición y se estima que iniciará construcción en el 2021. Por otro lado, en lo que respecta a regiones que poseen una participación superior a 2% de la inversión total, tenemos a Ica (US$ 1,740 millones), Puno (US$ 1,631 millones), Lambayeque (US$ 1,437 millones) y Áncash (US$ 1,282 millones). De estas regiones, el proyecto más representativo es Mina Justa en la provincia de Nazca en la región Ica, el cual inició construcción en el 2018 y ostenta una inversión de US$ 1,600 millones. Por último, Huancavelica, Lima, Pasco, Amazonas, Ayacucho y La Libertad concentran en conjunto el 3.1% de la inversión total de la Cartera ascendiendo a US$ 1,738 millones, con un proyecto en cada región mencionada.</div>", unsafe_allow_html=True)