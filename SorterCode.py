import os, shutil
path = r"C:/Users/zaraw/OneDrive/Documents/Python Tutorial/"
file_names = os.listdir(path)
folder_names = ['xlsx files', 'image files', 'text files']

for i in range(0,3):
    if not os.path.exists(path + folder_names[i]):
        print (path + folder_names[i])
        os.makedirs((path + folder_names[i]))
for file in file_names:
    if ".xlsx" in file and not os.path.exists(path + "xlsx files/" + file):
        shutil.move(path + file,path + "xlsx files/" + file)
    elif ".png" in file and not os.path.exists(path + "image files/" + file):
        shutil.move(path + file,path + "image files/" + file)
    elif ".txt" in file and not os.path.exists(path + "text files/" + file):
        shutil.move(path + file,path + "text files/" + file)
    elif ".csv" in file and not os.path.exists(path + "csv files/" + file):
        shutil.move(path + file,path + "csv files/" + file)
