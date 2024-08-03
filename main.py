import streamlit as st
from ModeloRedes import mostrar_ruta_mas_corta, flujo_maximo, arbol_de_expansion
from ModeloTransportes import vogel, metodo_de_la_esquina_noroeste, minimizar_costos

def modelo_de_redes():
    st.header("Modelo de Redes")
    sub_option = st.selectbox("Seleccione una operación", ["Ruta más corta", "Flujo máximo", "Árbol de expansión"])

    if sub_option == "Ruta más corta":
        mostrar_ruta_mas_corta()
    elif sub_option == "Flujo máximo":
        flujo_maximo()
    elif sub_option == "Árbol de expansión":
        arbol_de_expansion()


def metodo_de_transporte():
    st.header("Método de Transporte")
    method = st.selectbox("Seleccione un método", ["Vogel", "Esquina Noroeste", "Minimizar Costos"])

    if method == "Vogel":
        vogel()
    elif method == "Esquina Noroeste":
        metodo_de_la_esquina_noroeste()
    elif method == "Minimizar Costos":
        minimizar_costos()

def main():
    # Título principal
    st.title("Análisis de Redes y Métodos de Transporte")

    # Información de presentación en el sidebar
    with st.sidebar:
        st.subheader("Investigación Operativa")
        st.write("Curso: SIS8-002")
        st.write("Profesor: Ing. David Galeas")

        # Mostrar la lista de integrantes
        st.markdown("### Integrantes:")
        integrantes = """
        - Karen Amaguaña
        - Cristian Caiza
        - Jefferson Diaz
        - Christian Iza
        - Silvia Janeta
        - Erick Olalla
        - Jorge Sanchez
        - Andy Sisalema
        """
        st.markdown(integrantes)

        # Opciones del sidebar
        option = st.selectbox("Elija una opción", ["Modelo de Redes", "Método de Transporte"])

    # Llamada a las funciones según la opción seleccionada
    if option == "Modelo de Redes":
        modelo_de_redes()
    elif option == "Método de Transporte":
        metodo_de_transporte()

if __name__ == "__main__":
    main()

