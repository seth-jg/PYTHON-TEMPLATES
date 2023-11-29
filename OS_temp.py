import os

folderPath = "C:/Users/sethg/Documents/C# lessons"
listContent = os.listdir(folderPath)
print(listContent)

# Opens program
# use '"path"'
path = '"C:/Users/sethg/Desktop/Notepad.exe"'
# os.system(path)

# removes file
removePath = '"C:/Users/sethg/Desktop/Wiki/Seth.txt"'
# os.remove(removePath)