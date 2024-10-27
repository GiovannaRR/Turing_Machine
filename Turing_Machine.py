import json

def executar_maquina_turing(config, entrada, saida):

    with open(config, 'r') as arquivo_config:
        dados_maquina = json.load(arquivo_config)

    estado_atual = dados_maquina['initial']
    estados_aceitos = set(dados_maquina['final'])
    simbolo_em_branco = dados_maquina['white']
    tabela_transicoes = dados_maquina['transitions']

    transicoes_dict = {(trans['from'], trans['read']): trans for trans in tabela_transicoes}

    with open(entrada, 'r') as arquivo_entrada:
        fita = list(arquivo_entrada.read().strip()) 

    posicao_fita = 0 

    while estado_atual not in estados_aceitos:
        simbolo_atual = fita[posicao_fita] if posicao_fita < len(fita) else simbolo_em_branco
        chave_transicao = (estado_atual, simbolo_atual) 

        if chave_transicao not in transicoes_dict:
            print(f"Fita rejeitada: {''.join(fita)}\nResultado: 0")
            return

        # Executa a transição
        transicao_atual = transicoes_dict[chave_transicao]

        # Atualiza o símbolo na fita de acordo com a transição
        if posicao_fita < len(fita):
            fita[posicao_fita] = transicao_atual['write']
        else:
            fita.append(transicao_atual['write'])

        estado_atual = transicao_atual['to']

        posicao_fita += 1 if transicao_atual['dir'] == 'R' else -1
        posicao_fita = max(0, posicao_fita)

    resultado_fita = ''.join(fita) + "\n"

    with open(saida, 'w') as arquivo_saida:
        arquivo_saida.write(resultado_fita)

    print(f"Resultado: {resultado_fita.strip()} - Aceito")

def iniciar_programa():
    config = "duplo_bal.json"
    entrada = "entrada1.txt"
    saida = "saida.txt"
    
    executar_maquina_turing(config, entrada, saida)

if __name__ == "__main__":
    iniciar_programa()
