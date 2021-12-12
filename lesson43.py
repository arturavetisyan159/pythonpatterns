# структурные паттерны проектирования.

from random import random, randint

# Адаптер, Adapter
class Application:
    def calc_smth(self, one: int, two: int) -> int:
        if isinstance(one, int) and isinstance(two, int):
            return one + two
        else:
            raise ValueError('Всё сломалось!')


class FloatNumber:
    def get_number(self) -> float:
        return random() * 10


class StrNumber:
    def get_number(self) -> str:
        return str(randint(1, 10))


class Adapter:
    def __init__(self, source):
        if source == 'float':
            self.source = FloatNumber()
        elif source == 'str':
            self.source = StrNumber()
        else:
            raise ValueError('Передано не то!')

    def get_number(self) -> int:
        return int(self.source.get_number())


# Фасад, Facade
class Kitchen:
    def prepare_food(self):
        print('Еда готовится')

    def give_food(self):
        print('Еда готова, забирайте!')


class Waiter:
    def take_order(self, client):
        print(f'Официант принял заказ у клиента {client.get_name()}')

    def send_oreder_to_kitchen(self):
        print('Официалнт передал заказ на кухню')

    def serve_order_to_client(self, client):
        print(f'Блюда готовы и переданы клиенту {client.get_name()}')


class Client:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def request_menu(self, menu):
        print(f'Клиент ознакамливается с меню {menu}')

    def make_order(self):
        print('Клиент делает заказ')

    def eat_food(self):
        print(f'Клиент {self.__name} ест свою еду')


class RestaurantFacade:
    def __init__(self):
        self.kitchen = Kitchen()
        self.waiter = Waiter()
        self.menu = {
            'веган': 'вегетарианское меню',
            'мясоед': 'мясное меню',
            'всеед': 'меню с мясом и зеленью'
        }

    def get_menu(self, type):
        return self.menu[type]

    def take_order(self, client):
        self.waiter.take_order(client)
        self.waiter.send_oreder_to_kitchen()
        self.kitchen_work()
        self.waiter.serve_order_to_client(client)

    def kitchen_work(self):
        self.kitchen.prepare_food()
        self.kitchen.give_food()


def main():
    # adapter = Adapter('str')
    # app = Application()
    #
    # one = adapter.get_number()
    # two = adapter.get_number()
    #
    # print(app.calc_smth(one, two))

    client = Client('Вася')
    restaurant = RestaurantFacade()

    client.request_menu('веган')

    restaurant.take_order(client)
    client.eat_food()

if __name__ == "__main__":
    main()
