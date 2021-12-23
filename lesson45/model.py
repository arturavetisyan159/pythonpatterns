import pickle
from pathlib import Path



class Article:
    def __init__(self, title, author, pages, publlish_soure, description):
        self.title = title
        self.author = author
        self.pages = pages
        self.publish_source = publlish_soure
        self.description = description

    def __repr__(self):
        return f"{self.author}. \"{self.title}\""


class ArticleModel:
    def __init__(self):
        self.articles = self.load_data()

    def add_article(self, dict_article: dict[str]): #json
        article = Article(*dict_article.values())
        self.articles[article.title] = article

    def get_all_articles(self):
        return self.articles.values()

    def get_article_by_title(self, user_title):
        try:
            article = self.articles[user_title]
        except KeyError:
            raise ValueError
        else:
            dict_article = {
                "Название": article.title,
                "Автор": article.author,
                "Количество страниц": article.pages,
                "Источник": article.publish_source,
                "Описание": article.description,
            }
            return dict_article

    def delete_article(self, user_title):
        try:
            self.articles.pop(user_title)
        except KeyError:
            raise ValueError

    def load_data(self):
        db_path = Path().cwd() / "db.pkl" # склеиваем путь
        if db_path.exists():
            with open(db_path, "rb") as f:
                return pickle.load(f)
        else:
            return dict()

    def save_data(self):
        with open("db.pkl", "wb") as f:
            pickle.dump(self.articles, f)

