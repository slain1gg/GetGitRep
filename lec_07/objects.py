class Goat:
    def __init__(self):
        pass

    def pet(self):
        print('Mee')


# экземпляр  кслаа = объект

# Класс - объединение(инкапсуляция) кода и данных (код + данные)
# Модуль - объединение(инкапсуляция) кода и данных (код + данные)

a = Goat()
b = Goat()
a.age = 5 # экземплярный атрибут
a.pet()
b.pet()

b.name = 'Mashka'
