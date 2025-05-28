# Importa a biblioteca heapq que fornece uma implementação de fila de prioridade baseada em heap
import heapq

# Função que implementa o algoritmo de Dijkstra
def dijkstra(grafo, origem):
    # Inicializa todas as distâncias como infinito
    distancias = {vertice: float('infinity') for vertice in grafo}
    # A distância até a origem é zero
    distancias[origem] = 0
    # Fila de prioridade iniciada com a origem e distância 0
    fila_prioridade = [(0, origem)]

    # Enquanto houver vértices na fila de prioridade
    while fila_prioridade:
        # Remove o vértice com menor distância atual
        distancia_atual, vertice_atual = heapq.heappop(fila_prioridade)
        
        # Para cada vizinho do vértice atual
        for vizinho, peso in grafo[vertice_atual].items():
            # Calcula a nova distância até o vizinho
            nova_distancia = distancia_atual + peso
            
            # Se a nova distância for menor que a já registrada
            if nova_distancia < distancias[vizinho]:
                # Atualiza a distância
                distancias[vizinho] = nova_distancia
                # Insere o vizinho na fila de prioridade com a nova distância
                heapq.heappush(fila_prioridade, (nova_distancia, vizinho))

    # Retorna o dicionário com as menores distâncias a partir da origem
    return distancias

# Definição do grafo como um dicionário de dicionários, onde:
# a chave é o vértice e o valor é outro dicionário com vizinhos e pesos das arestas
grafo = {
    "A": {"B": 4, "C": 2},
    "B": {"A": 4, "C": 1, "D": 5},
    "C": {"A": 2, "B": 1, "D": 8, "E": 10},
    "D": {"B": 5, "C": 8, "E": 2, "F": 6},
    "E": {"C": 10, "D": 2, "F": 3},
    "F": {"D": 6, "E": 3}
}

# Mostra ao usuário os pontos disponíveis no grafo
print("Pontos disponíveis no grafo:", list(grafo.keys()))

# Solicita ao usuário que informe o ponto de origem
origem = input("Digite o ponto de origem: ").strip().upper()

# Verifica se a origem informada é válida
if origem not in grafo:
    # Se não for válida, exibe uma mensagem de erro
    print("Ponto de origem inválido! Por favor, escolha um dos pontos disponíveis.")
else:
    # Se for válida, executa o algoritmo de Dijkstra
    resultado = dijkstra(grafo, origem)
    # Exibe as distâncias mínimas a partir da origem
    print(f"Distâncias mínimas a partir de {origem}:", resultado)
