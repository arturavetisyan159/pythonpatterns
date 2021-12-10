# Паттерны проектирования
# Фабричный метод, Factory method, виртуальный конструктор

from abc import abstractmethod, ABC

class Logistics(ABC):
    @abstractmethod
    def create_transport(self):
        pass

    def connect_to_db(self):
        pass

    def get_data_from_db(self):
        pass


class GroundLogistics(Logistics):
    def create_transport(self):
        return Truck()


class SeaLogistics(Logistics):
    def create_transport(self):
        return Boat()


class ITransport():
    def deliver(self):
        pass


class Truck(ITransport):
    def deliver(self):
        print("Грузовик едет по суше")


class Boat(ITransport):
    def deliver(self):
        print("Лодка идет по воде")

# Абстрактная фабрика, Abstract Fabric


# def main():
#     ground_logistic = GroundLogistics()
#     sea_logistic = SeaLogistics()
#
#     truck = ground_logistic.create_transport()
#     truck.deliver()
#
#     boat = sea_logistic.create_transport()
#     boat.deliver()
#
# if __name__ == '__main__':
#     main()





