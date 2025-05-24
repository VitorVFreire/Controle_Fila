import argparse

def po(taxa_chegada: float, taxa_atendimento:float) -> float:
    return 1 - (taxa_chegada / taxa_atendimento)

def pn(po:float, taxa_chegada:float, taxa_atendimento:float, n_unidades:int) -> float:
    return po * ((taxa_chegada/taxa_atendimento) ** n_unidades)

def taxa_utilizacao(taxa_chegada:float, taxa_atendimento:float) -> float:
    return taxa_chegada * taxa_atendimento

def probabilidade(taxa_chegada:float, taxa_atendimento:float, target:int) -> float:
    return 1 * ((taxa_chegada / taxa_atendimento) ** (target+1))

def media_clientes_sistema(taxa_chegada:float, taxa_atendimento:float) -> float:
    return taxa_chegada / (taxa_atendimento - taxa_chegada)

def media_clientes_file(taxa_chegada:float, taxa_atendimento:float) -> float:
    return (taxa_chegada ** 2) / (taxa_atendimento * (taxa_atendimento - taxa_chegada))

def tempo_medio_permanencia(taxa_chegada:float, taxa_atendimento:float) -> float:
    return 1 / (taxa_atendimento - taxa_chegada)

def tempo_medio_fila(taxa_chegada:float, taxa_atendimento:float) -> float:
    return taxa_chegada / (taxa_atendimento * (taxa_atendimento-taxa_chegada))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    taxa_chegada = 1.0 #parser.add_argument('--taxa_chegada', type=float, help='..')
    taxa_atendimento = 3.0 #parser.add_argument('--taxa_atendimento', type=float, help='..')
    n_unidades = 3.0 #parser.add_argument('--n_unidades', type=int, help='..')
    target = 3.0 #parser.add_argument('--target', type=int, help='..')

    po = po(taxa_chegada, taxa_atendimento)
    pn = pn(po, taxa_chegada, taxa_atendimento, n_unidades)
    taxa_utilizacao = taxa_utilizacao(taxa_chegada, taxa_atendimento)
    probabilidade = probabilidade(taxa_chegada, taxa_atendimento, target)
    media_clientes_sistema = media_clientes_sistema(taxa_chegada, taxa_atendimento)
    media_clientes_file = media_clientes_file(taxa_chegada, taxa_atendimento)
    tempo_medio_permanencia = tempo_medio_permanencia(taxa_chegada, taxa_atendimento)
    tempo_medio_fila = tempo_medio_fila(taxa_chegada, taxa_atendimento)

    print(f'S: {taxa_utilizacao}\n P(0): {po}\nP(1): {pn}\nP(n=3): {probabilidade}')