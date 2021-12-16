"""
Архитектурная часть Модель (Model).

Здесь хранятся данные, а также методы по работе с ними.
"""

import pickle  # dill
from pathlib import Path


class Article:
    """Описывает, как выглядит статья"""
    def __init__(self, title, author, pages, publish_source, description):
        self.title = title
        self.author = author
        self.pages = pages
        self.publish_source = publish_source
        self.description = description

    def __repr__(self):
        return f'{self.author}. "{self.title}"'


class ArticleBase:
    """
    Класс базы статей.

    Это обычный словарь вида {'название_статьи': 'объект_статьи'}.
    Благодаря такому подходу, мы имеем доступ к объекту статьи по её
    названию.
    """
    def __init__(self):
        self.articles = self.load_data()  # {'название_статьи': 'объект_статьи'}

    def add_article(self, dict_article):  # {'title': '123', 'author': '456', ...}
        """
        Добавляет статью в базу статей.

        Принимает article, как словарь, а затем распаковывает его
        значения в конструктор класса Article, после чего записывает
        в словарь созданный объект: {'название_статьи': 'объект_статьи'}.
        """
        article = Article(*dict_article.values())
        self.articles[article.title] = article

    def remove_article(self, title):
        """
        Удаляет статью из базы статей.

        Принимает title как имя статьи и использует это имя в методе pop().
        Если переданный ключ не найдётся, это означает, что статьи нет.
        """
        self.articles.pop(title)

    def get_article_by_title(self, user_title):
        """
        Возвращает статью со всей информацией по ней.

        Принимает title как имя статьи, после чего используя это имя как ключ,
        из словаря достаётся объект статьи и конструируется словарь, который и
        возвращается.
        """
        article = self.articles[user_title]
        article_dict = {
            'Название': article.title,
            'Автор': article.author,
            'Количество страниц': article.pages,
            'Источник': article.publish_source,
            'Описание': article.description,
        }
        return article_dict

    def get_all_articles(self):
        """
        Возвращает список статей.

        Каждая статья в этом списке будет иметь вид согласно их методу __repr__(), а
        именно ['автор_статьи. "название_статьи"', ...]
        """
        return self.articles.values()

    def save_data(self):
        """
        Сохраняет базу статей в отдельный файл.
        """
        with open('data.pkl', 'wb') as f:
            pickle.dump(self.articles, f)

    def load_data(self):
        """
        Загружает базу статей.

        Проверяет, существует ли файл с данными, если нет, тогда возвращает пустой словарь.
        """
        data_path = Path().cwd() / 'data.pkl'
        if data_path.exists():
            with open('data.pkl', 'rb') as f:
                return pickle.load(f)
        else:
            return dict()
