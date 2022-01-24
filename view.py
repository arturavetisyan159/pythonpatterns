def index() -> str:
    """Вьюха, которая отдаёт html главной страницы."""
    with open('template/index.html') as template:
        return template.read()


def blog() -> str:
    """Вьюха, которая отдаёт html страницы с блогом."""
    with open('template/blog.html') as template:
        return template.read()

def info() -> str:
    with open('template/info.html') as template:
        return template.read()

def user() -> str:
    with open('template/user.html') as template:
        return template.read()

def error_404() ->str:
    with open('template/error_404.html') as temlpate:
        return template.read()
