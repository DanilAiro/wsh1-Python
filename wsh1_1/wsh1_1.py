# Задание 1.

# Создать функцию с двумя обязательными аргументами (фамилия ученика, название предметы). 
# В функции должен находиться словарь вида {‘фамилия’: {‘предмет1’:[оценки], ‘предмет2’:[оценки]}}. 
# В словаре должно быть 3 ученика, у каждого ученика должно быть 4 предмета и 5 оценок. 
# Пользователю должен предоставляться выбор (1 - вывод всех оценок по предмету у ученика, 
# 2 - вывод среднего балла по этому предмету). 
# Реализовать каждый из вариантов.  

def show_marks(name: str, subject: str) -> None:
  my_dict = {
    'Бобров': {
      'Математика': [1, 2, 3, 4, 5, ], 
      'Русский':    [2, 2, 2, 2, 2, ], 
      'Змеиный':    [5, 5, 4, 5, 5, ], 
      'Физика':     [10, 8, 9, 10, 8]
    }, 
    'Найсдиктов': {
      'Математика': [5, 5, 4, 5, 5, ], 
      'Русский':    [1, 2, 3, 4, 5, ], 
      'Змеиный':    [2, 2, 2, 2, 2, ], 
      'Физика':     [3, 4, 5, 4, 3, ]
    },
    'Огузок': {
      'Математика': [2, 2, 2, 2, 2, ], 
      'Русский':    [3, 4, 5, 4, 3, ], 
      'Змеиный':    [5, 5, 4, 5, 5, ], 
      'Физика':     [1, 2, 3, 4, 5, ]
    }
  }

  marks = my_dict[name][subject]

  my_str = input('1 - вывод всех оценок по предмету у ученика\n2 - вывод среднего балла по этому предмету\nВаш выбор: ')
  match my_str:
    case '1':
      print(marks)
    
    case '2':
      print(sum(marks)/len(marks))
    case _:
      print('Нет такой команды')


show_marks(input('Введите фамилию: '), input('Введите предмет: '))