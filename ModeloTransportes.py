import streamlit as st
import numpy as np
import pandas as pd

# Datos del problema
costos = np.array([
    [23, 30, 28, 30],
    [23, 30, 28, 30],
    [30, 25, 28, 10]
])
oferta = np.array([8000, 7000, 5000])
demanda = np.array([4000, 3000, 2500, 2500])

# Convertir a DataFrame para visualización
costos_df = pd.DataFrame(costos, columns=["Hospital Pediátrico 'Baca Ortiz'", "Hospital Carlos Andrade Marín", "Hospital Militar", "Hospital de Especialidades Eugenio Espejo"],
                         index=["MAQUIPHARMA S.A.", "DISTRIBUIDORA DISFASUR", "FARMAENLACE"])

def metodo_de_la_esquina_noroeste():
    st.subheader("Método de la Esquina Noroeste")
    st.write("Inicializamos con la oferta y demanda, y comenzamos desde la esquina noroeste de la matriz.")

    # Inicializar la matriz de transporte
    asignacion = np.zeros(costos.shape)
    oferta_temp = oferta.copy()
    demanda_temp = demanda.copy()

    i = 0
    j = 0
    pasos = []

    while i < len(oferta) and j < len(demanda):
        asignar = min(oferta_temp[i], demanda_temp[j])
        asignacion[i, j] = asignar
        oferta_temp[i] -= asignar
        demanda_temp[j] -= asignar

        pasos.append((i, j, asignar, oferta_temp.copy(), demanda_temp.copy(), asignacion.copy()))

        if oferta_temp[i] == 0:
            i += 1
        if demanda_temp[j] == 0:
            j += 1

    for paso, (i, j, asignar, oferta_temp, demanda_temp, asignacion) in enumerate(pasos, 1):
        st.write(f"**Paso {paso}:** Asignar {asignar} unidades desde {costos_df.index[i]} hasta {costos_df.columns[j]}")
        st.write(f"Oferta restante: {oferta_temp}")
        st.write(f"Demanda restante: {demanda_temp}")
        st.write("Matriz de asignación actual:")
        asignacion_df = pd.DataFrame(asignacion, columns=costos_df.columns, index=costos_df.index)
        st.write(asignacion_df)

    costo_total = np.sum(asignacion * costos)
    st.write(f"Costo total: ${costo_total}")

def vogel():
    st.subheader("Método de Aproximación de Vogel")
    st.write("Calculamos las penalizaciones y hacemos asignaciones sucesivas.")

    # Inicializar la matriz de transporte
    asignacion = np.zeros_like(costos, dtype=float)
    oferta_temp = oferta.copy()
    demanda_temp = demanda.copy()
    costos_temp = costos.astype(float)  # Asegúrate de que los costos son de tipo float para manejar grandes valores.

    # Máscaras para indicar si una fila o columna está activa
    fila_activa = np.ones(len(oferta), dtype=bool)
    columna_activa = np.ones(len(demanda), dtype=bool)
    pasos = []

    while fila_activa.any() and columna_activa.any():
        # Calcular penalizaciones para filas y columnas activas
        row_penalties = np.array([sorted(row[row != np.inf])[:2] if len(row[row != np.inf]) > 1 else [0, 0] for row in costos_temp])
        row_penalties = np.array([row[1] - row[0] if row[1] != 0 else 0 for row in row_penalties])
        col_penalties = np.array([sorted(col[col != np.inf])[:2] if len(col[col != np.inf]) > 1 else [0, 0] for col in costos_temp.T])
        col_penalties = np.array([col[1] - col[0] if col[1] != 0 else 0 for col in col_penalties])

        # Encontrar la penalización máxima
        if row_penalties.max() >= col_penalties.max():
            row_idx = np.argmax(row_penalties)
            col_idx = np.argmin(costos_temp[row_idx])
        else:
            col_idx = np.argmax(col_penalties)
            row_idx = np.argmin(costos_temp[:, col_idx])

        # Asignar tanto como sea posible
        asignar = min(oferta_temp[row_idx], demanda_temp[col_idx])
        asignacion[row_idx, col_idx] = asignar
        oferta_temp[row_idx] -= asignar
        demanda_temp[col_idx] -= asignar

        pasos.append((row_idx, col_idx, asignar, oferta_temp.copy(), demanda_temp.copy(), asignacion.copy(), costos_temp.copy()))

        # Actualizar estado de filas y columnas
        if oferta_temp[row_idx] == 0:
            fila_activa[row_idx] = False
            costos_temp[row_idx, :] = np.inf  # Solo marca la fila como inactiva
        if demanda_temp[col_idx] == 0:
            columna_activa[col_idx] = False
            costos_temp[:, col_idx] = np.inf  # Solo marca la columna como inactiva

    for paso, (row_idx, col_idx, asignar, oferta_temp, demanda_temp, asignacion, costos_temp) in enumerate(pasos, 1):
        st.write(f"**Paso {paso}:** Asignar {asignar} unidades desde {costos_df.index[row_idx]} hasta {costos_df.columns[col_idx]}")
        st.write(f"Oferta restante: {oferta_temp}")
        st.write(f"Demanda restante: {demanda_temp}")
        st.write("Matriz de asignación actual:")
        asignacion_df = pd.DataFrame(asignacion, columns=costos_df.columns, index=costos_df.index)
        st.write(asignacion_df)
        st.write("Matriz de costos actualizada:")
        st.write(pd.DataFrame(costos_temp, columns=costos_df.columns, index=costos_df.index))

    costo_total = np.sum(asignacion * costos)
    st.write(f"Costo total: ${costo_total}")

def minimizar_costos():
    st.subheader("Minimización de Costos")
    st.write("Seleccione un método para minimizar los costos de transporte:")
    metodo = st.selectbox("Método", ["Método de la Esquina Noroeste", "Método de Aproximación de Vogel"])

    if metodo == "Método de la Esquina Noroeste":
        metodo_de_la_esquina_noroeste()
    elif metodo == "Método de Aproximación de Vogel":
        vogel()

