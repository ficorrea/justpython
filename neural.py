import csv
import random


dataset = []
with open('data.csv') as file:
    data = csv.reader(file, delimiter=',')
    for line in data:
        line = [float(elemento) for elemento in line]
        dataset.append(line)


def treino_teste_split(dataset, porcentagem_teste):
    percent = porcentagem_teste*len(dataset)//100
    data_treino = random.sample(dataset, percent)
    data_teste = [data for data in dataset if data not in data_treino]

    def montar_df(dataset):
        x, y = [], []
        for data in dataset:
            x.append(data[0:5])
            y.append(data[5])
        return x, y
    x_train, y_train = montar_df(data_treino)
    x_test, y_test = montar_df(data_teste)
    return x_train, x_test, y_train, y_test


x_treino, x_teste, y_treino, y_teste = treino_teste_split(dataset, 80)


def sinal(u):
    return 1 if u >= 0 else 0


def ajuste(w, x, d, y):
    taxa_aprendizagem = 0.001
    return w + taxa_aprendizagem * (d - y) * x


def perceptron_fit(x, d):
    epoca = 0
    w = [random.random() for i in range(6)]
    print('Ws iniciais: {}'.format(w))
    while True:
        erro = False
        for i in range(len(x)):
            u = sum([w[0]*-1, w[1]*x[i][0], w[2]*x[i][1],
                     w[3]*x[i][2], w[4]*x[i][3], w[5]*x[i][4]])
            y = sinal(u)
            if y != d[i]:
                w[0] = ajuste(w[0], -1, d[i], y)
                w[1] = ajuste(w[1], x[i][0], d[i], y)
                w[2] = ajuste(w[2], x[i][1], d[i], y)
                w[3] = ajuste(w[3], x[i][2], d[i], y)
                w[4] = ajuste(w[4], x[i][3], d[i], y)
                w[5] = ajuste(w[5], x[i][4], d[i], y)
                erro = True
        epoca += 1
        if erro is False or epoca == 1000:
            break
    print('Épocas: {}'.format(epoca))
    return w


w_fit = perceptron_fit(x_treino, y_treino)
print('Ws ajustados: {}'.format(w_fit))


def perceptron_predict(x_test, w_ajustado):
    y_predict = []
    for i in range(len(x_test)):
        predict = sum(
            [w_ajustado[0]*-1, w_ajustado[1]*x_test[i][0],
             w_ajustado[2]*x_test[i][1], w_ajustado[3]*x_test[i][2],
             w_ajustado[4]*x_test[i][3], w_ajustado[5]*x_test[i][4]]
        )
        y_predict.append(sinal(predict))
    return y_predict


y_validado = perceptron_predict(x_teste, w_fit)
print('Y validado: {}'.format(y_validado))


def acuracia(y_test, y_predict):
    total_acertos = 0
    for i in range(len(y_test)):
        if y_predict[i] == y_test[i]:
            total_acertos += 1
        else:
            pass
    return total_acertos / len(y_test)


accuracy = acuracia(y_teste, y_validado)
print('Acurácia: {}'.format(accuracy))
