class Book:
    def __init__(self, heading, author):
        self.__heading = heading
        self.__author = author

    def __repr__(self):
        return {"Название": f"{self.__heading}", "Автор": f"{self.__author}"}

    def get_heading(self):
        return self.__heading

    def get_author(self):
        return self.__author


class Reader:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def request_book(self, book):
        print(f"Читатель {self.__name} запросил книгу {book.get_heading()}")

    def reading(self, book):
        print(f"Читатель {self.__name} получил и читает книгу {book.get_heading()}")


class Librarian:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def add_book(self, book):
        print(f"Библиотекарь {self.__name} добавил книгу {book.get_heading()} в библиотеку.")

    def delete_book(self, book):
        print(f"Библиотекарь {self.__name} удалил из библиотеки книгу {book.get_heading()}")

    def take_order(self, reader):
        print(f"Библиотекарь {self.__name} взял заказ у читателя {reader.get_name()}")

    def give_order(self, reader, book):
        print(f"Библиотекарь {self.__name} отдал читателю {reader.get_name()} книгу {book.get_heading()}")


class Library:
    def __init__(self):
        self.collection = []

    def set_librarian(self, librarian):
        self.librarian = librarian

    def add_to_library(self, book):
        self.librarian.add_book(book)
        self.collection.append(book)

    def delete_from_library(self, book):
        if book in self.collection:
            self.collection.remove(book)
            self.librarian.delete_book(book)
        else:
            pass

    def show_collection(self):
        print("Коллекция библиотеки: ")
        for book in self.collection:
            print(f"{book.get_heading()} - {book.get_author()}")

    def take_order(self, reader, book):
        reader.request_book(book)
        if book in self.collection:
            self.librarian.take_order(reader)
            self.collection.remove(book)
            self.librarian.give_order(reader, book)
            reader.reading(book)
        else:
            print(f"Книги {book.get_heading()} на полках не оказалось.")



def main():
    book1 = Book("Над пропастью во ржи", "Селинджер")
    book2 = Book("Убить пересмешника", "Харпер Ли")
    book3 = Book("Старик и море", "Ернест Хемингуей")

    library = Library()
    librarian = Librarian("Гендальф")
    reader1 = Reader("Артур")

    library.set_librarian(librarian)

    library.add_to_library(book1)
    library.add_to_library(book2)
    library.add_to_library(book3)

    library.take_order(reader1, book3)

    print()

    library.show_collection()


if __name__ == "__main__":
    main()