import time
import asyncio

from parsing import connect_session
from db import work_with_db
from parsing import clear_text
from parsing.clear_text import clean_text


# ----------------------------------------------------------------------------------------------------------------------
# собирает посты с канала
async def find_channel(client, username_channel):
    messages = await client.get_messages(username_channel, 5000)
    # res = []
    d = {}

    c_posts = 0
    for mes in messages:
        if mes.text is not None and mes.text != '':
            try:
                work_with_db.insert_post(username_channel, mes.id, mes.message, clear_text.clean_text(mes.message))
            except Exception as ex:
                print(f'{"-" * 20}\n{ex}\n{mes.message}\n{"-" * 20}')
            c_posts += 1
            if c_posts % 100 == 0:
                print(c_posts)

        # message_data = {
        #     'id': mes.id,
        #     'date': str(mes.date),
        #     'text': mes.message
        # }
        # res.append(message_data)

    # записываем в json
    # with open(f'result_parsing_{username_channel}.json', 'w', encoding='utf-8') as file_json:
    #     json.dump(obj=res,
    #               fp=file_json,
    #               ensure_ascii=False,
    #               indent=4)


async def start_parsing():
    client = await connect_session.return_connect_telethon()
    async with client:
        start_time = time.time()

        # await find_channel(client, 'rusich_army')
        await find_channel(client, 'RVvoenkor')

        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f'\n----------------\nthe end. time: {elapsed_time}')
    await connect_session.return_disconnect_telethon(client)


# ----------------------------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    # work_with_db.select_posts('rusich_army'):
    #     print(clean_text(t))

    asyncio.run(start_parsing())
