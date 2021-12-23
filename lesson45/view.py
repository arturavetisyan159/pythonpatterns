class UserInterface:
    def wait_user_answer(self):
        print(" Ввод пользователя ".center(40, "*"))
        print("Что хотим сделать со статьями?")
        print(
            "Возможные варианты:"
            "\n 1 - добавить статью"
            "\n 2 - посмотреть все статьи"
            "\n 3 - посмотреть конкретную статью"
            "\n 4 - удалить статью"
            "\n q - выйти из программмы"
        )
        user_answer = input("Выберите вариант действия: ")
        print("*" * 40)
        return user_answer

    def show_incorrect_answer_error(self, answer: str):
        print(" ОШИБКА! ".center(40, "*"))
        print(f"Варианта \"{answer}\" не существует!")
        print("*" * 40)

    def show_incorrect_title_error(self, user_title):
        print(" ОШИБКА! ".center(40, "*"))
        print(f"Статьи с названием \"{user_title}\" не существует!")
        print("*" * 40)

    def add_user_article(self):
        dict_article = {
            "Название": None,
            "Автор": None,
            "Количество страниц": None,
            "Источник": None,
            "Описание": None,
        }
        print(" Создание статьи ".center(40, "*"))
        for key in dict_article:
            dict_article[key] = input(f"Введите {key} статьи: ")
        print("*" * 40)
        return dict_article

    def show_all_articles(self, articles: list):
        print(" Список всех статей ".center(40, "*"))
        for idx, article in enumerate(articles, start=1):
            print(f"{idx}. {article}")
        print("*" * 40)

    def get_user_article(self):
        print(" Ввод названия статьи ".center(40, "*"))
        user_article = input("Введите название статьи: ")
        print("*" * 40)
        return user_article

    def show_user_article(self, article):
        print(" Статья найдена. Информация о статье ".center(40, "*"))
        for key in article:
            print(f"{key} - {article[key]}")
        print("*" * 40)








