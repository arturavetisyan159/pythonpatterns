"""
Архитектурная часть Контроллер (Controller).

Обрабатывает изменения/запросы пользователя и связывает его с
Моделью и Представлением. Передаёт изменения пользователя в Модель,
получает от туда данные, после чего передаёт их в Представление,
благодаря чему пользователь видит изменения в интерфейсе программы.
"""

from model import ArticleBase
from view import UserInterface


class Controller:
    """
    Класс, содержащий методы, которые обрабатывают пользовательские запросы.

    В контроллере есть два объекта: база статей и интерфейс. Именно
    Контроллер заставляет работать Модель и Представление, обрабатывая
    пользовательские изменения, с помощью методов ниже.
    """
    def __init__(self):
        self.articles_base = ArticleBase()
        self.user_interface = UserInterface()

    def run(self):
        """
        Запускает основное тело программы.

        Это точка старта всей программы. Каждую итерацию цикла ждёт
        пользовательский ввод answer, после чего передаёт его в метод
        check_user_answer()
        """
        answer = None
        while answer != 'q':
            answer = self.user_interface.wait_user_answer()
            self.check_user_answer(answer)

    def check_user_answer(self, answer):
        """
        Проверяет пользовательский ввод.

        Принимает answer, как пользовательский ввод и определяет,
        как программа должна на него отреагировать.
        """
        if answer == '1':
            self.add_article()
        elif answer == '2':
            self.remove_article()
        elif answer == '3':
            self.show_article()
        elif answer == '4':
            self.show_all_articles()
        elif answer == 'q':
            self.safe_quit()
        else:
            self.show_incorrect_answer_error(answer)

    def add_article(self):
        """
        Добавляет статью в базу статей.

        Вызывает у Представления метод, который позволяет пользователю
        сформировать статью, после чего отдаёт сформированный article,
        являющийся словарём, в метод Модели, который добавляет статью.
        """
        article = self.user_interface.add_user_article()
        self.articles_base.add_article(article)

    def remove_article(self):
        """
        Удаляет из базы статей конкретную статью.

        Вызывает у Представления метод, который спрашивает у пользователя
        название статьи, после чего отдаёт полученное название методу Модели,
        который и удалит от туда статью.
        """
        user_title = self.user_interface.get_user_article()
        try:
            self.articles_base.remove_article(user_title)
        except KeyError:
            self.user_interface.show_incorrect_title_error(user_title)

    def show_article(self):
        """
        Показывает конкретную статью.

        Вызывает у Представления метод, который спрашивает у пользователя
        название статьи, затем достаёт из Модели всю информацию по ней,
        после чего вызывает у Представления метод, который отображает её.
        """
        user_title = self.user_interface.get_user_article()
        try:
            article = self.articles_base.get_article_by_title(user_title)
        except KeyError:
            self.user_interface.show_incorrect_title_error(user_title)
        else:
            self.user_interface.show_user_article(article)

    def show_all_articles(self):
        """
        Показывает все имеющиеся статьи в базе статей.

        В articles записывает все статьи из Модели, затем передаёт его в
        метод Представления, который отобразит все статьи как надо.
        """
        articles = self.articles_base.get_all_articles()
        self.user_interface.user_show_all_articles(articles)

    def show_incorrect_answer_error(self, answer):
        """
        Показывает ошибку о том, что пользователь ввел неправильное действие
        """
        self.user_interface.show_incorrect_answer_error(answer)

    def safe_quit(self):
        """
        Безопасный выход из программы.

        При безопасном выходе из программы состояние базы статей сохраняется.
        """
        self.articles_base.save_data()
