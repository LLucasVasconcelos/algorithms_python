"""Busca(G, s)
Seja T um grafo com V(T)={s} e E(T)=0
enquanto há arestas de G entre V(T) e V(G)\\V(T) faça
seja xy uma aresta com x (E de somatorio de calculo Sigma) V(T) e y (E de somatorio de calculo Sigma) V(G\\V(T)
      V(T) = V(T)U{y}
      E(T) = E(T)U{xy}
"""         

def busca_grafo(grafo, start_node, global_visited):
    v_t = [start_node]
    e_t =[]
    found_new_edge = True
    while found_new_edge:
        found_new_edge = False
        for x in v_t:
            for edge in grafo.get(x,[]):
                y = edge[1]
                if y not in v_t:
                    e_t.append(edge)
                    v_t.append(y)
                    global_visited.add(y)
                    found_new_edge = True
                    break     
            if found_new_edge:
                break
    return v_t,e_t
                
vertex_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n"] 

grafo = {
    "a":[("a","b"), ("a","c"), ("a","d"), ("a","e")],
    "b":[("b","c"), ("b","d"), ("b","e")],
    "c":[("c","d"), ("c","e")],
    "d":[("d","e"),],
    "e":[],
    "f":[("f","g"), ("f","h"), ("f","i")],
    "g":[("g","h"),],
    "h":[("h","i"),],
    "i":[],
    "j":[("j","k"),("j","l")],
    "k":[("k","l"),("k","m")],
    "l":[("l","m"),("l","n")],
    "m":[("m","n"),],
    "n":[("n","j"),],
}

globally_visited = set()
regions_count = 0
for v in vertex_list:
    if v not in globally_visited:
        regions_count +=1
        globally_visited.add(v)
        vt,et = busca_grafo(grafo,v,globally_visited)
        print(f"Região {regions_count} encontrada a partir de '{v}':")
        print(f"  Vértices: {vt}")
        print(f"  Arestas da Árvore T: {et}\n")
                                                                         
                                                                                                
                                                                                                