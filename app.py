


######################## Importar Librerias ##############################
import streamlit as st
import pandas as pd
from PIL import Image
import c_ubicacion
import c_tipo_proyecto
import c_agua
import c_avance
import c_tipo
import e_ubicacion
import e_avance
import e_macroregion
import e_tipo
import menu
################################################################
# Set the configs
APP_TITLE = "CARTERA DE PROYECTOS MINEROS"
st.set_page_config(
    page_title = APP_TITLE,
    page_icon = Image.open('utils/pickaxe.png'),
    layout = "wide",
    initial_sidebar_state = "auto")
icon = Image.open('utils/pickaxe.png')


# External CSS
main_external_css = """
    <style>
        hr {margin: 15px 0px !important; background: #ff3a50}
        .footer {position: absolute; height: 50px; bottom: -150px; width:100%; padding:10px; text-align:center; }
        #MainMenu, .reportview-container .main footer {display: none;}
        .btn-outline-secondary {background: #FFF !important}
        .download_link {color: #f63366 !important; text-decoration: none !important; z-index: 99999 !important;
                        cursor:pointer !important; margin: 15px 0px; border: 1px solid #f63366;
                        text-align:center; padding: 8px !important; width: 200px;}
        .download_link:hover {background: #f63366 !important; color: #FFF !important;}
        h1, h2, h3, h4, h5, h6, a, a:visited {color: #054396 !important}
        label, stText, p, .caption {color: #000000 }
        .streamlit-expanderHeader {font-size: 16px !important;}
        .css-17eq0hr label, stText, .caption, .css-j075dz, .css-1t42vg8 {color: #000 !important}
        .css-17eq0hr a {text-decoration:underline;}
        .tickBarMin, .tickBarMax {color: #f84f57 !important}
        .markdown-text-container p {color: #035672 !important}
        .css-xq1lnh-EmotionIconBase {fill: #ff3a50 !important}
        .css-hi6a2p {max-width: 800px !important}
        /* Tabs */
        .tabs { position: relative; min-height: 200px; clear: both; margin: 40px auto 0px auto; background: #efefef; box-shadow: 0 48px 80px -32px rgba(0,0,0,0.3); }
        .tab {float: left;}
        .tab label { background: #f84f57; cursor: pointer; font-weight: bold; font-size: 18px; padding: 10px; color: #fff; transition: background 0.1s, color 0.1s; margin-left: -1px; position: relative; left: 1px; top: -29px; z-index: 2; }
        .tab label:hover {background: #035672;}
        .tab [type=radio] { display: none; }
        .content { position: absolute; top: -1px; left: 0; background: #fff; right: 0; bottom: 0; padding: 30px 20px; transition: opacity .1s linear; opacity: 0; }
        [type=radio]:checked ~ label { background: #035672; color: #fff;}
        [type=radio]:checked ~ label ~ .content { z-index: 1; opacity: 1; }
        /* Feature Importance Plotly Link Color */
        .js-plotly-plot .plotly svg a {color: #f84f57 !important}
    </style>
"""

st.markdown(main_external_css, unsafe_allow_html=True)




###################### SiderBar ########################################
st.sidebar.title('CARTERA DE PROYECTOS MINEROS')
st.sidebar.markdown("<div style='text-align: justify'>Esta pagina esta enfoca a analizar los datos de las Carteras de Proyectos Mineros de Construcción y Exploración Mina, estos datos fueron obtenidos del Ministerio de Energía y Minas, analizados en Power Bi y desplegado en Streamlit.</div>", unsafe_allow_html=True)
st.sidebar.write("")
st.sidebar.write("")
st.sidebar.write("")

separador=st.sidebar.selectbox(
'TIPO DE CARTERA',
("CARTERA DE CONSTRUCCIÓN",'CARTERA DE EXPLORACIÓN'))
st.sidebar.write("")
st.sidebar.title('MENÚ DE OPCIONES')
if (separador=="CARTERA DE CONSTRUCCIÓN"):
    options = st.sidebar.radio('Seleccione una página:', 
    ["SEGÚN SU UBICACIÓN","SEGÚN SU TIPO DE PROYECTO","SEGÚN EL CONSUMO DE AGUA","SEGÚN LA ETAPA DE AVANCE DEL PROYECTO","SEGÚN EL TIPO DE MINA","INFORMACIÓN"])
    if options == 'SEGÚN SU UBICACIÓN':
        c_ubicacion.main()
    elif options == 'SEGÚN SU TIPO DE PROYECTO':
        c_tipo_proyecto.main()
    elif options == 'SEGÚN EL CONSUMO DE AGUA':
        c_agua.main()
    elif options == 'SEGÚN LA ETAPA DE AVANCE DEL PROYECTO':
        c_avance.main()
    elif options == 'SEGÚN EL TIPO DE MINA':
        c_tipo.main()
    elif options == 'INFORMACIÓN':
        menu.principal()

else:
    options = st.sidebar.radio('Seleccione una página:', 
    ['SEGÚN SU UBICACIÓN', 'SEGÚN LA ETAPA DE AVANCE DEL PROYECTO','SEGÚN MACRORREGIÓN','SEGÚN TIPO DE EXPLORACIÓN',"INFORMACIÓN"])
    if options == 'SEGÚN SU UBICACIÓN':
        e_ubicacion.main()
    elif options == 'SEGÚN LA ETAPA DE AVANCE DEL PROYECTO':
        e_avance.main()
    elif options == 'SEGÚN MACRORREGIÓN':
        e_macroregion.main()
    elif options == 'SEGÚN TIPO DE EXPLORACIÓN':
        e_tipo.main()
    elif options == 'INFORMACIÓN':
        menu.principal()

