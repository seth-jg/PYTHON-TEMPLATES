import os

def print_file_lines(name):
    file = open(name + ".txt", "r")
    for x in file.readlines():
        print(x)
    file.close()


def read_file(name):
    file = open(name + ".txt", "r")
    print(file.read())
    file.close()
#read_file("test")

def copy_file(name):
    file = open(name + ".txt", "r")
    fileContent = file.read()
    newFile = open("copy_of_" + name + ".txt", "w")
    newFile.write(fileContent)
    file.close()
    newFile.close()


def create_file(name, content):
    file = open(name + ".txt", "w")
    file.write(content)
    file.close()


def check_filename_with_content(name, content):
    if os.path.exists(name + ".txt"):
        file = open(name + ".txt", "r")
        line1 = file.readline()
        if line1 == content:
            return True
    else:
        return False

def file_existance(name):
    if os.path.exists(name + ".txt"):
        return True
    else:
        return False