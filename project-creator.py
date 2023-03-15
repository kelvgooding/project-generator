# Modules

import os
from datetime import datetime
import shutil

# Variables

dt = datetime.today().strftime("%Y%m%d-%H%M%S")
user = os.getlogin()
path = fr"C:/Users/{user}/desktop/"

def automation_scripts():

    # Create project directory

    os.mkdir(os.path.join(path, f'automation-script-{dt}'))

    # Change directory

    os.chdir(os.path.join(path, f'automation-script-{dt}'))

    # Create sub-directories

    os.mkdir('build')
    os.mkdir('build/db')
    os.mkdir('build/scripts')
    os.mkdir('docs')
    os.mkdir('designs')

    # Create Virtual Environment

    os.system(r'python -m venv venv')

    # Create files

    with open("script.py", "w", ) as file1:
        file1.write('#!/usr/bin/env python3')

    with open("requirements.txt", "w", ) as file2:
        file2.write("")

    with open("config.ini", "w", ) as file3:
        file3.write("[DEFAULT]")

    # Move files

    shutil.move('script.py', 'build/')
    shutil.move('requirements.txt', 'build/')
    shutil.move('config.ini', 'build/')
    shutil.move('venv', 'build/')

def desktop_applications():
    # Create project directory

    os.mkdir(os.path.join(path, f'desktop-application-{dt}'))

    # Change directory

    os.chdir(os.path.join(path, f'desktop-application-{dt}'))

    # Create sub-directories

    os.mkdir('build')
    os.mkdir('build/db')
    os.mkdir('build/scripts')
    os.mkdir('build/ui')
    os.mkdir('docs')
    os.mkdir('designs')

    # Create Virtual Environment

    os.system(r'python -m venv venv')

    # Create files

    with open("script.py", "w", ) as file1:
        file1.write('#!/usr/bin/env python3')

    with open("requirements.txt", "w", ) as file2:
        file2.write("")

    with open("config.ini", "w", ) as file3:
        file3.write("[DEFAULT]")

    # Move files

    shutil.move('script.py', 'build/')
    shutil.move('requirements.txt', 'build/')
    shutil.move('config.ini', 'build/')
    shutil.move('venv', 'build/')

def static_websites():

    # Create project directory

    os.mkdir(os.path.join(path, f'static-website-{dt}'))

    # Change directory

    os.chdir(os.path.join(path, f'static-website-{dt}'))

    # Create several directories.

    os.mkdir('build')
    os.mkdir('build/static')
    os.mkdir('build/static/css')
    os.mkdir('build/static/images')
    os.mkdir('build/static/fonts')
    os.mkdir('build/templates')
    os.mkdir('designs')
    os.mkdir('docs')

    # Creating .html files

    with open("index.html", "w", ) as file1:
        file1.write("<!DOCTYPE html>\n")
        file1.write("<html>\n")
        file1.write("    <head>\n")
        file1.write('        <meta name="author" content="Kelv Gooding">\n')
        file1.write('        <meta name="viewport" content="width=device-width, initial-scale=1.0">\n')
        file1.write('        <link rel="icon" type="image/x-icon" href="">\n')
        file1.write('        <link rel="stylesheet" href="../static/css/styles.css">\n')
        file1.write("        <title>Home</title>\n")
        file1.write("    </head>\n")
        file1.write("    <body>\n")
        file1.write("        <header>\n")
        file1.write("        </header>\n")
        file1.write("        <main>\n")
        file1.write("        </main>\n")
        file1.write("        <footer>\n")
        file1.write("        </footer>\n")
        file1.write("    </body>\n")
        file1.write("</html>\n")

    # Create .css files

    with open("styles.css", "w", ) as file1:
        file1.write("body {\n")
        file1.write("    background-color: #FFFFFF;\n")
        file1.write("    font-size: 1em;\n")
        file1.write("    color: #000000;\n")
        file1.write("    margin: 0;\n")
        file1.write("    padding: 1.5em 1.5em 1.5em 1.5em;\n")
        file1.write("    text-align: center;\n")
        file1.write("}\n")

    # Move Files

    shutil.move('index.html', 'build/templates')
    shutil.move('styles.css', 'build/static/css')

def web_application():

    # Create project directory

    os.mkdir(os.path.join(path, f'web-application-{dt}'))

    # Change directory

    os.chdir(os.path.join(path, f'web-application-{dt}'))

    # Install Flask via PIP

    os.system('pip install flask')

    # Create several directories.

    os.mkdir('build')
    os.mkdir('build/static')
    os.mkdir('build/static/css')
    os.mkdir('build/static/images')
    os.mkdir('build/static/fonts')
    os.mkdir('build/templates')
    os.mkdir('designs')
    os.mkdir('docs')

    # Creating .html files

    with open("index.html", "w", ) as file1:
        file1.write("<!DOCTYPE html>\n")
        file1.write("<html>\n")
        file1.write("    <head>\n")
        file1.write('        <meta name="author" content="Kelv Gooding">\n')
        file1.write('        <meta name="viewport" content="width=device-width, initial-scale=1.0">\n')
        file1.write('        <link rel="icon" type="image/x-icon" href="">\n')
        file1.write('        <link rel="stylesheet" href="../static/css/styles.css">\n')
        file1.write("        <title>Home</title>\n")
        file1.write("    </head>\n")
        file1.write("    <body>\n")
        file1.write("        <header>\n")
        file1.write("        </header>\n")
        file1.write("        <main>\n")
        file1.write("        </main>\n")
        file1.write("        <footer>\n")
        file1.write("        </footer>\n")
        file1.write("    </body>\n")
        file1.write("</html>\n")

    # Create .css files

    with open("styles.css", "w", ) as file1:
        file1.write("body {\n")
        file1.write("    background-color: #FFFFFF;\n")
        file1.write("    font-size: 1em;\n")
        file1.write("    color: #000000;\n")
        file1.write("    margin: 0;\n")
        file1.write("    padding: 1.5em 1.5em 1.5em 1.5em;\n")
        file1.write("    text-align: center;\n")
        file1.write("}\n")

    # Creating ad-hoc files.

    with open('requirements.txt', 'w') as file:
        file.write('click==8.1.3\n')
        file.write('colorama==0.4.5\n')
        file.write('Flask==2.2.2\n')
        file.write('gunicorn==20.1.0\n')
        file.write('importlib-metadata==4.12.0\n')
        file.write('itsdangerous==2.1.2\n')
        file.write('Jinja2==3.1.2\n')
        file.write('MarkupSafe==2.1.1\n')
        file.write('Werkzeug==2.2.2\n')
        file.write('zipp==3.8.1\n')

    with open('Procfile', 'w') as file:
        file.write('web: gunicorn app:app')

    with open('app.py', 'w') as file:
        file.write('#!/usr/bin/env python3\n\n')
        file.write('from flask import Flask, render_template, request, flash\n\n')
        file.write('app = Flask(__name__)\n\n\n')
        file.write('@app.route("/")\n')
        file.write('def index():\n')
        file.write('    return render_template("index.html")')
        file.write('\n\n\n')
        file.write('if __name__ == "__main__":\n')
        file.write('    app.debug = True\n')
        file.write('    app.run(host="0.0.0.0", port=5000)')

    # Move Files

    shutil.move('index.html', 'build/templates')
    shutil.move('styles.css', 'build/static/css')
    shutil.move('app.py', 'build.')
    shutil.move('Procfile', 'build.')
    shutil.move('requirements.txt', 'build.')

def menu():

    print('------| PROJECT CREATOR |------\n')
    print("SELECT AN OPTION TO BEGIN PROJECT GENERATION:\n")
    print("1 | AUTOMATION SCRIPTS")
    print("2 | DESKTOP APPLICATIONS")
    print("3 | STATIC WEBSITES")
    print("4 | WEB APPLICATIONS")

    choice = input("\nENTER YOUR OPTION: ")

    if choice == "1":
        print('\n----------------------------')
        print("\nCREATING PROJECT - AUTOMATION SCRIPTS ..")
        automation_scripts()
        input("\nCOMPLETE! PRESS ANY KEY TO EXIT ..")
        os.startfile(os.path.join(path, f'automation-script-{dt}'))

    elif choice == "2":
        print('\n----------------------------')
        print("\nCREATING PROJECT - DESKTOP APPLICATIONS ..")
        desktop_applications()
        input("\nCOMPLETE! PRESS ANY KEY TO EXIT ..")
        os.startfile(os.path.join(path, f'desktop-application-{dt}'))

    elif choice == "3":
        print('\n----------------------------')
        print("\nCREATING PROJECT - STATIC WEBSITES ..")
        static_websites()
        input("\nCOMPLETE! PRESS ANY KEY TO EXIT ..")
        os.startfile(os.path.join(path, f'static-website-{dt}'))

    elif choice == "4":
        print('\n----------------------------')
        print("\nCREATING PROJECT - WEB APPLICATIONS ..")
        web_application()
        input("\nCOMPLETE! PRESS ANY KEY TO EXIT ..")
        os.startfile(os.path.join(path, f'web-application-{dt}'))

    else:
        print("INVALID OPTION. PLEASE TRY AGAIN.")
        menu()
menu()
