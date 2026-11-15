import nltk
from rank_bm25 import BM25Okapi


def return_res_bm25(text1, text2):
    # nltk.download('punkt_tab')

    # Предобработка текстов
    def preprocess_text(text):
        tokens = nltk.word_tokenize(text.lower())  # Приводим к нижнему регистру и токенизируем
        return [token for token in tokens if token.isalnum()]  # Оставляем только алфавитные символы


    # Получаем токены для каждого текста
    doc1 = preprocess_text(text1)
    doc2 = preprocess_text(text2)

    # Объединяем документы в один список
    documents = [doc1, doc2]

    # Создаем модель BM25
    bm25 = BM25Okapi(documents)
    # print(bm25)

    # Вычисляем сходство между первым и вторым документом
    scores = bm25.get_scores(doc1)

    # Результат
    similarity_score = scores[1]  # Сходство второго документа с первым

    # res = {'text1': text1,
    #        'text2': text2,
    #        'doc1': doc1,
    #        'doc2': doc2,
    #        'similarity_score': similarity_score}
    return similarity_score

    # Выводим результаты
    # print("Семантическое сходство между текстами:", similarity_score)
    # print("Подробности анализа:")
    # print("Токены первого текста:", doc1)
    # print("Токены второго текста:", doc2)
