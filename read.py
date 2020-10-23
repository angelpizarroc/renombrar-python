import os
import configparser
import re

# detect the current working directory
path = os.getcwd()

def configs(file):
    if(os.path.exists(file)):
        config = configparser.ConfigParser()
        config.sections()
        config.read(file)
        #print(config['Game']['Title'])
        return config['Game']['Title']
def removeSpecialChars(chard):
    #ret = chard.replace("!@#$%^&*()[]{};:,./<>?\|`~-=_+", " ")
    s = re.sub(r"[-()\"#/@;:<>{}`+=~|.!?,]", "", chard)
    #words = ret.split()
    #print ("Words list: ", words[0:20])
    return s
    
def renamef(path,nuname,original):
    #removeSpecialChars = str.replace("!@#$%^&*()[]{};:,./<>?\|`~-=_+", " ")
    #final=path + "\\" + str(nuname).replace("!@#$%^&*()[]{};:,./<>?\|`~-=_+", " ").strip()
    final=path + "\\" + removeSpecialChars(str(nuname))
    original=str(path)+"\\" + str(original).strip()
    
    #print("Original:"+path+"\\" +original)
    #print("path:" + path)
    #print("[" + str(nuname) + "]")
    if final==original:
        print("::::" + original)
        print(" ")
    else:
        #print("renombrar")
        print(final)
        os.rename(original, final)
    #os.rename(path+"\\" +original,path + "\\" + final)
    

    
# read the entries
with os.scandir(path) as listOfEntries:
    for entry in listOfEntries:
        # print all entries that are files
        if entry.is_dir():
            #print(entry.name +"/Game.ini")
            try:
                renamef(path,configs(entry.name +"/Game.ini"), entry.name )
                #configs(entry.name +"/Game.ini")
            except:
                print("problema con " + configs(entry.name +"/Game.ini")) 
            
        
print(path)
#os.rename("tutorialsdir","tutorialsdirectory")
