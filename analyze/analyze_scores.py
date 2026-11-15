import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# def ct(ch1, indxs1, ch2, indxs2, scores):
#     print(indxs1)
#
#     # Подготовка данных
#     data = []
#
#     for i in range(len(indxs1)):
#         for j in range(len(indxs2)):
#             pass
#             # print(scores[i][j])
#             # data.append({'Row': i, 'Column': j, 'Value': scores[i][j]})
#     #
#     # Создание DataFrame
#     # df = pd.DataFrame(data)
#     #
#     # Создание сводной таблицы
#     # pivot_table = df.pivot(index='Row', columns='Column', values='Value')
#     #
#     # Вывод сводной таблицы
#     # return pivot_table

def create_matrix(indxs1, indxs2, scores):
    similarity_matrix = pd.DataFrame(scores, index=indxs1, columns=indxs2)
    return similarity_matrix

def start_analyze(ch1, indxs1, ch2, indxs2, scores):
    matrix = create_matrix(indxs1, indxs2, scores)

    sns.set(style="whitegrid")

    # Визуализация тепло-карту
    plt.figure(figsize=(10, 8))
    sns.heatmap(matrix, annot=True, fmt=".2f", cmap="coolwarm", cbar=True)
    plt.title("Тепло-карта значений")
    plt.xlabel("RVvoenkor")
    plt.ylabel("rusich_army")
    plt.show()

    # print(matrix.describe())

    # correlation = matrix.corr()
    # plt.figure(figsize=(10, 8))
    # sns.heatmap(correlation, annot=True, cmap="coolwarm", cbar=True)
    # plt.title("Корреляция значений")
    # plt.show()

    return 'exit.'
