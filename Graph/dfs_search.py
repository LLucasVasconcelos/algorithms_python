from collections import deque

def get_grafo():
    return {
        'a': ['b', 'c', 'd', 'e'],
        'b': ['c', 'd', 'f', 'e'],
        'c': ['d', 'e', 'h'],
        'd': ['e'],
        'e': ['f'],
        'f': ['g', 'h', 'i'],
        'g': ['h', 'n'],
        'h': ['i', 'm'],
        'i': ['j'],
        'j': ['k', 'l'],
        'k': ['l', 'm'],
        'l': ['m', 'n'],
        'm': ['n'],
        'n': ['j']
    }

def bfs(grafo, inicio, destino):
    fila = deque([(inicio, [inicio], [])]) 
    visitados = {inicio}
    passos_fila = []

    while fila:
        passos_fila.append(list(n[0] for n in fila)) 
        u, caminho_v, arestas = fila.popleft()

        if u == destino:
            return arestas, passos_fila

        for vizinho in sorted(grafo.get(u, [])):
            if vizinho not in visitados:
                visitados.add(vizinho)
                fila.append((vizinho, caminho_v + [vizinho], arestas + [(u, vizinho)]))
    return None

def dfs(grafo, u, destino, visitados=None, arestas=None, pilha_registro=None):
    if visitados is None:
        visitados = set()
    if arestas is None:
        arestas = []
    if pilha_registro is None:
        pilha_registro = []

    visitados.add(u)
    pilha_registro.append(u) # Simulação da pilha de chamada

    if u == destino:
        return arestas, pilha_registro

    # Ordem alfabética para consistência
    for vizinho in sorted(grafo.get(u, [])):
        if vizinho not in visitados:
            resultado = dfs(grafo, vizinho, destino, visitados, arestas + [(u, vizinho)], pilha_registro)
            if resultado:
                return resultado
    
    return None


grafo = get_grafo()

# BFS
arestas_bfs, fila_total = bfs(grafo, 'a', 'l')
print("=== (BFS) ===")
print(f"arestas: {arestas_bfs}")
print(f"Último estado da Fila: {fila_total[-1]}")
print(f"Distância (arestas): {len(arestas_bfs)}\n")

# DFS
arestas_dfs, pilha_total = dfs(grafo, 'a', 'l')
print("=== (DFS) ===")
print(f"arestas: {arestas_dfs}")
print(f"Pilha de visitação (Caminho): {pilha_total}")
print(f"Distância (arestas): {len(arestas_dfs)}")