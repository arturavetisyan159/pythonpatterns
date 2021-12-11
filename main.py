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



###############################
# Абстрактная фабрика, Abstract Fabric

class FurninureFabric:
    @abstractmethod
    def create_table(self):
        pass

    @abstractmethod
    def create_sofa(self):
        pass


class ModernFurnitureFabric(FurninureFabric):
    def create_table(self):
        return ModernTable()

    def create_sofa(self):
        return ModernSofa()


class ArtDecoFurnitureFabric(FurninureFabric):
    def create_table(self):
        return ArtDecoTable()

    def create_sofa(self):
        return ArtDecoSofa()


class ITable:
    @abstractmethod
    def sit_to_the_table(self):
        pass


class ModernTable(ITable):
    def sit_to_the_table(self):
        print("сели за стол в дизайне модерн")


class ArtDecoTable(ITable):
    def sit_to_the_table(self):
        print("сели за стол в дизайне арт деко")


class ISofa:
    @abstractmethod
    def sit_on_the_sofa(self):
        pass


class ModernSofa(ISofa):
    def sit_on_the_sofa(self):
        print("сели на современный диван")


class ArtDecoSofa(ISofa):
    def sit_on_the_sofa(self):
        print("сели на диван в дизайне арт деко")


###########################
# паттерн строитель Builder


class Pizza:
    def __init__(self):
        self.testo = None
        self.sauce = None
        self.topping = []

    def __str__(self):
        return f"{self.__dict__}"


class IBuilder:
    def __init__(self):
        self.pizza = Pizza()

    def add_testo(self):
        pass

    def add_sauce(self):
        pass

    def add_topping(self):
        pass

    def get_result(self):
        self.add_testo()
        self.add_sauce()
        self.add_topping()
        return self.pizza


class MargaritaBuilder(IBuilder):
    def add_testo(self):
        self.pizza.testo = "Обычное тесто"

    def add_sauce(self):
        self.pizza.sauce = "томатный"

    def add_topping(self):
        self.pizza.topping.append("сыр")


class SalamiBuilder(IBuilder):
    def add_testo(self):
        self.pizza.testo = "Обычное тесто"

    def add_sauce(self):
        self.pizza.sauce = "томатный"

    def add_topping(self):
        self.pizza.topping.append("салями")
        self.pizza.topping.append("грибы")


class PizzaDirector:
    def __init__(self):
        self.builder = MargaritaBuilder()

    def change_builder(self, builder_name: str) -> None:
        if builder_name == "маргарита":
            self.builder = MargaritaBuilder()
        elif builder_name == "салями":
            self.builder = SalamiBuilder()
        else:
            raise ValueError(f"Переданного строителя {builder_name} не существует. Есть только маргарита и салями")

    def get_pizza(self) -> Pizza:
        return self.builder.get_result()


def main():
#     ground_logistic = GroundLogistics()
#     sea_logistic = SeaLogistics()
#
#     truck = ground_logistic.create_transport()
#     truck.deliver()

#################

#     boat = sea_logistic.create_transport()
#     boat.deliver()
#     modern_fabric = ModernFurnitureFabric()
#     art_deco_fabric = ArtDecoFurnitureFabric()
#
#     modern_table = modern_fabric.create_table()
#     modern_sofa = modern_fabric.create_sofa()
#     art_deco_table = art_deco_fabric.create_table()
#     art_deco_sofa = art_deco_fabric.create_sofa()
#
#     modern_table.sit_to_the_table()
#     modern_sofa.sit_on_the_sofa()
#     art_deco_table.sit_to_the_table()
#     art_deco_sofa.sit_on_the_sofa()

###################

    pizza_cooker = PizzaDirector()
    print(pizza_cooker.get_pizza())

    pizza_cooker.change_builder("салями")
    print(pizza_cooker.get_pizza())



if __name__ == '__main__':
    main()
