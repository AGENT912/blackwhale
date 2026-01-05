import turtle
turtle.hideturtle()
import os
import subprocess
import platform
import sys
import math
import time

# Read config file
with open("HDI/config.conf", 'r', encoding='utf-8') as file:
    configdata = file.readlines()
file.close()

name_alias=[]
com_alias=[]
sys_build='BETA.020126.3'
sys_ver='β10'

def Cow_Herder(cow_list):
    if cow_list[0]=='index': # Index command
        index()

    elif cow_list[0]=='read': # Read txt file
        read(cow_list[1:])

    elif cow_list[0]=='open': # Open file with default application
        runfile(cow_list[1:])   

    elif cow_list[0]=='chdir' or cow_list[0]=='cd': # Change dir
        chdir(cow_list[1:])

    elif cow_list[0]=='exit': # For haters)
        turtle.clear()
        turtle.write('Wait 4 seconds')
        time.sleep(3)
        turtle.clear()
        turtle.write('Goodbye!')
        time.sleep(1)
        sys.exit()

    elif cow_list[0]=='help': # Help manual
        turtle.clear()
        turtle.goto(0, 0)
        turtle.write("HDI/BlackWhale HELP GUIDE")
        turtle.goto(0, -10)
        turtle.write('Commands:')
        turtle.goto(0, -20)
        turtle.write('  index 1                          - Show directory contents')
        turtle.goto(0, -30)
        turtle.write('  read  1  [name]                  - Read a text file')
        turtle.goto(0, -40)
        turtle.write('  open  1  [name]                  - Open a file with default app')
        turtle.goto(0, -50)
        turtle.write('  chdir 1  [path]                  - Change current directory')
        turtle.goto(0, -60)
        turtle.write('  cdir   1 [path]                  - Create dir')
        turtle.goto(0, -70)
        turtle.write('  cudir    1                       - Show current dir')
        turtle.goto(0, -80)
        turtle.write('  exit  1                          - Exit the program')
        turtle.goto(0, -90)
        turtle.write('  help 1                           - Show this guide')
        turtle.goto(0, -100)
        turtle.write('  delfile1 [name]                  - Delete file')
        turtle.goto(0, -110)
        turtle.write('  deldir  1[path]                  - Delete empty dir')
        turtle.goto(0, -120)
        turtle.write('  renm  1  [name] [new_name]       - Rename file or dir')
        turtle.goto(0, -130)
        turtle.write('  copy  1  [scr]  [dest]           - Copy file')
        turtle.goto(0, -140)
        turtle.write('  about                           - About HDI')
        turtle.goto(0, -150)
        turtle.write('  log     [text]                  - Log text to console')
        turtle.goto(0, -160)
        turtle.write('  fms     [name]                  - Run FMS script')
        turtle.goto(0, -170)
        turtle.write('  py      [type] [name/str]|[str] - Run python file or code')
        turtle.goto(0, -180)
        turtle.write('  alias   [name] [com]|[com]      - Create alias for command or commands group')
        turtle.goto(0, -190)
        turtle.write('  calc    [expr]                  - Calculate mathematical expression,' \
        'also with python operands and functions with math lib')
            
            #FINALLY, THE END OF THIS NIGHTMARE!!!

    elif cow_list[0]=='delfile': # Delete file
        delfile(cow_list[1:])

    elif cow_list[0]=='deldir': # Delete dir
        deldir(cow_list[1:])

    elif cow_list[0]=='renm': # Rename file or dir
        rename(cow_list[1:])

    elif cow_list[0]=='cdir': # Create dir
        cdir(cow_list[1:])

    elif cow_list[0]=='cudir': # Show current dir
        turtle.clear()
        turtle.write('Current dir:   ',os.getcwd())

    elif cow_list[0]=='copy': # Copy file
        copy(cow_list[1:])
    
    #UFO has written this text
    
    elif cow_list[0]=='about' or cow_list[0]=='screenfetch': # About HDI
        turtle.clear()
        turtle.goto(0, 0)
        turtle.write('▓▓▓▓▓▓▓▓▓▓▓▓▒')
        turtle.goto(0, -1)
        turtle.write('▓           ▒',)
        turtle.goto(0, -2)
        turtle.write('▓ HDI       ▒')
        turtle.goto(0, -3)
        turtle.write('▓ ────      ▒','       HDI', sys_ver)
        turtle.goto(0, -4)
        turtle.write('▓ $         ▒')
        turtle.goto(0, -5)
        turtle.write('▓           ▒')
        turtle.goto(0, -6)
        turtle.write('▒▒▒▒▒▒▒▒▒▒▒▒▒')
        turtle.goto(0, -10)
        turtle.write(' HDI it`s a simple open sourse console file manager based on Python3')
        turtle.goto(0, -20)
        turtle.write('Developers:')
        turtle.goto(0, -21)
        turtle.write('  Tr37')
        turtle.goto(0, -22)
        turtle.write('  Sairsay')
        turtle.goto(0, -23)
        turtle.write('  AGENT912')
        turtle.goto(0, -33)
        turtle.write('Source code: github.com/Vladislaus-37/HDI')
        turtle.goto(0, -34)
        turtle.write('Site       : sites.google.com/view/hdi-fms')
        turtle.goto(0, -44)
        print('Build:   ', sys_build)

    elif cow_list[0]=='log': # Log to console
        turtle.clear()
        turtle.write(' '.join(cow_list[1:]).rstrip('\n'))
    
    elif cow_list[0]=='fms': # Run FMS script
        fms(cow_list[1])

    elif cow_list[0]=='py': # Run python file or strings
        pyexe(cow_list[1:])

    elif cow_list[0]=='alias': # Create Alias
        add_alias(cow_list[1:])

    elif cow_list[0]=='calc': # Calculate mathematical expression
        try:
            result=eval(' '.join(cow_list[1:]))
            turtle.clear()
            turtle.write(str(result))
        except ZeroDivisionError:
            turtle.write('0')
        except NameError or ModuleNotFoundError:
            turtle.write('Python function or variable is not found')
        except SyntaxError:
            turtle.write('Bro, your syntax sucks')
        except Exception as err:
            turtle.write(+str(err))

    elif cow_list[0]=='' or cow_list[0]=='\n' or cow_list[0]=='#': # For comment in FMS and white lines
        123

    else: # This SYNTAX else)
        run_alias(cow_list)
    return 0

def index():    # Index command
    try:
        turtle.clear()
        turtle.goto(0, 0)
        turtle.write('Contents of', os.getcwd()) 
        turtle.goto(0, -10)
        turtle.write('------------------------------------------------------------------')
        turtle.goto(0, -20)
        turtle.write('| Type  | Name            | Size                                 |')
        turtle.goto(0, -30)
        turtle.write('|-------|-----------------|--------------------------------------|')
        
        y_pos = -40
        for item in os.listdir():
            if os.path.isfile(item):
                turtle.goto(0, y_pos)
                turtle.write('| File: | ' + item[:15].ljust(15) + ' | ' + str(os.path.getsize(item)).ljust(36) + ' |')
                y_pos -= 10
            elif os.path.isdir(item):
                turtle.goto(0, y_pos)
                turtle.write('| Dir:  | ' + item[:15].ljust(15) + ' | ' + str(os.path.getsize(item)).ljust(36) + ' |')
                y_pos -= 10
        
        turtle.goto(0, y_pos)
        turtle.write('------------------------------------------------------------------')
    except:
        turtle.clear()
        turtle.goto(0, 0)
        turtle.write('    INDEX_ERR')
        turtle.goto(0, -10)
        turtle.write('    May be path of dir is invalid')
        turtle.goto(0, -20)
        turtle.write('    Or your system is do not supported')
    return 0

def read(File):     # Read txt file
    try:
        with open(File[0].rstrip('\n'), 'r') as file:
            contenta = file.read()
        turtle.clear()
        turtle.goto(0, 0)
        turtle.write('------------------')
        turtle.goto(0, -10)
        turtle.write(' ')
        turtle.goto(0, -20)
        turtle.write(contenta)
        turtle.goto(0, -30)
        turtle.write(' ')
        turtle.goto(0, -40)
        turtle.write('------------------')
        turtle.goto(0, -50)
        turtle.write('')
        file.close()
    except:
        turtle.clear()
        turtle.goto(0, 0)
        turtle.write('    READ_ERR')
        turtle.goto(0, -10)
        turtle.write('    May be name of file is invalid')
        turtle.goto(0, -20)
        turtle.write('    Or your system is do not supported')
    return 0

def runfile(File):       # Run file
    try:
        filepath = os.getcwd() + "/" + File[0].rstrip('\n')
        if platform.system() == 'Darwin':       # for macOS
            subprocess.call(('open', filepath))
        elif platform.system() == 'Windows':    # for Windows
            os.startfile(filepath)
        else:                                   # for Pinguins
            subprocess.call(('xdg-open', filepath))
    except:
        turtle.clear()
        turtle.goto(0, 0)
        turtle.write('    OPEN_ERR')
        turtle.goto(0, -10)
        turtle.write('    May be name of file is invalid')
        turtle.goto(0, -20)
        turtle.write('    Or your system is do not supported')
    return 0

def chdir(File):        # Change dir
    try:
         os.chdir(File[0].rstrip('\n'))
         turtle.clear()
         turtle.goto(0, 0)
         turtle.write('Directory changed to: ' + os.getcwd())
    except:
        turtle.clear()
        turtle.goto(0, 0)
        turtle.write('    CHDIR_ERR')
        turtle.goto(0, -10)
        turtle.write('    May be path of dir is invalid')
        turtle.goto(0, -20)
        turtle.write('    Or your system is do not supported')
    return 0

def delfile(File):       # Delete flie
    try:
        os.remove(File[0].rstrip('\n'))
        turtle.clear()
        turtle.goto(0, 0)
        turtle.write('File deleted: ' + File[0])
    except:
        turtle.clear()
        turtle.goto(0, 0)
        turtle.write('    DEL_FILE_ERR')
        turtle.goto(0, -10)
        turtle.write('    May be path of file is invalid')
        turtle.goto(0, -20)
        turtle.write('    Or your system is do not supported')
    return 0

def deldir(File):       # Delete dir
    dirpath=File[0].rstrip('\n')
    try:
        os.rmdir(dirpath)
        turtle.clear()
        turtle.goto(0, 0)
        turtle.write('Directory deleted: ' + dirpath)
    except:
        turtle.clear()
        turtle.goto(0, 0)
        turtle.write('    DEL_DIR_ERR')
        turtle.goto(0, -10)
        turtle.write('    May be name of dir is invalid')
        turtle.goto(0, -20)
        turtle.write('    Or your dir is not empty')
        turtle.goto(0, -30)
        turtle.write('    Or your system is do not supported')
    return 0

def rename(File):
    try:
        os.rename(File[0].rstrip('\n'), File[1].rstrip('\n'))
        turtle.clear()
        turtle.goto(0, 0)
        turtle.write('Renamed: ' + File[0] + ' -> ' + File[1])
    except:
        turtle.clear()
        turtle.goto(0, 0)
        turtle.write('    RENAME_ERR')
        turtle.goto(0, -10)
        turtle.write('    May be path of file is invalid')
        turtle.goto(0, -20)
        turtle.write('    Or your system is do not supported')
    return 0

def cdir(File):     # Create dir
    try:
        os.mkdir(''.join(File[0]).rstrip('\n'))
        turtle.clear()
        turtle.goto(0, 0)
        turtle.write('Directory created: ' + File[0])
    except:
        turtle.clear()
        turtle.goto(0, 0)
        turtle.write('    CREATE_DIR_ERR')
        turtle.goto(0, -10)
        turtle.write('    May be path of new dir is invalid')
        turtle.goto(0, -20)
        turtle.write('    Or your system is do not supported')
    return 0

def copy(File):     # Copy file
    src = File[0].rstrip('\n')
    dest = File[1].rstrip('\n')
    turtle.clear()
    turtle.goto(0, 0)
    turtle.write('Copying: ' + src + ' -> ' + dest) 
    try:
        if platform.system() == 'Darwin':       # for macOS
            subprocess.call(('cp', src, dest))
        elif platform.system() == 'Windows':    # for Windows
            subprocess.call(('cmd', '/c', 'copy', src, dest))
        else:                                   # for Pinguins
            subprocess.call(('cp', src, dest))
        turtle.goto(0, -10)
        turtle.write('Copy completed!')
    except:
        turtle.clear()
        turtle.goto(0, 0)
        turtle.write('    COPY_ERR')
        turtle.goto(0, -10)
        turtle.write('    May be name of file is invalid')
        turtle.goto(0, -20)
        turtle.write('    Or your system is do not supported')
    return 0

# Run fms script
def fms(path):
    try:
        with open(path+'.fms', 'r', encoding='utf-8') as file:
            script = file.readlines()
            file.close()
        for i in script:
            Cow_Herder(i.rstrip('\n').split(' '))
    except:
        turtle.clear()
        turtle.goto(0, 0)
        turtle.write('    FSM_ERR')
        turtle.goto(0, -10)
        turtle.write('    May be name of script is invalid')
        turtle.goto(0, -20)
        turtle.write('    Or script will be wrong')

# Run py file or execute python strings
def pyexe(pyexe_pe):
    if pyexe_pe[0] == 'file':
        runfile([' '.join((pyexe_pe[1:]))])
    elif pyexe_pe[0] == 'exe':
        code_py=' '.join(pyexe_pe[1:]).split(' | ')
        try:
            for i in code_py:
                exec(i)
        except Exception as err:
            turtle.clear()
            turtle.goto(0, 0)
            turtle.write('    PY_ERR')
            turtle.goto(0, -10)
            turtle.write('    ' + str(err))
            turtle.goto(0, -20)
            turtle.write('    Check your code')
    return 0

# Create alias
def add_alias(name_com):
    global name_alias, com_alias
    name_alias.append(name_com[0])
    com_alias.append(str(' '.join(name_com[1:])).split(' | '))
    turtle.clear()
    turtle.goto(0, 0)
    turtle.write("Alias created: " + name_alias[-1])
    turtle.goto(0, -10)
    turtle.write("Commands: " + str(com_alias[-1]))
    return 0

# Run Alias code
def run_alias(name):
    global name_alias, com_alias
    if name[0] not in name_alias:
        turtle.clear()
        turtle.goto(0, 0)
        turtle.write('    SYNTAX_ERR')
        turtle.goto(0, -10)
        turtle.write('    Command not found: ' + name[0])
    else:
        comands=com_alias[name_alias.index(name[0])]
        for i in comands:
            Cow_Herder(i.split(' '))

# Run Part  
if sys.argv[-1]!=sys.argv[0]:
    if sys.argv[1]=='fms':
        fms(' '.join(sys.argv[2:]))

# by TR37 https://t.me/tr333777

# Настройки экрана
screen = turtle.Screen()
screen.bgcolor("grey")
screen.title("HDI/BlackWhale 0.1 (A)")

# Основная черепашка для текста
text_turtle = turtle.Turtle()
text_turtle.hideturtle()
text_turtle.penup()
text_turtle.speed(0)
text_turtle.color("black")

# Черепашка для подчеркивания
line_turtle = turtle.Turtle()
line_turtle.hideturtle()
line_turtle.penup()
line_turtle.speed(0)
line_turtle.color("black")
line_turtle.pensize(3)

# Список команд и их позиций с рассчитанной шириной
commands = []
font_name = "Arial"
font_size = 18
font_style = "normal"

# Функция для расчета ширины текста в пикселях
def get_text_width(text):
    return len(text) * font_size * 0.6  # Более точный расчет

# Новый список команд (18 команд)
# Разделим на две строки: первая 9 команд, вторая 9 команд
upper_row = ["index", "read", "open", "chdir", "cdir", "cudir", "exit", "help", "delfile"]
lower_row = ["deldir", "renm", "copy", "about", "log", "fms", "py", "alias", "calc"]

# Настройка позиционирования
start_x = -300  # начальная X координата для левого края
y_upper = 50     # Y координата для верхней строки
y_lower = -20    # Y координата для нижней строки
spacing = 100     # расстояние между командами

# Создаем верхнюю строку команд
for i, cmd_name in enumerate(upper_row):
    x = start_x + i * spacing
    commands.append({"name": cmd_name, "x": x, "y": y_upper})

# Создаем нижнюю строку команд
for i, cmd_name in enumerate(lower_row):
    x = start_x + i * spacing
    commands.append({"name": cmd_name, "x": x, "y": y_lower})

# Текущая позиция (индекс в списке команд)
current_position = 0

# Нарисовать все команды
def draw_commands():
    text_turtle.clear()
    for cmd in commands:
        text_width = get_text_width(cmd["name"])
        text_turtle.penup()
        text_turtle.goto(cmd["x"] - text_width/2, cmd["y"])
        text_turtle.pendown()
        text_turtle.write(cmd["name"], align="center", font=(font_name, font_size, font_style))
        text_turtle.penup()

# Нарисовать линию под текущей командой
def draw_line():
    line_turtle.clear()
    cmd = commands[current_position]
    text_width = get_text_width(cmd["name"])
    line_x = cmd["x"] - text_width/2
    line_x_end = cmd["x"] + text_width/2
    line_y = cmd["y"] - 10
    line_turtle.penup()
    line_turtle.goto(line_x, line_y)
    line_turtle.pendown()
    line_turtle.goto(line_x_end, line_y)
    line_turtle.penup()

# Функция для выполнения текущей команды
def execute_command():
    cmd_name = commands[current_position]["name"]
    
    # Визуальная обратная связь - мигание линии
    original_color = line_turtle.pencolor()
    for _ in range(2):
        line_turtle.pencolor("yellow")
        screen.update()
        time.sleep(0.1)
        line_turtle.pencolor(original_color)
        screen.update()
        time.sleep(0.1)
    
    # Скрыть меню перед выполнением команды
    text_turtle.clear()
    line_turtle.clear()
    
    # Выполнение команды
    if cmd_name == "index":
        Cow_Herder(["index"])
    elif cmd_name == "read":
        file_name = turtle.textinput("Read File", "Enter filename:")
        if file_name:
            Cow_Herder(["read", file_name])
    elif cmd_name == "open":
        file_name = turtle.textinput("Open File", "Enter filename:")
        if file_name:
            Cow_Herder(["open", file_name])
    elif cmd_name == "chdir":
        path = turtle.textinput("Change Directory", "Enter path:")
        if path:
            Cow_Herder(["chdir", path])
    elif cmd_name == "cdir":
        dir_name = turtle.textinput("Create Directory", "Enter directory name:")
        if dir_name:
            Cow_Herder(["cdir", dir_name])
    elif cmd_name == "cudir":
        Cow_Herder(["cudir"])
    elif cmd_name == "exit":
        Cow_Herder(["exit"])
    elif cmd_name == "help":
        Cow_Herder(["help"])
    elif cmd_name == "delfile":
        file_name = turtle.textinput("Delete File", "Enter filename to delete:")
        if file_name:
            Cow_Herder(["delfile", file_name])
    elif cmd_name == "deldir":
        dir_name = turtle.textinput("Delete Directory", "Enter directory name to delete:")
        if dir_name:
            Cow_Herder(["deldir", dir_name])
    elif cmd_name == "renm":
        old_name = turtle.textinput("Rename", "Enter old name:")
        if old_name:
            new_name = turtle.textinput("Rename", "Enter new name:")
            if new_name:
                Cow_Herder(["renm", old_name, new_name])
    elif cmd_name == "copy":
        src = turtle.textinput("Copy", "Enter source file:")
        if src:
            dest = turtle.textinput("Copy", "Enter destination:")
            if dest:
                Cow_Herder(["copy", src, dest])
    elif cmd_name == "about":
        Cow_Herder(["about"])
    elif cmd_name == "log":
        text = turtle.textinput("Log", "Enter text to log:")
        if text:
            Cow_Herder(["log", text])
    elif cmd_name == "fms":
        script_name = turtle.textinput("FMS Script", "Enter FMS script name:")
        if script_name:
            Cow_Herder(["fms", script_name])
    elif cmd_name == "py":
        py_type = turtle.textinput("Python", "Enter type (file/exe):")
        if py_type:
            if py_type == "file":
                file_name = turtle.textinput("Python File", "Enter Python filename:")
                if file_name:
                    Cow_Herder(["py", "file", file_name])
            elif py_type == "exe":
                code = turtle.textinput("Python Code", "Enter Python code:")
                if code:
                    Cow_Herder(["py", "exe", code])
    elif cmd_name == "alias":
        alias_name = turtle.textinput("Alias", "Enter alias name:")
        if alias_name:
            commands_str = turtle.textinput("Alias", "Enter commands (separated by |):")
            if commands_str:
                Cow_Herder(["alias", alias_name, commands_str])
    elif cmd_name == "calc":
        expression = turtle.textinput("Calculator", "Enter expression:")
        if expression:
            Cow_Herder(["calc", expression])
    
    # После выполнения команды ждем нажатия Esc для возврата в меню
    turtle.goto(0, -100)
    turtle.write("Press ESC to return to menu", align="center", font=("Arial", 12, "normal"))

# Функции для перемещения
def move_up():
    global current_position
    # Если мы в нижней строке, переходим на аналогичную позицию в верхней строке
    if current_position >= len(upper_row):
        # Вычисляем позицию в строке (0-8)
        pos_in_row = current_position - len(upper_row)
        current_position = pos_in_row
    else:
        # Если уже в верхней строке, остаемся на месте
        pass
    draw_commands()
    draw_line()

def move_down():
    global current_position
    # Если мы в верхней строке, переходим на аналогичную позицию в нижней строке
    if current_position < len(upper_row):
        # Вычисляем позицию в строке (0-8) и добавляем смещение для нижней строки
        pos_in_row = current_position
        current_position = pos_in_row + len(upper_row)
    else:
        # Если уже в нижней строке, остаемся на месте
        pass
    draw_commands()
    draw_line()

def move_right():
    global current_position
    # Определяем текущую строку
    current_row_start = 0
    current_row_end = len(upper_row)
    
    # Если мы в нижней строке
    if current_position >= len(upper_row):
        current_row_start = len(upper_row)
        current_row_end = len(commands)
    
    # Вычисляем позицию в текущей строке
    pos_in_row = current_position - current_row_start
    
    # Перемещаемся вправо (циклически)
    pos_in_row = (pos_in_row + 1) % (current_row_end - current_row_start)
    
    # Устанавливаем новую позицию
    current_position = current_row_start + pos_in_row
    
    draw_commands()
    draw_line()

def move_left():
    global current_position
    # Определяем текущую строку
    current_row_start = 0
    current_row_end = len(upper_row)
    
    # Если мы в нижней строке
    if current_position >= len(upper_row):
        current_row_start = len(upper_row)
        current_row_end = len(commands)
    
    # Вычисляем позицию в текущей строке
    pos_in_row = current_position - current_row_start
    
    # Перемещаемся влево (циклически)
    pos_in_row = (pos_in_row - 1) % (current_row_end - current_row_start)
    
    # Устанавливаем новую позицию
    current_position = current_row_start + pos_in_row
    
    draw_commands()
    draw_line()

# Функция для возврата в меню
def return_to_menu():
    # Очищаем экран
    turtle.clearscreen()
    
    
    # Восстанавливаем настройки экрана
    screen.bgcolor("grey")
    
    # Перерисовываем меню
    draw_commands()
    draw_line()
    screen.listen()
    screen.onkey(move_up, "Up")
    screen.onkey(move_down, "Down")
    screen.onkey(move_right, "Right")
    screen.onkey(move_left, "Left")
    screen.onkey(execute_command, "Return")  # Клавиша Enter/ВВОД
    screen.onkey(return_to_menu, "Escape")  # Клавиша ESC для возврата в меню

# Назначить клавиши для управления
screen.listen()
screen.onkey(move_up, "Up")
screen.onkey(move_down, "Down")
screen.onkey(move_right, "Right")
screen.onkey(move_left, "Left")
screen.onkey(execute_command, "Return")  # Клавиша Enter/ВВОД
screen.onkey(return_to_menu, "Escape")  # Клавиша ESC для возврата в меню

# Нарисовать все команды
draw_commands()

# Нарисовать начальную линию
draw_line()

# Основной цикл
screen.mainloop()

# By ÅGENT912 https://t.me/MonsieurHacker