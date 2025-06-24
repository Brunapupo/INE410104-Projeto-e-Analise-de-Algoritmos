from collections import deque

entregas = {
    'c1':  ['c2', 'c4'],
    'c2':  ['c1', 'c3', 'c10'],     
    'c3':  ['c2'],
    'c4':  ['c1', 'c5', 'c6'],
    'c5':  ['c4', 'c8'],
    'c6':  ['c4'],
    'c7':  ['c9', 'c12'],         
    'c8':  ['c5'],
    'c9':  ['c7'],                 
    'c10': ['c2', 'c11'],       
    'c11': ['c10', 'c12'],
    'c12': ['c11', 'c7']
}

idCentrais = set()
for central, vizinhos in entregas.items():
    idCentrais.add(central)
    for vizinha in vizinhos:
        idCentrais.add(vizinha)

def BuscaEmLargura(entregas, idCentrais, origem, destino):
   
    ConteudoNaFila = {v: False for v in idCentrais}         
    DistanciaAresta = {v: float('inf') for v in idCentrais}  
    AncestralDireto = {v: None for v in idCentrais}          
    ConteudoNaFila[origem] = True
    DistanciaAresta[origem] = 0
    EliminaDaFila = deque()
    EliminaDaFila.append(origem)

    while EliminaDaFila:
        u = EliminaDaFila.popleft()

        for v in entregas.get(u, []):
            if not ConteudoNaFila[v]:
                ConteudoNaFila[v] = True
                DistanciaAresta[v] = DistanciaAresta[u] + 1
                AncestralDireto[v] = u
                EliminaDaFila.append(v)

  
    if AncestralDireto[destino] is None and origem != destino:
        return None  

    caminho = []
    atual = destino
    while atual is not None:
        caminho.append(atual)
        atual = AncestralDireto[atual]
    caminho.reverse()

    return caminho

origem = input("Digite a central de origem (ex: c1, c2, c3...): ")
destino = input("Digite a central de destino (ex: c1, c2, c3...): ")

caminho = BuscaEmLargura(entregas, idCentrais, origem, destino)

if caminho:
    print("Caminho mais curto:", caminho)
else:
    print("Não há caminho possível entre as centrais fornecidas.")
