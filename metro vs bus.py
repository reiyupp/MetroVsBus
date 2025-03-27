import networkx as nx

# Grafo del Metro de Medellín
G_metro = nx.DiGraph()

# Estaciones del metro y tiempos de viaje (en minutos)
G_metro.add_edge('Itagüí', 'Envigado', weight=5)
G_metro.add_edge('Envigado', 'Ayura', weight=3)
G_metro.add_edge('Ayura', 'Aguacatala', weight=4)
G_metro.add_edge('Aguacatala', 'El Poblado', weight=3)
G_metro.add_edge('El Poblado', 'Itagüí', weight=10)  # Ejemplo de una estación de retorno


# Grafo de rutas de buses
G_buses = nx.DiGraph()

# Estaciones de buses y tiempos de viaje (en minutos)
G_buses.add_edge('Itagüí', 'Envigado', weight=10)  # Tiempo más largo por tráfico
G_buses.add_edge('Envigado', 'Ayura', weight=15)  # Tráfico pesado
G_buses.add_edge('Ayura', 'Aguacatala', weight=12)  # Tráfico moderado
G_buses.add_edge('Aguacatala', 'El Poblado', weight=20)  # Tráfico pesado
G_buses.add_edge('El Poblado', 'Itagüí', weight=18)  # Tráfico moderado

# Algunas rutas alternativas para buses
G_buses.add_edge('Itagüí', 'Ayura', weight=25)  # Ruta más larga en bus
G_buses.add_edge('Envigado', 'Aguacatala', weight=30)  # Ruta de bus en hora pico

# Función para obtener la mejor ruta en el metro
def obtener_mejor_ruta_metro(G, origen, destino):
    return nx.dijkstra_path(G, source=origen, target=destino, weight='weight')

# Ejemplo: mejor ruta en el metro de Itagüí a El Poblado
ruta_metro = obtener_mejor_ruta_metro(G_metro, 'Itagüí', 'El Poblado')
print("La mejor ruta en el metro de Itagüí a El Poblado es:", ruta_metro)

# Función para obtener la mejor ruta en el bus
def obtener_mejor_ruta_bus(G, origen, destino):
    return nx.dijkstra_path(G, source=origen, target=destino, weight='weight')

# Ejemplo: mejor ruta en bus de Itagüí a El Poblado
ruta_bus = obtener_mejor_ruta_bus(G_buses, 'Itagüí', 'El Poblado')
print("La mejor ruta en bus de Itagüí a El Poblado es:", ruta_bus)

# Calcular el tiempo total de viaje en el metro
tiempo_metro = sum(G_metro[u][v]['weight'] for u, v in zip(ruta_metro, ruta_metro[1:]))
print("Tiempo de viaje en el metro de Itagüí a El Poblado:", tiempo_metro, "minutos")

# Calcular el tiempo total de viaje en el bus
tiempo_bus = sum(G_buses[u][v]['weight'] for u, v in zip(ruta_bus, ruta_bus[1:]))
print("Tiempo de viaje en bus de Itagüí a El Poblado:", tiempo_bus, "minutos")

# Comparar los tiempos
if tiempo_metro < tiempo_bus:
    print("El metro es más rápido.")
else:
    print("El bus es más rápido.")


# import matplotlib.pyplot as plt

# # Visualización del grafo del metro
# nx.draw(G_metro, with_labels=True, node_color='lightblue', node_size=2000, font_size=10, font_weight='bold')
# plt.title("Grafo del Metro de Medellín")
# plt.show()

# # Visualización del grafo de las rutas de bus
# nx.draw(G_buses, with_labels=True, node_color='lightgreen', node_size=2000, font_size=10, font_weight='bold')
# plt.title("Grafo de las Rutas de Bus")
# plt.show()

