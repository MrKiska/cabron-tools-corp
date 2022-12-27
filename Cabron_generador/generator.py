from random import randint
import os

root = os.getcwd()

langs = {
    "english": "en_us",
    "russian": "ru_ru"
}




first = open(root+"/Cabron_generador/"+"first.txt").read().split('\n')
second =open(root+"/Cabron_generador/"+"second.txt").read().split('\n')
third = open(root+"/Cabron_generador/"+"third.txt").read().split('\n')

fem = ["а","ь","я"]
gay = ["е","о"]

useThird = False
def onStart():
    print("max: "+ str(len(first)*len(second)*len(third)))
    print("press enter to ")
    
def main():
    langCode = langs
    if input()=="":
        name=[]
        name.append(first[randint(0,len(first))-1])
        name.append(second[randint(0,len(second)-1)])
        if useThird:
            name.append(third[randint(0,len(third)-1)])
        if name[1][-1:] in fem:
            name[0] = name[0][:-2]+"ая"
        elif name[1][-1:] in gay:
            name[0] = name[0][:-2]+"ое"


        print(" ".join(str(i) for i in name))
        