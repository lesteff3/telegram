import telebot
from telebot import types

import requests
from bs4 import BeautifulSoup as b
import random
import time

bot = telebot.TeleBot("5464738604:AAGD2mhq8iFF1TUR1vY1OyxDmr5rJF9kXxc")





@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Тааак вижу вам нужна моя помощь🆘')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Виды блюд🍕")
    markup.add(item1)
    item2 = types.KeyboardButton("Инструкция🔧")
    markup.add(item2)
    bot.send_message(message.chat.id, 'Выберите что вам надо', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def message_reply(message):
    if message.text =="Виды блюд🍕":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Горячее🍲")
        markup.add(item1)
        item2 = types.KeyboardButton("Салаты🥬")
        markup.add(item2)
        item3 = types.KeyboardButton("Десерты🥞")
        markup.add(item3)
        bot.send_message(message.chat.id, 'Выберите что вас интересует', reply_markup=markup)
    if message.text == "Горячее🍲":
        bot.send_message(message.chat.id, 'Так давай определим какие ингредиенты у вас есть❗')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Макароны1⃣')
        markup.add(btn1)
        btn2 = types.KeyboardButton('Картошка2⃣')
        markup.add(btn2)
        btn3 = types.KeyboardButton('Рис3⃣')
        markup.add(btn3)
        bot.send_message(message.chat.id, 'От этого уже буду отталкиваться🤔', reply_markup=markup)
        bot.send_message(message.chat.id, 'Выберите что на гарнир', reply_markup=markup)
    if message.text == 'Макароны1⃣':
        bot.send_message(message.chat.id, 'Хорошо🔥')
        pasta = types.ReplyKeyboardMarkup(resize_keyboard=True)
        pasta_btn1 = types.KeyboardButton('Курица🍗')
        pasta.add(pasta_btn1)
        pasta_btn2 = types.KeyboardButton('Рыба🍤')
        pasta.add(pasta_btn2)
        pasta_btn3 = types.KeyboardButton('Мясо🥩')
        pasta.add(pasta_btn3)
        pasta_btn4 = types.KeyboardButton('Виды блюд🍕')
        pasta.add(pasta_btn4)
        bot.send_message(message.chat.id, 'С чем хотите Макарошки ❓😍', reply_markup=pasta)
    if message.text == 'Виды блюд🍕':
        bot.register_next_step_handler(message.chat, message_reply)
    if message.text == 'Курица🍗':
        link = 'https://www.russianfood.com/'
        url = "https://www.russianfood.com/recipes/bytype/?fid=1109/recipes/recipe.php?rid=139317"
        response = requests.get(url)
        soup = b(response.text, 'html.parser')
        section = soup.find_all("div", class_='recipe_list_new')
        for products in section:
            product = products.find_all("div", class_='recipe_l in_seen v2')
            for items in product:
                item = items.find_all("div", class_='title_o')
                for cooking_pasta in item:
                    product_link = link + cooking_pasta.find("a").get('href')
                    all_products = f'{product_link}'
                    bot.send_message(message.chat.id, all_products)


    if message.text == 'Рыба🍤':
        link = 'https://www.russianfood.com/'
        url = "https://www.russianfood.com/recipes/bytype/?fid=16,1053"
        response = requests.get(url)
        soup = b(response.text, 'html.parser')
        section = soup.find_all("div", class_='recipe_list_new')
        for products in section:
            product = products.find_all("div", class_='recipe_l in_seen v2')
            for items in product:
                item = items.find_all("div", class_='title_o')
                for cooking_pasta in item:
                    product_link = link + cooking_pasta.find("a").get('href')
                    all_products = f'{product_link}'
                    bot.send_message(message.chat.id, all_products)


    if message.text == 'Мясо🥩':
        link = 'https://www.russianfood.com/'
        url = "https://www.russianfood.com/recipes/bytype/?fid=1107"
        response = requests.get(url)
        soup = b(response.text, 'html.parser')
        section = soup.find_all("div", class_='recipe_list_new')
        for products in section:
            product = products.find_all("div", class_='recipe_l in_seen v2')
            for items in product:
                item = items.find_all("div", class_='title_o')
                for cooking_pasta in item:
                    product_link = link + cooking_pasta.find("a").get('href')
                    all_products = f'{product_link}'
                    bot.send_message(message.chat.id, all_products)


    if message.text == 'Картошка2⃣':
        bot.send_message(message.chat.id, 'Хорошо🔥')
        pasta = types.ReplyKeyboardMarkup(resize_keyboard=True)
        pasta_btn1 = types.KeyboardButton('Курица🍖')
        pasta.add(pasta_btn1)
        pasta_btn3 = types.KeyboardButton('Мясо🥓')
        pasta.add(pasta_btn3)
        pasta_btn4 = types.KeyboardButton('Виды блюд🍕')
        pasta.add(pasta_btn4)
        bot.send_message(message.chat.id, 'С чем хотите Картошку❓😍', reply_markup=pasta)

    if message.text == 'Виды блюд🍕':
        bot.register_next_step_handler(message.chat, message_reply)

    if message.text == 'Курица🍖':
        link = 'https://www.russianfood.com/'
        url = "https://www.russianfood.com/recipes/bytype/?fid=937"
        response = requests.get(url)
        soup = b(response.text, 'html.parser')
        section = soup.find_all("div", class_='recipe_list_new')
        for products in section:
            product = products.find_all("div", class_='recipe_l in_seen v2')
            for items in product:
                item = items.find_all("div", class_='title_o')
                for cooking_pasta in item:
                    product_link = link + cooking_pasta.find("a").get('href')
                    all_products = f'{product_link}'
                    bot.send_message(message.chat.id, all_products)


    if message.text == 'Мясо🥓':
        link = 'https://www.russianfood.com/'
        url = "https://www.russianfood.com/recipes/bytype/?fid=1190"
        response = requests.get(url)
        soup = b(response.text, 'html.parser')
        section = soup.find_all("div", class_='recipe_list_new')
        for products in section:
            product = products.find_all("div", class_='recipe_l in_seen v2')
            for items in product:
                item = items.find_all("div", class_='title_o')
                for cooking_pasta in item:
                    product_link = link + cooking_pasta.find("a").get('href')
                    all_products = f'{product_link}'
                    bot.send_message(message.chat.id, all_products)


    if message.text == 'Рис3⃣':
        bot.send_message(message.chat.id, 'Хорошо🔥')
        pasta = types.ReplyKeyboardMarkup(resize_keyboard=True)
        pasta_btn1 = types.KeyboardButton('Курица😋')
        pasta.add(pasta_btn1)
        pasta_btn2 = types.KeyboardButton('Мясо😍')
        pasta.add(pasta_btn2)
        pasta_btn3 = types.KeyboardButton('Рыба🦪')
        pasta.add(pasta_btn3)
        pasta_btn4 = types.KeyboardButton('Виды блюд🍕')
        pasta.add(pasta_btn4)
        bot.send_message(message.chat.id, 'С чем хотите Рис❓😍', reply_markup=pasta)

    if message.text == 'Виды блюд🍕':
        bot.register_next_step_handler(message.chat, message_reply)


    if message.text == 'Курица😋':
        link = 'https://www.russianfood.com/'
        url = "https://www.russianfood.com/recipes/bytype/?fid=942"
        response = requests.get(url)
        soup = b(response.text, 'html.parser')
        section = soup.find_all("div", class_='recipe_list_new')
        for products in section:
            product = products.find_all("div", class_='recipe_l in_seen v2')
            for items in product:
                item = items.find_all("div", class_='title_o')
                for cooking_pasta in item:
                    product_link = link + cooking_pasta.find("a").get('href')
                    all_products = f'{product_link}'
                    bot.send_message(message.chat.id, all_products)


    if message.text == 'Мясо😍':
        link = 'https://www.russianfood.com/'
        url = "https://www.russianfood.com/recipes/bytype/?fid=14,1019"
        response = requests.get(url)
        soup = b(response.text, 'html.parser')
        section = soup.find_all("div", class_='recipe_list_new')
        for products in section:
            product = products.find_all("div", class_='recipe_l in_seen v2')
            for items in product:
                item = items.find_all("div", class_='title_o')
                for cooking_pasta in item:
                    product_link = link + cooking_pasta.find("a").get('href')
                    all_products = f'{product_link}'
                    bot.send_message(message.chat.id, all_products)


    if message.text == 'Рыба🦪':
        link = 'https://www.russianfood.com/'
        url = "https://www.russianfood.com/recipes/bytype/?fid=16,1019"
        response = requests.get(url)
        soup = b(response.text, 'html.parser')
        section = soup.find_all("div", class_='recipe_list_new')
        for products in section:
            product = products.find_all("div", class_='recipe_l in_seen v2')
            for items in product:
                item = items.find_all("div", class_='title_o')
                for cooking_pasta in item:
                    product_link = link + cooking_pasta.find("a").get('href')
                    all_products = f'{product_link}'
                    bot.send_message(message.chat.id, all_products)



    if message.text == "Салаты🥬":
        bot.send_message(message.chat.id, 'С салатами попроще❗')
        mark = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bt1 = types.KeyboardButton('С Морепродуктами1⃣')
        mark.add(bt1)
        bt2 = types.KeyboardButton('Праздничные2⃣')
        mark.add(bt2)
        bt3 = types.KeyboardButton('Легкие3⃣')
        mark.add(bt3)
        bt4 = types.KeyboardButton('Виды блюд🍕')
        mark.add(bt4)
        bot.send_message(message.chat.id, 'Нужно всего-то определиться с чем будет салат🥦', reply_markup=mark)




    if message.text == 'С Морепродуктами1⃣':
        link = 'https://www.russianfood.com/'
        url = "https://www.russianfood.com/recipes/bytype/?fid=1288"
        response = requests.get(url)
        soup = b(response.text, 'html.parser')
        section = soup.find_all("div", class_='recipe_list_new')
        for products in section:
            product = products.find_all("div", class_='recipe_l in_seen v2')
            for items in product:
                item = items.find_all("div", class_='title_o')
                for cooking_pasta in item:
                    product_link = link + cooking_pasta.find("a").get('href')
                    all_products = f'{product_link}'
                    bot.send_message(message.chat.id, all_products)


    if message.text == 'Праздничные2⃣':
        link = 'https://www.russianfood.com/'
        url = "https://www.russianfood.com/recipes/bytype/?fid=880"
        response = requests.get(url)
        soup = b(response.text, 'html.parser')
        section = soup.find_all("div", class_='recipe_list_new')
        for products in section:
            product = products.find_all("div", class_='recipe_l in_seen v2')
            for items in product:
                item = items.find_all("div", class_='title_o')
                for cooking_pasta in item:
                    product_link = link + cooking_pasta.find("a").get('href')
                    all_products = f'{product_link}'
                    bot.send_message(message.chat.id, all_products)


    if message.text == 'Легкие3⃣':
        link = 'https://www.russianfood.com/'
        url = "https://www.russianfood.com/recipes/bytype/?fid=1282"
        response = requests.get(url)
        soup = b(response.text, 'html.parser')
        section = soup.find_all("div", class_='recipe_list_new')
        for products in section:
            product = products.find_all("div", class_='recipe_l in_seen v2')
            for items in product:
                item = items.find_all("div", class_='title_o')
                for cooking_pasta in item:
                    product_link = link + cooking_pasta.find("a").get('href')
                    all_products = f'{product_link}'
                    bot.send_message(message.chat.id, all_products)




    if message.text == 'Десерты🥞':
        link = 'https://www.russianfood.com/'
        url = "https://www.russianfood.com/recipes/bytype/?fid=45"
        response = requests.get(url)
        soup = b(response.text, 'html.parser')
        section = soup.find_all("div", class_='recipe_list_new')
        for products in section:
            product = products.find_all("div", class_='recipe_l in_seen v2')
            for items in product:
                item = items.find_all("div", class_='title_o')
                for cooking_pasta in item:
                    product_link = cooking_pasta.find("a").get('href')
                    all_products = link + product_link
                    bot.send_message(message.chat.id, all_products)





bot.infinity_polling()