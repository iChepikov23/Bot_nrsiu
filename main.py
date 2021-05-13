import vk_api
from vk_api import VkUpload
from vk_api.longpoll import VkLongPoll, VkEventType
import random
import time
import json

token = "713dfee5a7ed1f46b2a81efae9dfc81b8b2cb36589895b1b10106ae130e720e2d7dbbb33f4264fc06c5f2"
vk = vk_api.VkApi(token=token)
vk._auth_token()


def read():
    file = open("info.txt", "r", encoding = "utf-8")
    i=1
    for line in file:
        if i % 3 == 1:
            vk.method("messages.send",
                      {"peer_id": id, "message": line, "random_id": random.randint(1, 2147483647)})
            i = i + 1
        else:
            i = i + 1

    file.close()

def give(num):
    file = open("info.txt", "r", encoding = "utf-8")
    i=1
    ch = ''
    n = 0
    key =0
    for line in file:
        if key== 2:
            vk.method("messages.send",
                      {"peer_id": id, "keyboard": keyboard2,
                       "message": "👉🏻Это ссылка на хозяина выбранной книги: ",
                       "random_id": random.randint(1, 2147483647)})
            vk.method("messages.send", {"peer_id": id, "message": line,
                                        "random_id": random.randint(1, 2147483647)})
            vk.method("messages.send",
                      {"peer_id": id, "keyboard": keyboard2,
                       "message": "\n\n😢 Он сказал, что эта книга уже очень долго стоит на полке без дела. Напиши ему, чтобы договориться об обмене.\n\n😇 Обязательно напиши мне о результатах!",
                       "random_id": random.randint(1, 2147483647)})
            key=0


        if key ==1:
            vk.method("messages.send", {"peer_id": id, "keyboard": keyboard1,"message": line, "random_id": random.randint(1, 2147483647)})
            key=2

            construct(id, id, 0, 0)


        if i % 3 == 1:
            a = list(line)
            while a[n] != ' ':
               ch= ch+a[n]
               n=n+1
            if ch == num:
                key =1





            #vk.method("messages.send",{"peer_id": id, "message": line, "random_id": random.randint(1, 2147483647)})
            i = i + 1
            ch = ''
            n = 0
        else:
            i = i + 1

    file.close()








##Вторая часть


def construct(id, name, money, power):
    p = {}
    p["name"] = name
    p["money"] = money
    p["messegNumb"] = 0
    p["power"] = power
    data[str(id)] = p


def savebd():
    with open("data.txt", "w") as file:
        for i in data:  # проходимся по data и получаем id в нем
            p = str(i) + " " + str(data[i]["name"]) + " " + str(data[i]["money"]) + " " + str(
                data[i]["messegNumb"]) + " " + str(data[i]["power"])

            file.write(p + '\n')  # записываем в data.txt построчно пользователей


def loadbd():
    file = open("data.txt", "r")
    datas = file.read()
    datas = datas.splitlines()
    file.close()
    data = {}
    for i in datas:
        i = i.split()
        if len(i) > 4:  # проверка на полноту данных
            data[str(i[0])] = {}
            data[str(i[0])]["name"] = i[1]
            data[str(i[0])]["money"] = i[2]
            data[str(i[0])]["messegNumb"] = i[3]
            data[str(i[0])]["power"] = i[4]

    return (data)


data = loadbd()  # загружаем в переменную data информацию из функции loadbd и файла data.txt


def get_button(label, color, payload=""):
    return {
        "action": {
            "type": "text",
            "payload": json.dumps(payload),
            "label": label
        },
        "color": color
    }


keyboard10 = {
    "one_time": False,
    "buttons": [
        [get_button(label="Назад к главному меню", color="primary")]
    ]
}

keyboard10 = json.dumps(keyboard10, ensure_ascii=False).encode('utf-8')
keyboard10 = str(keyboard10.decode('utf-8'))

keyboard1 = {
    "one_time": False,
    "buttons": [
        [get_button(label="Беру", color="primary"), get_button(label="Подумаю ещё", color="negative")],
        [get_button(label="Назад к главному меню", color="primary")]

    ]
}

keyboard1 = json.dumps(keyboard1, ensure_ascii=False).encode('utf-8')
keyboard1 = str(keyboard1.decode('utf-8'))

keyboard2 = {
    "one_time": False,
    "buttons": [
        [get_button(label="Книга получена", color="primary"), get_button(label="Обмен не состоялся", color="negative")],
        [get_button(label="Назад к главному меню", color="primary")]

    ]
}

keyboard2 = json.dumps(keyboard2, ensure_ascii=False).encode('utf-8')
keyboard2 = str(keyboard2.decode('utf-8'))

keyboard3 = {
    "one_time": False,
    "buttons": [
        [get_button(label="1", color="primary"), get_button(label="2", color="negative")],
        [get_button(label="Назад к главному меню", color="primary")]

    ]
}

keyboard3 = json.dumps(keyboard3, ensure_ascii=False).encode('utf-8')
keyboard3 = str(keyboard3.decode('utf-8'))

keyboard = {
    "one_time": False,
    "buttons": [
        [get_button(label="Xочу сдать книгу", color="primary"), get_button(label="Хочу взять книгу", color="negative")],
        [get_button(label="Назад к главному меню", color="primary")]

    ]
}

keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
keyboard = str(keyboard.decode('utf-8'))

# У кнопок может быть один из 4 цветов:
# 1. primary — синяя кнопка, обозначает основное действие. #5181B8
# 2. default — обычная белая кнопка. #FFFFFF
# 3. negative — опасное действие, или отрицательное действие (отклонить, удалить и тд). #E64646
# 4. positive — согласиться, подтвердить. #4BB34B
while True:
    try:
        messages = vk.method("messages.getConversations", {"offset": 0, "count": 20, "filter": "unanswered"})
        id = messages["items"][0]["last_message"]["from_id"]
        body = messages["items"][0]["last_message"]["text"]
        n = 0
        for i in data:
            print(i)
            if str(id) == i:
                n = 1
        if n == 0:
            construct(id, id, 0, 0)

        if messages["count"] >= 1 and int(data[str(id)]["power"]) == 0:
            # авторизация пользователя в боте

            if body == "Xочу сдать книгу":
                # key = 1
                construct(id, id, 0, 1)

                vk.method("messages.send",
                          {"peer_id": id, "keyboard": keyboard10,
                           "message": "🙏🏻 Для того, чтобы мы могли включить твою книгу в онлайн-библиотеку, ответь, пожалуйста, на пару вопросов.",
                           "random_id": random.randint(1, 2147483647)})

                vk.method("messages.send",
                          {"peer_id": id, "keyboard": keyboard10, "message": "📕Название книги?",
                           "random_id": random.randint(1, 2147483647)})



            elif body == "Хочу взять книгу":
                construct(id, id, 0, 4)
                vk.method("messages.send",
                          {"peer_id": id, "keyboard": keyboard10,
                           "message": "🤗 Ознакомься с нашей онлайн-библиотекой!\n\n👉🏻 Чтобы помочь тебе побыстрее определиться с выбором, я могу прислать краткое описание той книги, порядковый номер которой ты отправишь в чат\n\n",
                           "random_id": random.randint(1, 2147483647)})
                read()

            elif body.lower() == "начать":
                vk.method("messages.send",
                          {"peer_id": id,
                           "message": "💡 Я могу найти интересную тебе литературу или же могу принять твои запылившиеся книги в онлайн-библиотеку буккроссинга\n\n😎 С чем тебе помочь?",
                           "random_id": random.randint(1, 2147483647)})
                vk.method("messages.send",
                          {"peer_id": id, "keyboard": keyboard, "message": "Воспользуйся кнопками 👇🏻\n\n",
                           "random_id": random.randint(1, 2147483647)})
            elif body.lower() == "назад к главному меню":

                vk.method("messages.send",
                          {"peer_id": id, "keyboard": keyboard, "message": "Воспользуйся кнопками 👇🏻\n\n",
                           "random_id": random.randint(1, 2147483647)})
            elif body.lower() == "чепиков илья":
                vk.method("messages.send",
                          {"peer_id": id, "message": "Это мой создатель", "random_id": random.randint(1, 2147483647)})
            elif body.lower() == "беру":
                vk.method("messages.send",
                          {"peer_id": id, "keyboard": keyboard2,
                           "message": "👉🏻Это ссылка на хозяина выбранной книги: ",
                           "random_id": random.randint(1, 2147483647)})


                vk.method("messages.send",
                          {"peer_id": id, "keyboard": keyboard2,"message": "😢 Он сказал, что эта книга уже очень долго стоит на полке без дела. Напиши ему, чтобы договориться об обмене.\n\n😇 Обязательно напиши мне о результатах!", "random_id": random.randint(1, 2147483647)})
            elif body.lower() == "книга получена":
                vk.method("messages.send",
                          {"peer_id": id, "keyboard": keyboard,
                           "message": "Круто👍🏻 \n\nСпасибо за то, что подарил книге новую жизнь❤🤗",
                           "random_id": random.randint(1, 2147483647)})
            elif body.lower() == "обмен не состоялся":
                construct(id, id, 0, 4)
                vk.method("messages.send",
                          {"peer_id": id, "keyboard": keyboard10,
                           "message": "Может быть, попробуешь найти что-нибудь еще?🥺👉🏻👈🏻\n\n",
                           "random_id": random.randint(1, 2147483647)})
                read()
            elif body.lower() == "подумаю ещё":
                construct(id, id, 0, 4)
                vk.method("messages.send",
                          {"peer_id": id, "keyboard": keyboard10, "message": "Выбери нужную тебе книгу\n\n",
                           "random_id": random.randint(1, 2147483647)})
                read()
            elif body.lower() == "кнопки":
                vk.method("messages.send", {"peer_id": id, "keyboard": keyboard, "message": "вот и они",
                                            "random_id": random.randint(1, 2147483647)})
            else:
                vk.method("messages.send",
                          {"peer_id": id, "keyboard": keyboard,
                           "message": "🤓Для большего удобства и экономии твоего времени мы сделали кнопки для общения с ботом\n😘Воспользуйся ими\n\n",
                           "random_id": random.randint(1, 2147483647)})
        elif data[str(id)]["power"] == 1:
            if body.lower() == "назад к главному меню":

                vk.method("messages.send",
                          {"peer_id": id, "keyboard": keyboard, "message": "Воспользуйся кнопками 👇🏻\n\n",
                           "random_id": random.randint(1, 2147483647)})
                construct(id, id, 0, 0)
            else:
                vk.method("messages.send",
                          {"peer_id": id, "keyboard": keyboard10, "message": "📗Автор книги?\n\n",
                           "random_id": random.randint(1, 2147483647)})
                # key = 2
                construct(id, id, 0, 2)


        elif data[str(id)]["power"] == 2:
            if body.lower() == "назад к главному меню":

                vk.method("messages.send",
                          {"peer_id": id, "keyboard": keyboard, "message": "Воспользуйся кнопками 👇🏻\n\n",
                           "random_id": random.randint(1, 2147483647)})
                construct(id, id, 0, 0)
            else:
                vk.method("messages.send",
                          {"peer_id": id, "keyboard": keyboard10, "message": "📘Краткое описание книги?\n\n",
                           "random_id": random.randint(1, 2147483647)})
                # key = 3
                construct(id, id, 0, 3)


        elif data[str(id)]["power"] == 3:
            if body.lower() == "назад к главному меню":

                vk.method("messages.send",
                          {"peer_id": id, "keyboard": keyboard, "message": "Воспользуйся кнопками 👇🏻\n\n",
                           "random_id": random.randint(1, 2147483647)})
                construct(id, id, 0, 0)
            else:
                vk.method("messages.send",
                          {"peer_id": id, "keyboard": keyboard,
                           "message": "Круто👍🏻\nСпасибо за то, что подарил книге новую жизнь❤🤗\n\n",
                           "random_id": random.randint(1, 2147483647)})

                construct(id, id, 0, 0)
        elif data[str(id)]["power"] == 4:
            if body.lower() == "назад к главному меню":

                vk.method("messages.send",
                          {"peer_id": id, "keyboard": keyboard, "message": "Воспользуйся кнопками 👇🏻\n\n",
                           "random_id": random.randint(1, 2147483647)})
                construct(id, id, 0, 0)
            else:
                give(body)



        savebd()






    except Exception as E:
        time.sleep(1)
