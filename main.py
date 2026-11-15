import json
from pathlib import Path

from models import modelBM25
from db import work_with_db
from analyze import analyze_scores
from models import cosine_jaccard

channel1 = 'rusich_army'
channel2 = 'RVvoenkor'

posts_rusich_army = work_with_db.select_posts(channel1, 10)
posts_RVvoenkor = work_with_db.select_posts(channel2, 10)

ind_rusich_army = [i[0] for i in posts_rusich_army]
ind_RVvoenkor = [i[0] for i in posts_RVvoenkor]

res_analyze_scores = []

data_json = []

for i in range(len(posts_rusich_army)):
    row_res_analyze_scores = []
    for j in range(len(posts_RVvoenkor)):
        text1, text2 = posts_rusich_army[i][1], posts_RVvoenkor[j][1]

        """ --- cosine_jaccard ------------------------------------------------------------------------------------- """
        # Вычисляем косинусное сходство между двумя текстами
        cosine_sim = cosine_jaccard.TextAnalizator.calculate_cosine_similarity(text1, text2)
        # Вычисляем коэффициент Жаккара между двумя текстами
        jaccard_sim = cosine_jaccard.TextAnalizator.calculate_jaccard_similarity(text1, text2)

        res_analyze_two_posts = round(((cosine_sim + jaccard_sim) / 2), 2)
        """ -------------------------------------------------------------------------------------------------------- """

        """ --- modelBM25 ------------------------------------------------------------------------------------------ """
        # res_analyze_two_posts = float(modelBM25.return_res_bm25(text1, text2))
        """ -------------------------------------------------------------------------------------------------------- """

        # ДЛЯ ТАБЛИЦЫ (графика)
        row_res_analyze_scores.append(res_analyze_two_posts)

        # для JSON
        data_json.append({'id1': posts_rusich_army[i][0],
                          'id2': posts_RVvoenkor[j][0],
                          'text1': posts_rusich_army[i][1],
                          'text2': posts_RVvoenkor[j][1],
                          'score': res_analyze_two_posts})

        # для БД
        work_with_db.insert_result_BM25(posts_rusich_army[i][0],
                                        posts_RVvoenkor[j][0],
                                        posts_rusich_army[i][1],
                                        posts_RVvoenkor[j][1],
                                        res_analyze_two_posts)


    res_analyze_scores.append(row_res_analyze_scores)


# записываем в json
with open(Path(__file__).resolve().parent / 'data' / 'result_BM25.json', 'w', encoding='utf-8') as file_json:
    json.dump(obj=data_json,
              fp=file_json,
              ensure_ascii=False,
              indent=4)


print(analyze_scores.start_analyze(channel1, ind_rusich_army, channel2, ind_RVvoenkor, res_analyze_scores))
