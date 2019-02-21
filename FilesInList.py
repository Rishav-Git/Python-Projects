# Store all file names in a list

path= input("Enter the path:")
jiles=[]
files = os.listdir(path)
for i in range(len(files)):
    jiles.append(os.path.join(path,files[i]))
