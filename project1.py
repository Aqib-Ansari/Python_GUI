import os,shutil

imageExtension = ('.png','.jpg','.jpeg','.svg')
normalFiles = ('.txt','.pdf','.csv')
msFiles = ('.docs','.xls','.pptx')
codeFiles = ('.c','.py','.html','.css','.js','.json','.c')

folderPath  = input("enter folder path : ")

def file_finder(folder_path,file_extension):
    files=[]
    for file in os.listdir(folder_path):
        for extension in file_extension:
            if file.endswith(extension):
                files.append(file)
    return files

print(file_finder(folderPath,normalFiles))