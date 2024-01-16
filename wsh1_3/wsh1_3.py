# Задание 3. 
# Создать интерфейс для регистрации в RPG. Пользователь, используя кнопки, должен выбрать следующие параметры персонажа:
# - Расу
# - Профессию 
# - Оружие
# После выбора на экран выводятся все параметры и характеристики (hp, damage).

import pygame
import menu

pygame.init()

WIDTH = 800
HEIGHT = 800
FPS = 30

character_info = {
    'name': None,
    'race': None,
    'prof': None,
    'health': 100,
    'damage': 20
}
new_info = False

def change_info(name, race, change_hp, change_dmg):
  character_info['name'] = name
  character_info['race'] = race
  character_info['health'] = change_hp
  character_info['damage'] = change_dmg
  global new_info
  new_info = True

def change_prof(prof):
  character_info['prof'] = prof
  global new_info
  new_info = True

text = None

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption("RPG")

startmenu = menu.Menu(screen)
racemenu = menu.Menu(screen)
profmenu = menu.Menu(screen)
applymenu = menu.Menu(screen)
applymenu.disable()
text = startmenu.add.text_input('Никнейм: ', default='username')
startmenu.add.button('Играть', racemenu)
startmenu.add.button('Выход', quit)

racemenu.add.label('Выберите расу')
racemenu.add.button('Эльф', lambda: change_info(text.get_value(),'Эльф', 150, 20))
racemenu.add.button('Гном', lambda: change_info(text.get_value(),'Гном', 80, 24))
racemenu.add.button('Человек', lambda: change_info(text.get_value(),'Человек', 100, 20))
racemenu.add.button('Далее', profmenu)

profmenu.add.label('Выберите профессию')
profmenu.add.button('Лучник', lambda: change_prof('Лучник'))
profmenu.add.button('Щитоносец', lambda: change_prof('Щитоносец'))
profmenu.add.button('Рыцарь', lambda: change_prof('Рыцарь'))
profmenu.add.button('Далее', applymenu)

info1 = applymenu.add.label(f'name - {character_info["name"]}')
info2 = applymenu.add.label(f'race - {character_info["race"]}')
info3 = applymenu.add.label(f'prof - {character_info["prof"]}')
info4 = applymenu.add.label(f'health - {character_info["health"]}')
info5 = applymenu.add.label(f'damage - {character_info["damage"]}')
applymenu.add.button('Подтвердить', quit)

run = True

while run:
  clock.tick(FPS)
  events = pygame.event.get()
  for event in events:
    if event.type == pygame.QUIT:
      run = False

  if new_info:
    new_info = False
    info1.set_title(f'name - {character_info["name"]}')
    info2.set_title(f'race - {character_info["race"]}')
    info3.set_title(f'prof - {character_info["prof"]}')
    info4.set_title(f'health - {character_info["health"]}')
    info5.set_title(f'damage - {character_info["damage"]}')

  screen.fill("#aaf0d1")
  startmenu.flip(events)
  
  pygame.display.flip()

pygame.quit()

