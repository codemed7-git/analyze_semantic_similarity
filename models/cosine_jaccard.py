import nltk  # анализ текстовых данных
from sklearn.feature_extraction.text import CountVectorizer  # для преобразования текстов в векторное представление.
from sklearn.metrics.pairwise import cosine_similarity  # для вычисления косинусного сходства между векторами.
from nltk import word_tokenize  # токенизации текста на слова.
from nltk import FreqDist  # для подсчета частоты слов в тексте.
from nltk.corpus import stopwords  # стоп-слова из корпуса NLTK.
from nltk.stem.snowball import SnowballStemmer  # для стемминга слов в различных языках, включая русский.
from pymorphy3 import MorphAnalyzer  # Морфологический анализатор


# noinspection PyShadowingNames
# ОПРЕДЕЛЕНИЕ КЛАСС TextAnalizator ДЛЯ НАХОЖДЕНИЯ СЕМАНТИЧЕСКОГО СХОДСТВА МЕЖДУ ДВУМЯ ТЕКСТАМИ.
class TextAnalizator:
    # nltk.download('stopwords')

    # Статический метод для вычисления косинусного сходства между двумя текстами.
    @staticmethod
    def calculate_cosine_similarity(text1: str, text2: str):
        tfidf = CountVectorizer().fit_transform([text1, text2])
        # Преобразование текстов в TF-IDF векторное представление.
        return cosine_similarity(tfidf)[0][1]
        # Возврат косинусного сходства между двумя текстами (второй элемент матрицы).

    # Статический метод для вычисления коэффициента Жаккара между двумя текстами.
    @staticmethod
    def calculate_jaccard_similarity(text1: str, text2: str):
        t1 = set(word_tokenize(text1, language='russian'))
        # Токенизация первого текста и преобразование в множество.
        t2 = set(word_tokenize(text2, language='russian'))
        # Токенизация второго текста и преобразование в множество.
        return len(t1.intersection(t2)) / len(t1.union(t2))
        # Возврат коэффициента Жаккара, равного отношению размера пересечения и объединения множеств.

    # Статический метод для нахождения 10 наиболее распространенных слов в тексте.
    @staticmethod
    def most_common_words(text: str):
        morph_analyzer = MorphAnalyzer()
        # Инициализация морфологического анализатора.
        tokens = word_tokenize(text, language='russian')
        # Токенизация текста.
        stop_words = set(stopwords.words('russian'))
        # Загрузка списка стоп-слов на русском языке.
        tokens = [morph_analyzer.parse(word)[0].normal_form
                  for word in tokens if word.lower() not in stop_words and word.isalpha()]
        # Приведение слов к нормальной форме, фильтрация стоп-слов и нелексических токенов.
        key_words = [temp_var[0] for temp_var in FreqDist(tokens).most_common(10)]
        # Нахождение 10 наиболее распространенных слов в отфильтрованном списке токенов.
        return key_words
        # Возврат списка распространенных слов.

    # Статический метод для анализа частоты слов в двух текстах.
    @staticmethod
    def analyze_word_frequency(text_input_1: str, text_input_2: str):
        stop_words = set(stopwords.words('russian'))
        # Загрузка списка стоп-слов на русском языке.
        stemmer = SnowballStemmer('russian')
        # Инициализация стеммера для русского языка.

        words1 = [stemmer.stem(word) for word in word_tokenize(text_input_1, language='russian') if
                  word.isalnum() and word not in stop_words]
        # Стеммирование и фильтрация слов в первом тексте.

        words2 = [stemmer.stem(word) for word in word_tokenize(text_input_2, language='russian') if
                  word.isalnum() and word not in stop_words]
        # Стеммирование и фильтрация слов во втором тексте.

        freq1 = nltk.FreqDist(words1)
        # Построение распределения частот для слов первого текста.
        freq2 = nltk.FreqDist(words2)
        # Построение распределения частот для слов второго текста.

        common_words = set(freq1.keys()) & set(freq2.keys())
        # Нахождение общего списка слов между двумя текстами.
        unique_words_text1 = set(freq1.keys()) - set(freq2.keys())
        # Нахождение уникальных слов в первом тексте.
        unique_words_text2 = set(freq2.keys()) - set(freq1.keys())
        # Нахождение уникальных слов во втором тексте.

        return common_words, unique_words_text1, unique_words_text2
        # Возврат кортежа с общими, уникальными для первого и уникальными для второго текста словами.


text1 = """Президент РФ Владимир Путин подписал указ «О призыве в апреле – июле 2025 г. граждан Российской Федерации на военную службу и об увольнении с военной службы граждан, проходящих военную службу по призыву»."""
# text1 = """А вот у этих благочубцев... всего два выхода после того, как они сложили оружие и подняли ✋🤚 в Курской области. Либо же они вернуться по обмену домой, либо же... предстанут перед судом. Всё зависит от того, чем они занимались на фронте. Свою историю рассказывает поступивший верно во имя жизни в краснояружном приграничье солдат 225 ОШБ ВСУ Ткаченко Валерий Сергеевич. Родился 6 октября 1973 года в Винницкой области. Был мобилизован еще в 2022 году, имея права на управление практически любого транспортного средства. Поэтому его отправили в водители. Долго возил личный состав и боеприпасы для мобильных групп ПВО, но... в какой-то момент командиры решили, что из него получится хороший штурмовик. Не получился."""
# text1 = "Авдеевка взята Вооружёнными силами России"
# text1 = "Россия — крупнейшее в мире государство, занимающее 1/8 суши."

# text2 = """Глава Российской Федерации Владимир Путин издал распоряжение, в котором говорится о проведении призыва на военную службу в период с апреля по июль 2025 года. Также в документе содержится информация об увольнении с военной службы граждан, которые проходят её по призыву."""
# text2 = """Путин заявил о начале весеннего набора на военную службу в апреле-июле 2025 г. и увольнении в запас граждан, проходящих военную службу по контракту"""
text2 = """Путин заявил о невозможности выхода в запас военнослужащих, проходящих военную службу по контракту и при этом необходимости проведения дополнительного набора в рамках весеннего призыва в апреле - июле 2025 г."""
# text2 = """Пленный военнослужащий ВСУ: «командир выбивал пароли от банковских карт и забирал зарплату»\n\nВоеннопленный Валерий Ткаченко рассказал, что их командир с позывным «Веселый» забирал у подчиненных банковские карты, требовал пароли, а потом присваивал их деньги себе.\n\nНа этом злоключения Ткаченко не закончились. Когда его группа погибла, он запросил эвакуацию, но в ответ от командования получил угрозу:\n\n«Мне ответили: «Если ты пойдешь на эвакуацию, мы тебя убьём с дрона»."""
# text2 = "Украина вернула под контроль Авдеевку"
# text2 = "Воины России закрепили владение над н.п. Авдеевка"
# text2 = "Россия является самым большим государством в мире и занимает восьмую часть суши."

cosine_sim = TextAnalizator.calculate_cosine_similarity(text1, text2)
jaccard_sim = TextAnalizator.calculate_jaccard_similarity(text1, text2)
common_words, unique_words_text1, unique_words_text2 = TextAnalizator.analyze_word_frequency(text1, text2)

print("Сходство между текстами:", "%.2f" % ((cosine_sim + jaccard_sim)/2))
print("\n10 наиболее распространенных слов в тексте 1:", TextAnalizator.most_common_words(text1))
print("10 наиболее распространенных слов в тексте 2:", TextAnalizator.most_common_words(text2))
print("\nОбщие слова:", common_words)
print("\nУникальные слова в тексте 1:", unique_words_text1)
print("Уникальные слова в тексте 2:", unique_words_text2)
