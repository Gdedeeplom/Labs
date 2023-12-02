# Создаём класс Alphabet
class Alphabet:
    # Создаём метод __init__(), внутри которого будут определены два динамических свойства 
    def __init__(self, lang, letters):
        self.lang = lang
        self.letters = letters
    # Создаём метод print(), который выведет в консоль буквы алфавита
    def print(self):
        print(self.letters)
    # Создаём метод letters_num(), который вернёт количество букв в алфавите
    def letters_num(self):
        print(len(self.letters))
# Создаём класс EngAlphabet путём наследования от класса Alphabet
class EngAlphabet(Alphabet):
# Создаём метод __init__(), внутри которого будет вызываться родительский метод __init__()
# В качестве параметров ему передаются обозначения языка ('En') и строка, состоящая из всех букв алфавита
    def __init__(self):
        Alphabet.__init__(self, lang = 'En', letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ')
# Добавляем приватное статическое свойство __letters__num, которое хранит количество букв в алфавите 
        self.__letters_num = (len(self.letters))
# Создаём метод is_in_letters(), он принимает букву в качестве параметра и определяет её принадлежность к алфавиту
    def is_in_letters(self, letter):
        print(letter in self.letters)
# Переопределяем метод letters_num(), в текущем классе он будет возвращать значение свойства letters_num
    def letters_num(self): 
        print(self.__letters_num)
# Создаём статический метод example(), он возвращает пример текста на английском языке
    def example(self):
        print('Price is hight.') 
# Создаём объект EngAlphabet 
n = EngAlphabet()
# Напечатаем буквы алфавита для этого объекта
n.print()
# Выведем количество букв в алфавите
n.letters_num()
# Проверим, относится ли буква F к английскому алфавиту
n.is_in_letters('F')
# Проверим, относится ли буква Щ к английскому алфавиту
n.is_in_letters('Щ')
# Выведем пример текста на английском языке