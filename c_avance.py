import streamlit as st
from PIL import Image
import streamlit.components.v1 as components

    
def main():
    st.title('INVERSIONES SEGÚN LA ETAPA DE AVANCE DEL PROYECTO')
    st.write("    ")
    st.markdown("<div style='text-align: justify'>Según la etapa de avance, 5 proyectos se encuentran en etapa de construcción con un monto de inversión conjunta de US$ 8,501 millones, lo cual representa el 15% de la inversión global de la Cartera. De este grupo destaca Mina Justa el cual inició construcción en 2018 y estaría iniciando operación en el primer semestre del 2021; posteriormente, los proyectos Ampliación Santa María (US$ 121 millones), Ampliación Toromocho (US$ 1,355 millones) y Quellaveco (US$ 5,300 millones), tienen inicios de construcción programados para el 2022.</div>", unsafe_allow_html=True)
    st.write("    ")
    st.markdown("<div style='text-align: justify'>Por otro lado, es importante precisar que Relaves B2 y Quecher Main, proyectos considerados en la edición 2019, culminaron la etapa de construcción en el cuarto trimestre de 2019, motivo por el cual ya no son considerados en la presente edición. Respecto a los proyectos que se encuentran en la etapa de Ingeniería de Detalle, la presente Cartera contempla 4 con una inversión conjunta de US$ 4,219 millones y representando el 7% de la inversión total, y estos son: Yanacocha Sulfuros (US$ 2,100 millones), Tía María (US$ 1,400 millones), Corani (US$ 579 millones) y Ampliación Shouxin (US$ 140 millones. De los proyectos descritos, resalta Yanacocha Sulfuros debido a la gestión realizada por su titular Minera Yanacocha S.R.L., lo cual le permitió avanzar dos etapas (pasó de pre-factibilidad a ingeniería de detalle).</div>", unsafe_allow_html=True)
    st.write("    ")
    link='<iframe width="1250" height="800" src="https://app.powerbi.com/view?r=eyJrIjoiMDBhMDc0ODQtYjM3Ny00MDUzLWJkZmUtM2I0N2ExNWYxZDU5IiwidCI6IjcyODk0ODA3LTJhMzctNDExNC1hZjVlLTU3MDU1ZTljNmQ5NCJ9&pageName=ReportSection939bdcc4073db9515b93" frameborder="0" allowFullScreen="true"></iframe>'
    components.html(link,width=1250, height=800)
    st.write("    ")
    st.markdown("<div style='text-align: justify'>Por su parte, en la etapa de factibilidad se encuentran 17 proyectos con una inversión conjunta de US$ 16,590 millones lo cual representa el 30% de la inversión total. Finalmente, en la etapa de prefactibilidad se concentran la mayor cantidad de proyectos, en total 20 proyectos, con una inversión conjunta estimada en US$ 26,847 millones, representando el 48% de la inversión total en Cartera.</div>", unsafe_allow_html=True)