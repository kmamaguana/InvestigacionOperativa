import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt

# Crear el grafo dirigido
G = nx.DiGraph()

# Añadir los nodos (distribuidores y hospitales)
nodos = [
    'MAQUIPHARMA S.A.', 'DISTRIBUIDORA DISFASUR', 'FARMAENLACE',
    'Hospital Pediátrico "Baca Ortiz"', 'Hospital Carlos Andrade Marín',
    'Hospital Militar', 'Hospital de Especialidades Eugenio Espejo',
    'Av. América1', 'Av. América2', 'Av. Cristóbal Colón', '18 de Septiembre1',
    '18 de Septiembre2', 'Av. Patria', 'Av. Universitaria', 'Av. Amazonas',
    'Av. 10 de Agosto', 'Av. La Prensa', 'Bolivia', 'Av. Portugal', 'Av. 6 de Diciembre',
    'Av. Gran Colombia', 'Av. Francisco de Orellana', 'Av. Perez Guerrero', 'Yaguachi',
    'Bantec', 'Luis Sodiro'
]

nodosD = [
    'MAQUIPHARMA S.A.', 'DISTRIBUIDORA DISFASUR', 'FARMAENLACE'
]

nodosH = [
    'Hospital Pediátrico "Baca Ortiz"', 'Hospital Carlos Andrade Marín',
    'Hospital Militar', 'Hospital de Especialidades Eugenio Espejo'
]

# Añadir las aristas con distancia y costos
aristas = [
    ('MAQUIPHARMA S.A.', 'Av. América1', {'distance': 200, 'cost': 8, 'capacity': 100}),
                        ('Av. América1', 'Av. Cristóbal Colón', {'distance': 200, 'cost': 12, 'capacity': 100}),
                                        ('Av. Cristóbal Colón', 'Hospital Pediátrico "Baca Ortiz"', {'distance': 1700, 'cost': 23, 'capacity': 100}),
                        ('Av. América1', 'Av. Patria', {'distance': 290, 'cost': 18, 'capacity': 100}),
                                        ('Av. Patria', 'Hospital Militar', {'distance': 9000, 'cost': 28, 'capacity': 100}),
                        ('Av. América1', 'Av. Universitaria', {'distance': 700, 'cost': 15, 'capacity': 100}),
                                        ('Av. Universitaria', '18 de Septiembre1', {'distance': 50, 'cost': 7, 'capacity': 100}),
                                                             ('18 de Septiembre1', 'Hospital Carlos Andrade Marín', {'distance': 50, 'cost': 18, 'capacity': 100}),
                                        ('Av. Universitaria', 'Hospital Carlos Andrade Marín', {'distance': 700, 'cost': 30, 'capacity': 100}),
    ('DISTRIBUIDORA DISFASUR', 'Av. La Prensa', {'distance': 600, 'cost': 10, 'capacity': 100}),
                              ('Av. La Prensa', 'Av. 10 de Agosto', {'distance': 3300, 'cost': 25, 'capacity': 100}),
                                               ('Av. 10 de Agosto', 'Av. Francisco de Orellana', {'distance': 3100, 'cost': 28, 'capacity': 100}),
                                                                   ('Av. Francisco de Orellana', 'Av. Amazonas',{'distance': 600, 'cost': 12, 'capacity': 100}),
                                                                                                ('Av. Amazonas', 'Av. Cristóbal Colón', {'distance': 900, 'cost': 12, 'capacity': 100}),
                              ('Av. La Prensa', 'Av. América2', {'distance': 3000, 'cost': 20, 'capacity': 100}),
                                               ('Av. América2', 'Av. Universitaria', {'distance': 4300, 'cost': 22, 'capacity': 100}),
                                               ('Av. América2', 'Av. Patria', {'distance': 4900, 'cost': 30, 'capacity': 100}),
                                                               ('Av. Patria','Av. Gran Colombia', {'distance': 900, 'cost': 19, 'capacity': 100}),
                                                                            ('Av. Gran Colombia', 'Luis Sodiro', {'distance': 200, 'cost': 13, 'capacity': 100}),
                                                                                                 ('Luis Sodiro', 'Hospital de Especialidades Eugenio Espejo', {'distance': 300, 'cost': 16, 'capacity': 100}),
                                                                            ('Av. Gran Colombia', 'Hospital de Especialidades Eugenio Espejo', {'distance': 500, 'cost': 22, 'capacity': 100}),
                                                                            ('Av. Gran Colombia', 'Yaguachi', {'distance': 500, 'cost': 11, 'capacity': 100}),
                                                                                                 ('Yaguachi', 'Bantec', {'distance': 110, 'cost': 7, 'capacity': 100}),
                                                                                                             ('Bantec', 'Hospital de Especialidades Eugenio Espejo', {'distance': 50, 'cost': 10, 'capacity': 100}),
    ('FARMAENLACE', 'Av. Portugal', {'distance': 750, 'cost': 9, 'capacity': 100}),
                   ('Av. Portugal', 'Av. 6 de Diciembre', {'distance': 900, 'cost': 18, 'capacity': 100}),
                                   ('Av. 6 de Diciembre', 'Av. Gran Colombia', {'distance': 710, 'cost': 14, 'capacity': 100}),
                   ('Av. Portugal', 'Bolivia', {'distance': 3900, 'cost': 15, 'capacity': 100}),
                                   ('Bolivia', '18 de Septiembre2', {'distance': 130, 'cost': 14, 'capacity': 100}),
                                              ('18 de Septiembre2', 'Hospital Carlos Andrade Marín', {'distance': 100, 'cost': 23, 'capacity': 100}),
                                   ('Bolivia', 'Av. Perez Guerrero', {'distance': 1000, 'cost': 12, 'capacity': 100}),
                                              ('Av. Perez Guerrero', 'Hospital Militar', {'distance': 290, 'cost': 25, 'capacity': 100}),
]

G.add_edges_from((u, v, attr) for u, v, attr in aristas)

# Posiciones aproximadas para visualización (opcional)
pos = {
    'MAQUIPHARMA S.A.': (-3.5, 3.5),
    'DISTRIBUIDORA DISFASUR': (-3.5, 1),
    'FARMAENLACE': (-3.5, -1),

    'Av. América1': (-2.5, 3),
    'Av. La Prensa': (-2.5, 1.5),
    'Av. Portugal': (-2.5, -0.5),

    'Av. 10 de Agosto': (-1.75,2),
    'Av. América2': (-1.75,0.75),

    'Bolivia': (-1.5, 0),
    'Av. 6 de Diciembre': (-1.5, -2),

    'Av. Universitaria': (-0.5, 2),

    'Av. Gran Colombia': (-0.5, -1.3),

    'Av. Cristóbal Colón': (1.75,4),
    '18 de Septiembre1': (-0.2, 3),
    'Av. Patria': (1.50, 2),
    '18 de Septiembre2': (1, 1),
    'Av. Francisco de Orellana': (1.4, 0.5),
    'Av. Perez Guerrero': (1, -0.2),
    'Yaguachi': (1, -1),

    'Av. Amazonas': (2.5, 2.80),
    'Bantec': (2.5, -1),
    'Luis Sodiro': (2, -2),

    'Hospital Pediátrico "Baca Ortiz"': (4, 3),
    'Hospital Carlos Andrade Marín': (4, 1.5),
    'Hospital Militar': (4, -0.5),
    'Hospital de Especialidades Eugenio Espejo': (4, -2),
}


def draw_graph(G, path=[], title="Grafo"):
    plt.figure(figsize=(14, 8))
    color_map = ['red' if node in path else 'lightblue' for node in G.nodes()]
    edge_color_map = ['red' if (u, v) in path or (v, u) in path else 'black' for u, v in G.edges()]
    weights = nx.get_edge_attributes(G, 'cost')
    nx.draw(G, pos, node_color=color_map, edge_color=edge_color_map, with_labels=True, node_size=500, arrowsize=20)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=weights)
    plt.title(title)
    st.pyplot(plt)

def mostrar_ruta_mas_corta():
    st.subheader("Ruta Más Corta")
    source = st.selectbox("Seleccione el nodo de origen:", nodosD)
    target = st.selectbox("Seleccione el nodo de destino:", nodosH)
    criterio = st.selectbox("Seleccione el criterio:", ["distance", "cost"])

    if source and target and criterio:
        try:
            path = nx.shortest_path(G, source=source, target=target, weight=criterio)
            path_cost = nx.shortest_path_length(G, source=source, target=target, weight=criterio)
            st.write(f"La ruta más corta desde {source} hasta {target} según {criterio} es: {path} con un costo de {path_cost}")

            # Proceso paso a paso
            st.write("### Proceso paso a paso:")
            total_cost = 0
            for i in range(len(path) - 1):
                u, v = path[i], path[i + 1]
                edge_cost = G[u][v][criterio]
                total_cost += edge_cost
                st.write(f"De {u} a {v}: {criterio} = {edge_cost}, {criterio} acumulado = {total_cost}")
            st.write(f"Resultado final: {total_cost}")
            draw_graph(G, path=path, title=f'Ruta más corta ({criterio})')

        except nx.NetworkXNoPath:
            st.error(f"No existe una ruta desde {source} hasta {target} según {criterio}.")

def flujo_maximo():
    st.subheader("Flujo Máximo")
    source = st.selectbox("Seleccione el nodo de origen:", nodosD)
    target = st.selectbox("Seleccione el nodo de destino:", nodosH)
    capacidad = st.selectbox("Seleccione la variable:", ["distance", "cost"])

    if source and target and capacidad:
        # Convertir los atributos seleccionados como capacidad
        for u, v, d in G.edges(data=True):
            d['capacity'] = d[capacidad]

        flow_value, flow_dict = nx.maximum_flow(G, source, target, capacity='capacity', flow_func=nx.algorithms.flow.edmonds_karp)
        st.write(f"Flujo máximo desde {source} hasta {target} según {capacidad}: {flow_value}")

        # Mostrar el flujo a través de las aristas
        edge_flow = [(u, v) for u, v in G.edges() if flow_dict[u][v] > 0]
        fig, ax = plt.subplots(figsize=(14, 8))
        nx.draw(G, pos, with_labels=True, node_size=500, node_color='lightblue', edge_color='black', arrowsize=20, ax=ax)
        nx.draw_networkx_edges(G, pos, edgelist=edge_flow, edge_color='red', width=2, ax=ax)
        plt.title(f"Flujo Máximo desde {source} hasta {target} según {capacidad}")
        st.pyplot(fig)

def arbol_de_expansion():
    st.subheader("Árbol de Expansión Mínima")
    criterio = st.selectbox("Seleccione el criterio:", ["distance", "cost"])

    if criterio:
        mst = nx.minimum_spanning_tree(G.to_undirected(), weight=criterio)

        # Calcular el peso total del árbol de expansión mínima
        total_weight = sum(d[criterio] for u, v, d in mst.edges(data=True))

        fig, ax = plt.subplots(figsize=(14, 8))
        nx.draw(mst, pos, with_labels=True, node_size=700, node_color='lightgreen', arrows=True, edge_color='green', ax=ax)
        edge_labels = {(u, v): f"{d[criterio]}" for u, v, d in mst.edges(data=True)}
        nx.draw_networkx_edge_labels(mst, pos, edge_labels=edge_labels, ax=ax)

        plt.title(f"Árbol de Expansión Mínima ({criterio})")
        st.pyplot(fig)

        st.write(f"Peso total del árbol de expansión mínima según {criterio}: {total_weight}")

"""
def flujo_de_costo_minimo():
    st.subheader("Flujo de Costo Mínimo")
    source = st.selectbox("Seleccione el nodo de origen:", nodosD)
    target = st.selectbox("Seleccione el nodo de destino:", nodosH)

    if source and target:
        cost, flow_dict = nx.network_simplex(G)

        st.write(f"Flujo de costo mínimo desde {source} hasta {target}: {cost}")

        # Mostrar el flujo a través de las aristas
        edge_flow = [(u, v) for u, v in G.edges() if flow_dict[u][v] > 0]
        fig, ax = plt.subplots(figsize=(14, 8))
        nx.draw(G, pos, with_labels=True, node_size=500, node_color='lightblue', edge_color='black', arrowsize=20, ax=ax)
        nx.draw_networkx_edges(G, pos, edgelist=edge_flow, edge_color='red', width=2, ax=ax)
        plt.title(f"Flujo de Costo Mínimo desde {source} hasta {target}")
        st.pyplot(fig)
"""
