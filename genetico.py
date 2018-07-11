import random
import string

alfabeto = string.printable[:-5]
senha = list('senha#$%@')
# senha = random.sample(alfabeto, 20)
MAX = 10000


def populacao(quantidade_cromossomos, quantidade_individuos):
    individuos = [random.sample(alfabeto, quantidade_cromossomos)
                  for i in range(quantidade_individuos)]
    return individuos


def fitness_individuo(senha, individuo):
    valor = 0
    for caracter, letra in zip(senha, individuo):
        if caracter == letra:
            valor += 1
    return valor


def fitness_populacao(individuos):
    fitness_geral = []
    for i in range(len(individuos)):
        fitness_geral.append(fitness_individuo(senha, individuos[i]))
    return fitness_geral


def selecao(individuos, quantidade_individuos, fitness_populacao):
    melhores = []
    for i in range(quantidade_individuos):
        melhores.append(
            individuos[fitness_populacao.index(max(fitness_populacao))])
        individuos.pop(fitness_populacao.index(max(fitness_populacao)))
        fitness_populacao.pop(fitness_populacao.index(max(fitness_populacao)))
    return melhores


def cruzamento(individuos):
    filhos = []
    for i in range(1, len(individuos), 2):
        filhos.append(individuos[i-1][0:len(senha)//2] +
                      individuos[i][len(senha)//2:len(senha)])
    return filhos


def mutacao(filhos, taxa):
    for x in range(len(filhos)):
        filho = filhos[x]
        for i in range(len(filho)):
            if random.random() <= taxa:
                filho[i] = ''.join(random.sample(alfabeto, 1))
        filhos[x] = filho
    return filhos


def parada(senha, individuos):
    for individuo in individuos:
        if individuo == senha:
            print('Resultado: {}'.format(''.join(individuo)))
            return True
    return False


x = 1
populacao = populacao(len(senha), 5)

while x < MAX:
    fitness = fitness_populacao(populacao)
    melhores = selecao(populacao[:], 2, fitness[:])
    print('Geração {} : {}'.format(x, melhores[0]))
    filhos = cruzamento(melhores[:])
    mutados = mutacao(filhos, 0.05)
    populacao = melhores + mutados
    if parada(senha, populacao) is True:
        break
    x += 1

if x >= MAX:
    print(''.join(senha))
    print('Geração máxima atingida e senha não encontrada')
