from tkinter import Tk
import os
import pathlib

root = Tk()

monitor_height = root.winfo_screenheight()
monitor_width = root.winfo_screenwidth()
# для определения пути к игре можно использовать переменную окружения, так как в облачном сервисе мы можем быть точно уверены, куда игра установится.
PATH_TO_GAME = 'C:/"Program Files (x86)"/Steam/steamapps/common/Underlords/game/bin/win64/underlords.exe'

path_to_config = pathlib.Path('C:/') / 'Program Files (x86)' / 'Steam' / 'steamapps'/ 'common'/ 'Underlords'/ 'game'/ 'dac'/ 'cfg'/ 'video.txt' 
# Можжно использовать инструментарий самой os с абсолютным путем, но по какой то причине мой пк ее не воспринимает. Возможно, что то делаю не так

with open(path_to_config, 'r', encoding=None) as config:

    x_split = config.readlines()

    count = 0 # Нужен для замены элемента по его индексу, это уменьшит количество запросов к списку
    for i in x_split:
        
        # В идеале тут должен быть поиск по регулярным выражениям, но их составлять я еще не пробовал. Обычно искал готовые, если была необходимость.
        if i.find("setting.defaultres") != -1:
            x_str = i[0: i.rfind('"', 0, -2) + 1] + str(monitor_width) + '"\n'
            x_split[count] = x_str
        if i.find("setting.defaultresheight") != -1:
            x_str = i[0: i.rfind('"', 0, -2) + 1] + str(monitor_height) + '"\n'
            x_split[count] = x_str
        
        count += 1

# Экранирование символов обратно и приведение конфиг-файла к исходному состоянию    
final = str(x_split)[1:-1].replace('\\t', '\t').replace('\\n', '\n').replace('\', \'', '').replace('\'', '')

with open(path_to_config, 'w', encoding="utf-8") as config:
    config.write(final)


cmd = f'{PATH_TO_GAME}'
os.system(cmd)


# также для этой задачи есть более простое решение - использовать параметры запуска, тогда нет необходимости вносить изменения в конфиг файл
# cmd = '%s -w %d -h %d' %(PATH_TO_GAME, monitor_width, monitor_height)
# os.system(cmd)
