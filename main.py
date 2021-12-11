# Для выполнения данного задания используется паттерн строитель (Builder)

class Pasta:
    def __init__(self):
        self.pasta_type = None
        self.sauce = None
        self.filling = []
        self.additive = []

    def __str__(self):
        return f"{self.__dict__}"


class IBuilder:
    def __init__(self):
        self.pasta = Pasta()

    def add_pasta_type(self):
        pass

    def add_sauce(self):
        pass

    def add_filling(self):
        pass

    def add_additive(self):
        pass

    def get_result(self):
        self.add_pasta_type()
        self.add_sauce()
        self.add_filling()
        self.add_additive()
        return self.pasta


class BologneseBuilder(IBuilder):
    def add_pasta_type(self):
        self.pasta.pasta_type = "spaghetti"

    def add_sauce(self):
        self.pasta.sauce = "bolognese"

    def add_filling(self):
        self.pasta.filling = "meat"

    def add_additive(self):
        self.pasta.additive.append("basil")


class CarbonaraBuilder(IBuilder):
    def add_pasta_type(self):
        self.pasta.pasta_type = "spaghetti"

    def add_sauce(self):
        self.pasta.sauce = "carbonara"

    def add_filling(self):
        self.pasta.filling.append("bacon")

    def add_additive(self):
        self.pasta.additive.append("egg")


class PestoBuilder(IBuilder):
    def add_pasta_type(self):
        self.pasta.pasta_type = "penne"

    def add_sauce(self):
        self.pasta.sauce = "pesto"

    def add_filling(self):
        pass

    def add_additive(self):
        self.pasta.additive.append("cheese")

class Director:
    def __init__(self):
        self.builder = BologneseBuilder()

    def change_builder(self, builder_name: str) -> None:
        if builder_name == "bolognese":
            self.builder = BologneseBuilder()
        elif builder_name == "carbonara":
            self.builder = CarbonaraBuilder()
        elif builder_name == "pesto":
            self.builder = PestoBuilder()
        else:
            raise ValueError(f"конструктора {builder_name} не сущесвтует. выберите другой.")

    def get_pasta(self):
        return self.builder.get_result()


def main():
    pasta_sheff = Director()
    print(pasta_sheff.get_pasta())

    pasta_sheff.change_builder("carbonara")
    print(pasta_sheff.get_pasta())

    pasta_sheff.change_builder("pesto")
    print(pasta_sheff.get_pasta())


if __name__ == "__main__":
    main()


