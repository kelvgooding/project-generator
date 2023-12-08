"""
Author: Kelvin Gooding
Created: 2022-11-17
Updated: 2023-12-08
Version: 2.1.0
"""

# Modules

from datetime import datetime
from modules import create_file_system
import shutil
import os

# General Variables

username = os.path.split(os.path.expanduser("~"))[-1]
base_path = fr'C:/Users/{username}/desktop/'
dt_timestamp = datetime.today().strftime('%Y%m%d-%H%M%S')
file_timestamp = datetime.today().strftime('%Y-%m-%d')
dir_name = f'new_project_{dt_timestamp}'

# Script

def scripts():

    # Create dir(s)

    os.mkdir(os.path.join(base_path, dir_name))

    # Change dir(s)

    os.chdir(os.path.join(base_path, dir_name))

    # Create sub-dir(s)

    os.mkdir('build')
    os.mkdir('build/scripts')
    os.mkdir('build/modules')
    os.mkdir('build/docs')

    # Create .py file(s)

    with open("script.py", "w", ) as py_file:
        py_file.write('#!/usr/bin/python3\n\n')
        py_file.write('"""\n')
        py_file.write('Author: Kelv Gooding\n')
        py_file.write(f'Created: {file_timestamp}\n')
        py_file.write(f'Updated: {file_timestamp}\n')
        py_file.write('Version: 1.0.0\n')
        py_file.write('"""\n\n')
        py_file.write('# Modules\n\n\n')
        py_file.write('# Variables\n\n\n')
        py_file.write('# Script\n\n\n')

    create_file_system.file('requirements.txt', '')
    create_file_system.file('__init__.py', '')

    # Move file(s)

    shutil.move('script.py', 'build/')
    shutil.move('requirements.txt', 'build/')
    shutil.move('config.ini', 'build/')
    shutil.move('__init__.py', 'build/modules/')

def web_app():

    # Create base dir(s)

    os.mkdir(os.path.join(base_path, dir_name))

    # Change dir(s)

    os.chdir(os.path.join(base_path, dir_name))

    # Create sub-dir(s)

    os.mkdir('build')
    os.mkdir('build/static')
    os.mkdir('build/static/css')
    os.mkdir('build/static/img')
    os.mkdir('build/static/js')
    os.mkdir('build/static/fonts')
    os.mkdir('build/templates')
    os.mkdir('build/modules')
    os.mkdir('build/docs')

    # Create .html file(s)

    with open("index.html", "w", ) as html_file:
        html_file.write("<!DOCTYPE html>\n")
        html_file.write("<html>\n")
        html_file.write("    <head>\n")
        html_file.write('        <meta name="author" content="Kelv Gooding">\n')
        html_file.write('        <meta name="viewport" content="width=device-width, initial-scale=1.0">\n')
        html_file.write('        <link rel="icon" type="image/x-icon" href="">\n')
        html_file.write('        <link rel="stylesheet" href="../static/css/styles.css">\n')
        html_file.write("        <title>untitled</title>\n")
        html_file.write("    </head>\n")
        html_file.write("    <body>\n")
        html_file.write("        <header>\n")
        html_file.write("        </header>\n")
        html_file.write("        <main>\n")
        html_file.write("        </main>\n")
        html_file.write("        <footer>\n")
        html_file.write("        </footer>\n")
        html_file.write("    </body>\n")
        html_file.write("</html>\n")

    # Create .css file(s)

    with open("styles.css", "w", ) as css_file:
        css_file.write("body {\n")
        css_file.write("    background-color: #FFFFFF;\n")
        css_file.write("    font-size: 1em;\n")
        css_file.write("    color: #000000;\n")
        css_file.write("    margin: 0;\n")
        css_file.write("    padding: 1.5em 1.5em 1.5em 1.5em;\n")
        css_file.write("    text-align: center;\n")
        css_file.write("}\n")

    # Create app.py file(s)

    with open('app.py', 'w') as py_file:
        py_file.write('#!/usr/bin/python3\n\n')
        py_file.write('from flask import Flask, render_template, request, flash\n\n')
        py_file.write('# Flask Variables\n\n')
        py_file.write('app = Flask(__name__)\n\n\n')
        py_file.write('@app.route("/")\n')
        py_file.write('def index():\n')
        py_file.write('    return render_template("index.html")\n\n\n')
        py_file.write('if __name__ == "__main__":\n')
        py_file.write('    app.debug = True\n')
        py_file.write('    app.run(host="0.0.0.0", port=5000)')

    # Creating ad-hoc file(s)

    create_file_system.file('requirements.txt', f'Flask==3.0.0')
    create_file_system.file('__init__.py', '')

    # Move file(s)

    shutil.move('index.html', 'build/templates')
    shutil.move('styles.css', 'build/static/css')
    shutil.move('app.py', 'build.')
    shutil.move('requirements.txt', 'build.')
    shutil.move('__init__.py', 'build/modules/')

def menu():

    print('------| PROJECT GENERATOR |------\n')
    print('SELECT AN OPTION TO BEGIN:\n')
    print('1: SCRIPTS')
    print('2: WEB APP')

    choice = input("\nENTER YOUR OPTION: ")

    if choice == '1':
        print('\n----------------------------')
        print("\nCREATING PROJECT - 'SCRIPTS'")
        scripts()
        input("COMPLETE! PRESS ANY KEY TO EXIT ..")
        os.startfile(os.path.join(base_path, dir_name))

    elif choice == '2':
        print('\n----------------------------')
        print("\nCREATING PROJECT - 'WEB APP'")
        web_app()
        input("COMPLETE! PRESS ANY KEY TO EXIT ..")
        os.startfile(os.path.join(base_path, dir_name))

    else:
        print("INVALID OPTION. PLEASE TRY AGAIN.")
        menu()
menu()
