import io

def loadFile(Directory: str):
    with io.open(Directory,"r") as file:
        return file.read()
    
def saveFile(Data,Name):
    with io.open(Name,"w") as file:
        file.writelines(Data)
        file.close()