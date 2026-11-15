import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent.parent / "data" / "posts.db"


def insert_post(name_table, id_post, text_post, clear_text_post):
    con = sqlite3.connect(DB_PATH)
    cur = con.cursor()

    try:
        cur.execute(f'INSERT INTO {name_table} VALUES (?, ?, ?)',
                    (id_post, text_post, clear_text_post))
    except Exception as ex:
        print(ex)

    con.commit()


def select_posts(name_table, lim):
    con = sqlite3.connect(DB_PATH)
    cur = con.cursor()

    try:
        cur.execute(f'SELECT * FROM {name_table} LIMIT {lim}')
        # posts = [t[2] for t in cur.fetchall()]
        posts = [[t[0], t[2]] for t in cur.fetchall()]
        con.commit()
        return posts
    except Exception as ex:
        print(ex)


def select_all_table(name_table):
    con = sqlite3.connect(DB_PATH)
    cur = con.cursor()

    try:
        cur.execute(f'SELECT * FROM {name_table}')
        res = cur.fetchall()
        con.commit()
        return res
    except Exception as ex:
        print(ex)


def insert_result_BM25(id_rusich_army, id_RVvoenkor, text_rusich_army, text_RVvoenkor, scope):
    con = sqlite3.connect(DB_PATH)
    cur = con.cursor()

    try:
        cur.execute(f'INSERT INTO result_BM25 VALUES (?, ?, ?, ?, ?)',
                    (id_rusich_army, id_RVvoenkor, text_rusich_army, text_RVvoenkor, scope))
    except Exception as ex:
        print(ex)

    con.commit()
