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
        self.articles = []

    def add_article(self, dict_article: dict[str]): #json
        article = Article(*dict_article.values())
        self.articles.append(article)

    def get_all_articles(self):
        return self.articles



