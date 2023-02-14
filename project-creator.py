# Modules

from tkinter import *
import os
from datetime import datetime
import shutil
from tkinter import messagebox

# Tkinter Variables

root = Tk()
root.geometry("250x310")
root.title("Project Creator")
root.configure(bg='#5A5A5A')
root.columnconfigure(0, weight=1)
root.resizable(False, False)

# Variables

dt = datetime.today().strftime("%Y%m%d-%H%M%S")
user = os.getlogin()
path = fr"C:/Users/{user}/desktop/"
dir1 = fr"automation-script-{dt}"
dir2 = fr"desktop-application-{dt}"
dir3 = fr"static-website-{dt}"
dir4 = fr"web-application-{dt}"

def automation_scripts():

    messagebox.showinfo("Loading..", "Please wait whilst your project is being generated..")

    # Create project directory

    os.mkdir(os.path.join(path, dir1))

    # Change directory

    os.chdir(os.path.join(path, dir1))

    # Create sub-directories

    os.mkdir('build')
    os.mkdir('docs')
    os.mkdir('designs')
    os.mkdir('db')
    os.mkdir('scripts')

    # Create Virtual Environment

    os.system(r'python -m venv venv')

    # Create files

    with open("script.py", "w", ) as file1:
        file1.write("")

    with open("requirements.txt", "w", ) as file2:
        file2.write("")

    with open("config.ini", "w", ) as file3:
        file3.write("[DEFAULT]")

    messagebox.showinfo("Success!", "Your Automation Script project has now been created.")

    os.startfile(os.path.join(path, dir1))

def desktop_applications():
    # Create project directory

    os.mkdir(os.path.join(path, dir2))

    # Change directory

    os.chdir(os.path.join(path, dir2))

    # Create sub-directories

    os.mkdir('build')
    os.mkdir('docs')
    os.mkdir('designs')
    os.mkdir('db')
    os.mkdir('scripts')
    os.mkdir('UI')

    # Create Virtual Environment

    os.system(r'python -m venv venv')

    # Create files

    with open("script.py", "w", ) as file1:
        file1.write("")

    with open("requirements.txt", "w", ) as file2:
        file2.write("")

    with open("config.ini", "w", ) as file3:
        file3.write("[DEFAULT]")

    messagebox.showinfo("Success!", "Your Desktop Application project has now been created.")

    os.startfile(os.path.join(path, dir2))

def static_websites():
    # Create project directory

    os.mkdir(os.path.join(path, dir3))

    # Change directory

    os.chdir(os.path.join(path, dir3))

    # Create sub-directories

    os.mkdir('designs')
    os.mkdir('docs')
    os.mkdir('static')
    os.mkdir('static/css')
    os.mkdir('static/images')
    os.mkdir('static/fonts')
    os.mkdir('templates')

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

    shutil.move('index.html', 'templates')
    shutil.move('styles.css', 'static/css')

    messagebox.showinfo("Success!", "Your Static Website project has now been created.")

    os.startfile(os.path.join(path, dir3))

def web_application():
    # Create project directory

    os.mkdir(os.path.join(path, dir4))

    # Change directory

    os.chdir(os.path.join(path, dir4))

    # Install Flask via PIP

    os.system('pip install flask')

    # Create several directories.

    os.mkdir('designs')
    os.mkdir('docs')
    os.mkdir('static')
    os.mkdir('static/css')
    os.mkdir('static/images')
    os.mkdir('static/fonts')
    os.mkdir('templates')

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

    shutil.move('index.html', 'templates')
    shutil.move('styles.css', 'static/css')

    messagebox.showinfo("Success!", "Your Website Application project has now been created.")

    os.startfile(os.path.join(path, dir4))

# Tkinter Widgets

BTN1 = Button(text="Automation\nScripts", width='20', height='3', command=automation_scripts)
BTN1.grid(column=0, row=0, padx=10, pady=10)

BTN2 = Button(text="Desktop\nApplications", width='20', height='3', command=desktop_applications)
BTN2.grid(column=0, row=1, padx=10, pady=10)

BTN3 = Button(text="Static\nWebsites", width='20', height='3', command=static_websites)
BTN3.grid(column=0, row=2, padx=10, pady=10)

BTN4 = Button(text="Web\nApplications", width='20', height='3', command=web_application)
BTN4.grid(column=0, row=3, padx=10, pady=10)

root.mainloop()
