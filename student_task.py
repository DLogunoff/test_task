# Не стоит использовать имена переменных, которые являются или включают в себя
# тип используемых данных. Потому что при взгляде на значение переменной необходимость
# в дублировании этого в названии переменной отпадает.

# Этот метод можно записать более лаконичным образом, если воспользоваться collections.defaultdict
# или collections.Counter
# https://docs.python.org/3/library/collections.html#collections.defaultdict
# https://docs.python.org/3/library/collections.html#collections.Counter
def get_count_char(str_):
    # На самом деле можно не сохранять это значение в отдельной переменной.
    # Можно рассчитать и сразу использовать в цикле
    letters = str_.lower()
    # Другое название словарей - отображение. Они отображают ключ на значение.
    # Можно взять это во внимание и переименовать этот словарь.
    # Обычно пишут <смысл ключа>_to_<смысл значения>
    dictionary = {}
    # Переменным нужно давать более понятные имена.
    # Имен переменных, которые состоят из одной буквы стоит вовсе избегать
    for i in letters:
        if i.isalpha():
            # Если мы хотим проверить, является ли i ключом словаря, то можно убрать метод .keys(),
            # так как словарь представляется списком своих ключей для операций in (а также цикла for)
            if i in dictionary.keys():
                # Все вычисления можно записать в одну строчку, воспользовавшись комбинированным оператором сложения +=.
                # https://stackoverflow.com/questions/4841436/what-exactly-does-do
                count = dictionary[i]
                count += 1
                dictionary[i] = count
            else:
                dictionary[i] = 1
    return dictionary


def get_percent_correlation(str_):
    # Не совсем понятное имя переменной. Что такое cor и что это значит?
    cor = get_count_char(str_)
    summary = sum(cor.values())
    for key in cor:
        # Можно скомбинировать все вычисления и записать эти три строчки в одну
        cor[key] /= summary
        cor[key] *= 100
        # Из-за округления теряется точность. Сумма всех процентов должна быть равна 100, но
        # для указанной ниже строки она получается 95. Куда-то делось 5 процентов.
        cor[key] = round(cor[key])
    return cor


main_str = """
        Данное предложение будет разбиваться на отдельные слова. 
        В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список 
        отдельных слов. 
        Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join.
        Приступим!!!!
    """

# print(get_count_char(main_str))  # Вывод словаря "Буква" - "Количество"
print(get_percent_correlation(main_str))  # Вывод словаря "Буква" - "Процентное соотношение (данная буква/все буквы)"
