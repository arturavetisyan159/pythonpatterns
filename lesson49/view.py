def index() -> str:
    with open('template/index.html') as template:
        return template.read()


def blog() -> str:
    with open('template/blog.html') as template:
        return template.read()
