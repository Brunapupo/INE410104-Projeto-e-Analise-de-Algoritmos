mapa_grafo = {
    'c1':  [('c2', 15), ('c4',  8)],
    'c2':  [('c1', 15), ('c3', 12), ('c10', 30)],
    'c3':  [('c2', 12)],
    'c4':  [('c1',  8), ('c5', 10), ('c6',  7)],
    'c5':  [('c4', 10), ('c8', 18)],
    'c6':  [('c4',  7)],
    'c7':  [('c9', 14), ('c12', 20)],
    'c8':  [('c5', 18)],
    'c9':  [('c7', 14)],
    'c10': [('c2', 30), ('c11',  9)],
    'c11': [('c10', 9), ('c12', 11)],
    'c12': [('c11', 11), ('c7', 20)]
}

pedagio = {
    'c1': 4.80,
    'c2': 6.50,
    'c3': 5.10,
    'c4': 3.90,
    'c5': 4.20,
    'c6': 3.50,
    'c7': 7.00,
    'c8': 4.10,
    'c9': 6.80,
    'c10': 5.60,
    'c11': 6.10,
    'c12': 7.30
}

def dijkstra_basico(
    mapa_grafo,
    pedagio,
    preco_combustivel,
    origem,
    destino,
    autonomia_km_litro,
):
    distancia = {vertice: float('inf') for vertice in mapa_grafo}   # Dv ← ∞
    anterior  = {vertice: None     for vertice in mapa_grafo}   # Av ← null
    ancestralDiretoVisitado  = {vertice: False    for vertice in mapa_grafo}   # Cv ← false
    distancia[origem] = 0.0                                     # Ds ← 0

    while True:

        u = None
        menorDistancia = float('inf')
        for vertice in mapa_grafo:
            if (not ancestralDiretoVisitado[vertice]) and (distancia[vertice] < menorDistancia):
                menorDistancia = distancia[vertice]
                u = vertice

        # se não existe mais vértice não ancestralDiretoVisitado, encerra o laço
        if u is None:
            break

        ancestralDiretoVisitado[u] = True     # Cu ← true

        # foreach vizinho ∈ N(u) : Cv = falso do
        for vizinho, km in mapa_grafo.get(u, []):
            if not ancestralDiretoVisitado[vizinho]:
                custo_uv = (
                    km / autonomia_km_litro * preco_combustivel
                    + pedagio.get(vizinho, 0.0)
                )
                novo_custo = distancia[u] + custo_uv
                if novo_custo < distancia[vizinho]:
                    distancia[vizinho] = novo_custo
                    anterior[vizinho]  = u

    # reconstrução do caminho ótimo
    caminho = []
    vertice = destino
    while vertice is not None:
        caminho.append(vertice)
        vertice = anterior[vertice]
    #inverte a ordem dos elementos da lista/caminho. No algoritmo a reconstrução da rota, começa do dentido e vai voltando até a origem.
    caminho.reverse() 
    
    return caminho, distancia[destino]

origem = input("Digite a localidade de origem (ex: c3): ")
destino = input("Digite a localidade de destino (ex: c11): ")
preco_combustivel = float(input("Digite o preço do combustível (R$/L): "))
autonomia_km_litro = float(input("Digite a autonomia do veículo (km/L): "))


caminho, custo_total = dijkstra_basico(
    mapa_grafo=mapa_grafo,
    pedagio=pedagio,
    preco_combustivel=preco_combustivel,
    origem=origem,
    destino=destino,
    autonomia_km_litro=autonomia_km_litro,
)

if caminho:
    print("Rota de menor custo:", " → ".join(caminho))
    print(f"Custo total da viagem: R$ {custo_total:.2f}")
else:
    print("Não há rota possível entre as localidades fornecidas.")
