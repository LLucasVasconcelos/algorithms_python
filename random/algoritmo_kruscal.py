# --- ALGORITMO DE KRUSKAL (Rede de Transporte Metropolitano) ---

# 1. Conjunto de Arestas E conforme especificação
arestas = [
    ('a', 'b', 4), ('a', 'c', 3), ('a', 'd', 6), ('a', 'e', 7),
    ('b', 'c', 2), ('b', 'd', 4), ('b', 'f', 9), ('b', 'e', 5),
    ('c', 'd', 3), ('c', 'e', 4), ('c', 'h', 8),
    ('d', 'e', 5), ('e', 'f', 6),
    ('f', 'g', 5), ('f', 'h', 7), ('f', 'i', 6),
    ('g', 'h', 2), ('g', 'n', 9),
    ('h', 'i', 3), ('h', 'm', 4),
    ('i', 'j', 7),
    ('j', 'k', 6), ('k', 'l', 3), ('l', 'm', 4),
    ('m', 'n', 5), ('n', 'j', 8),
    ('j', 'l', 5), ('k', 'm', 7), ('l', 'n', 6)
]


arestas_ordenadas = sorted(arestas, key=lambda x: (x[2], x[0], x[1]))

print("--- LISTA DE ARESTAS ORDENADA ---")
for e in arestas_ordenadas:
    print(f"Aresta {e[0]}-{e[1]}: Custo {e[2]}")
print("-" * 30)

# 2. ESTRUTURA DISJOINT SET UNION (DSU)
parent = {v: v for v in "abcdefghijklmn"}

def find(i):
    if parent[i] == i:
        return i
    parent[i] = find(parent[i]) 
    return parent[i]

def union(i, j):
    root_i = find(i)
    root_j = find(j)
    if root_i != root_j:
        parent[root_i] = root_j
        return True
    return False


mst = []
custo_total = 0


for u, v, peso in arestas_ordenadas:
    # O "Find" decide se a aresta entra (se raízes são diferentes)
    if find(u) != find(v):
        union(u, v)
        mst.append((u, v, peso))
        custo_total += peso
        
        # Agrupando componentes para visualização
        componentes = {}
        for nodo in parent:
            root = find(nodo)
            if root not in componentes:
                componentes[root] = []
            componentes[root].append(nodo)
            
        print(f"Adicionada: {u}-{v} ({peso}) | Componentes atuais: {list(componentes.values())}")
    else:
        continue

print("\n" + "="*40)
print("CONJUNTO FINAL DE ARESTAS DA MST:")
for u, v, w in mst:
    print(f"  ({u}, {v}) [Peso: {w}]")

print(f"\nCUSTO TOTAL DA MST: {custo_total}")
print("="*40)