# 11811ECP012 - Anaísa Forti da Fonseca

n = input()                          # número de estados
sigma = input()                      # conjunto de símbolos terminais
gama = input()                       # conjunto de símbolos da pilha
F = input()                          # conjunto de estados de aceitação
nTransicoes = input()                # número de transições do autômato

t = []                               # lista de transições
while len(t) < int(nTransicoes):     # recebendo todas as transições
    transicao = input()
    transicao = transicao.split(' ')
    t.append(transicao)

c = input()                          # número de cadeias que serão avaliadas
cadeias = []                         # lista de cadeias a serem avaliadas
while len(cadeias) < int(c):         # recebendo todas as cadeias
    cad = input()
    cad = list(cad)
    cadeias.append(cad)

sigma = sigma.split(' ')             # separando os símbolos terminais
nSimbolos = sigma[0]                 # quantidade de símbolos terminais
simbolos = sigma[1:]                 # lista de símbolos terminais

gama = gama.split(' ')               # separando os símbolos da pilha
nSimbolosPilha = gama[0]             # quantidade de símbolos da pilha
simbolosPilha = gama[1:]             # lista de símbolos da pilha

F = F.split(' ')                     # separando os estados de aceitação
nEstados = F[0]                      # número de estados de aceitação
estados = F[1:]                      # lista de estados de aceitação

aceitacao = list(map(int,estados))   # transformando estados de aceitação em inteiros


# função recursiva para percorrer cada cadeia de entrada
# se parar em estado de aceitação: true, outro estado: false
def percorreCadeia(cadeiaAtual, estadoAtual, pilha):
    # pega o símbolo da cadeia atual a ser analisado
    if(cadeiaAtual != []):
        simboloAtual = cadeiaAtual[0]

    # laço for para percorrer todas as possíveis transições
    for i in range(len(t)):
        # pega as informações da transição atual
        topoPilha = pilha[-1]
        transicaoAtual = t[i]
        estadoInicialT = int(transicaoAtual[0])
        simboloT = transicaoAtual[1]
        topoPilhaT = transicaoAtual[2]

        # cadeias que ja foram totalmente percorridas ou cadeias vazias
        if(cadeiaAtual == [] or cadeiaAtual == ['-']):
            # confere se o estado atual é um de aceitação
            if(estadoAtual in aceitacao):
                return True

            # percorre transições vazias para ver outros estados finais possíveis
            elif(
                (estadoInicialT == estadoAtual) 
                and (list(simboloT) == ['-']) 
                and (topoPilhaT == topoPilha)
            ):
                # define o estado atingido e a lista de cadeia de
                # símbolos a ser empilhada
                estadoNovo = int(transicaoAtual[3])
                empilha = list(transicaoAtual[4])

                # função que trata o empilhamento da cadeia de símbolos da pilha
                if(empilhamento(cadeiaAtual,estadoNovo,pilha,empilha)):
                    return True
                # confere se o novo estado atingido é um de aceitação
                if(estadoNovo in aceitacao):
                    return True

        # qualquer cadeia que NÃO tenha sido totalmente percorrida
        elif(cadeiaAtual != []):
            if(
                (estadoInicialT == estadoAtual)
                and (topoPilhaT == topoPilha)
            ):
                # confere se o símbolo da transição é um símbolo do autômato,
                # segue a transição e PERCORRE a cadeia
                if(simboloT == simboloAtual):
                    # define o estado atingido, a cadeia nova e a lista de
                    # cadeia de símbolos a ser empilhada
                    cadeiaNova = cadeiaAtual[1:]
                    estadoNovo = int(transicaoAtual[3])
                    empilha = list(transicaoAtual[4])
                    # função que trata o empilhamento da cadeia de símbolos da pilha
                    if(empilhamento(cadeiaNova, estadoNovo, pilha, empilha)):
                        return True

                # confere se o símbolo da transição é o símbolo vazio,
                # segue a transição e NÃO PERCORRE a cadeia
                elif(list(simboloT) == ['-']):
                    # define o estado atingido, a cadeia nova e a lista de
                    # cadeia de símbolos ser empilhada
                    cadeiaNova = cadeiaAtual
                    estadoNovo = int(transicaoAtual[3])
                    empilha = list(transicaoAtual[4])
                    # função que trata o empilhamento da cadeia de símbolos da pilha
                    if(empilhamento(cadeiaNova, estadoNovo, pilha, empilha)):
                        return True
    return False


# função para tratar o empilhamento da cadeia de símbolos da pilha
def empilhamento(cadeiaNova, estadoNovo, pilha, empilha):
    # empilhamento vazio: apenas deleta o topo da pilha
    if(empilha == ['-']):
        popped = pilha.pop()
        if(percorreCadeia(cadeiaNova,estadoNovo,pilha)):
            return True
        else:
            pilha.append(popped)

    # empilhamento não-vazio: substitui o topo da pilha pela cadeia de 
    # símbolos da pilha relativa à transição (exemplo: A, BA, BZ)
    elif(empilha != ['-']):
        empilhaReverso = empilha[::-1]
        popped = pilha.pop()
        pilhaNova = pilha + empilhaReverso
        # chama a função principal para continuar percorrendo a cadeia
        if(percorreCadeia(cadeiaNova,estadoNovo,pilhaNova)):
            return True
        # desfaz o que foi feito na pilha caso o caminho não seja válido
        else:
            pilha.append(popped)


# aceitação ou rejeição de cada cadeia de entrada
for j in range(int(c)):
    pilha = ['Z']
    cadeiaAtual = cadeias[j]
    # percorre cada cadeia (o estado 0 é sempre o estado inicial)
    if(percorreCadeia(cadeiaAtual,0,pilha)):
        print("aceita")
    else:
        print("rejeita")