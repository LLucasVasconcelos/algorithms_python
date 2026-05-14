grafo = {
    'a': [('b', 4), ('c', 3), ('d', 6), ('e', 7)],
    'b': [('a', 4), ('c', 2), ('d', 4), ('f', 9), ('e', 5)],
    'c': [('a', 3), ('b', 2), ('d', 3), ('e', 4), ('h', 8)],
    'd': [('a', 6), ('b', 4), ('c', 3), ('e', 5)],
    'e': [('a', 7), ('b', 5), ('c', 4), ('d', 5), ('f', 6)],
    'f': [('b', 9), ('e', 6), ('g', 5), ('h', 7), ('i', 6)],
    'g': [('f', 5), ('h', 2), ('n', 9)],
    'h': [('c', 8), ('f', 7), ('g', 2), ('i', 3), ('m', 4)],
    'i': [('f', 6), ('h', 3), ('j', 7)],
    'j': [('i', 7), ('k', 6), ('l', 5), ('n', 8)],
    'k': [('j', 6), ('l', 3), ('m', 7)],
    'l': [('j', 5), ('k', 3), ('m', 4), ('n', 6)],
    'm': [('h', 4), ('k', 7), ('l', 4), ('n', 5)],
    'n': [('g', 9), ('m', 5), ('j', 8), ('l', 6)]
}

# Inicialização
vertices_conectados = {'a'}
arestas_mst = []
custo_total = 0

# Fila de Prioridade Inicial (Arestas saindo de 'a')
fila_prioridade = [(4, 'a', 'b'), (3, 'a', 'c'), (6, 'a', 'd'), (7, 'a', 'e')]
fila_prioridade.sort() # Simula min-heap

print("Início do Algoritmo de Prim no vértice 'a':\n")

passo = 1
while len(vertices_conectados) < len(grafo):
    # 1. Escolher a aresta mínima candidata
    peso, u, v = fila_prioridade.pop(0)
    
    if v not in vertices_conectados:
        # 2. Registrar conexão
        arestas_mst.append((u, v, peso))
        vertices_conectados.add(v)
        custo_total += peso
        
        print(f"Passo {passo}:")
        print(f"  Vértices conectados: {sorted(list(vertices_conectados))}")
        print(f"  Aresta escolhida: ({u}, {v}) com peso {peso}")
        
        # 3. Atualizar Fila de Prioridade com novas arestas de 'v'
        for vizinho, p in grafo[v]:
            if vizinho not in vertices_conectados:
                fila_prioridade.append((p, v, vizinho))
        
        fila_prioridade.sort() # Re-ordena (Simulando comportamento da Heap)
        print(f"  Próximas candidatas (Heap): {fila_prioridade[:5]}...")
        print("-" * 50)
        passo += 1

print("\nRESULTADO FINAL:")
print(f"Árvore Geradora Mínima (MST): {arestas_mst}")
print(f"Custo total da rede: {custo_total}")