# set up react project with vite + tailwind css

import os
import shutil
rootdir = os.getcwd()
print("Please wait...")
print("Setting up your react project with tailwind css")
os.system("npm create vite@latest")

print(os.listdir(os.getcwd()))
project = input("Select project to start with?: ")
os.chdir(os.getcwd()+"\\"+project)
os.system("npm install")
os.system("npm install -D tailwindcss postcss autoprefixer")
os.system("npx tailwind init -p")
print(os.getcwd())
if os.path.exists(os.getcwd()+"\\tailwind.config.js"):
    os.remove(os.getcwd()+"\\tailwind.config.js")
    print(os.getcwd())
    shutil.copy(rootdir+"\\tailwind.config.js",os.getcwd())
os.chdir(os.getcwd()+"\\src\\")
if os.path.exists(os.getcwd()+"\\index.css"):
    os.remove(os.getcwd()+"\\index.css")
    print(os.getcwd())
    shutil.copy(rootdir+"\\index.css",os.getcwd())