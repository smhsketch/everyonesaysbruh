import subprocess
from time import sleep
import os


file = open("/home/sketch/Projects/everyonesaysbruh/ethnicgroups.txt", "r")
wordsList = file.readlines()
file.close()

for i in range(1482):
    wordsList[i] = (wordsList[i])[:-1] # removes the \n from each word

for i in range(1550):
    currentwordfile = open("/home/sketch/Projects/everyonesaysbruh/currentword.txt", "r+")
    currentword = currentwordfile.readlines()
    currentword = currentword[0]
    currentwordfile.write("1")
    currentwordcount = len(currentword)

    wordOutput = wordsList[currentwordcount]
    bashCommand = "twurl -d 'status="+wordOutput+" be like: bruh"+"' /1.1/statuses/update.json"
    # bashCommand = "echo "+wordOutput

    os.system(bashCommand)

    currentwordfile.close()
    
    sleep(1800)


# bashCommand = "twurl -d 'status=bruh' /1.1/statuses/update.json"
process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)

# twurl -d 'status=bruh' /1.1/statuses/update.json
