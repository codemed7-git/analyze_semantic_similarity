from collections import Counter
import re
import emoji


# -------------------------------------------
# def most_common_words(texts):
#     words = text.lower().split()
#     word_counts = Counter(words)
#     max_count = max(word_counts.values())
#     most_common = [word for word, count in word_counts.items() if count == max_count]
#
#     return most_common


# -------------------------------------------
def remove_emojis(text):
    clear_text = emoji.replace_emoji(text, replace='')
    # t = re.sub(r'http\S+', '', t)
    # t = re.sub(r't.me\S+', '', t)
    return clear_text


# ----------------------------------------------------------------------------------------------------------------------
def clean_text(text):
    res = remove_emojis(text)
    return res