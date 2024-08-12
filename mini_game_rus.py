import requests

from bs4 import BeautifulSoup
from deep_translator import GoogleTranslator

# Создаём функцию, которая будет получать информацию
def get_english_words():
    url = "https://randomword.com/"
    try:
        response = requests.get(url)

        # Создаём объект Soup
        soup = BeautifulSoup(response.content, "html.parser")
        # Получаем слово. text.strip удаляет все пробелы из результата
        english_words = soup.find("div", id="random_word").text.strip()
        # Получаем описание слова
        word_definition = soup.find("div", id="random_word_definition").text.strip()
        # Чтобы программа возвращала словарь
        return {
            "english_words": english_words,
            "word_definition": word_definition
        }
    # Функция, которая сообщит об ошибке, но не остановит программу
    except:
        print("Произошла ошибка")


# Создаём функцию, которая будет делать саму игру
def word_game():
    translator = GoogleTranslator(source='en', target='ru')
    print("Добро пожаловать в игру")
    while True:
        # Используем результат функции-словаря
        word_dict = get_english_words()
        word = word_dict.get("english_words")
        word_definition = word_dict.get("word_definition")

        # Переводим слово на русский
        translated_word = translator.translate(word)
        translated_word_definition = translator.translate(word_definition)
        # Начинаем игру
        print(f"Значение слова - {translated_word_definition}")
        user = input(f"Что это за слово? \n")
        if user == translated_word:
            print("Все верно!")
        else:
            print(f"Ответ неверный, было загадано это слово - {translated_word}")

        # Возможность закончить игру
        play_again = input("Хотите сыграть еще раз? да/нет \n")
        if play_again != "да":
            print("Спасибо за игру!")
            break

if __name__ == "__main__":
    word_game()


