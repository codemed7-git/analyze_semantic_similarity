from models import cosine_jaccard

text1 = ''

text2 = ''


# Вычисляем косинусное сходство между двумя текстами
cosine_sim = cosine_jaccard.TextAnalizator.calculate_cosine_similarity(text1, text2)
# Вычисляем коэффициент Жаккара между двумя текстами
jaccard_sim = cosine_jaccard.TextAnalizator.calculate_jaccard_similarity(text1, text2)

res_analyze_two_posts = round(((cosine_sim + jaccard_sim) / 2), 2)

# text1 = "Россия — крупнейшее в мире государство, занимающее 1/8 суши."
# text2 = "Россия является самым большим государством в мире и занимает восьмую часть суши."
# cosine_sim = TextAnalizator.calculate_cosine_similarity(text1, text2)
# jaccard_sim = TextAnalizator.calculate_jaccard_similarity(text1, text2)
# common_words, unique_words_text1, unique_words_text2 = TextAnalizator.analyze_word_frequency(text1, text2)
#
# print("Сходство между текстами:", "%.2f" % ((cosine_sim + jaccard_sim)/2))
# print(TextAnalizator.most_common_words(text1))
# print(TextAnalizator.most_common_words(text2))
# print("Общие слова:", common_words)
# print("Уникальные слова в тексте 1:", unique_words_text1)
# print("Уникальные слова в тексте 2:", unique_words_text2)
