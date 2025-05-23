import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    taxa_chegada = parser.add_argument('--taxa_chegada', type=float, help='..')
    taxa_atendimento = parser.add_argument('--taxa_atendimento', type=float, help='..')
    n_unidades = parser.add_argument('--n_unidades', type=int, help='..')
    pass