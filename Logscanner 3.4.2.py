#import re
#import colorama
#from colorama import Fore, Style
#colorama.init(autoreset= True)

def descripor():
    print("")
    print(".......................")
    print("Attention Level:")
    print ("Medium Attention =",("!"))
    print ("High Attention  =", ("!!"))
    print(".......................")
    
def words():
    print("")
    print("__________________")
    print("")
    print("DETECTED WORDS")
    print("__________________")

def phrases():
    print("")
    print("__________________")
    print("")
    print("DETECTED PHRASES")
    print("__________________")

def wordcount(filename,listwords):
    try:
        file = open(filename,"r")
        read = file.readlines()
        file.close()
        
        for word in listwords:
            lower= word.lower()
            count =0
            alert =("!")
            Talert = ("!!")
            
            for sentance in read:
                line = sentance.split()
                for each in line:
                    line2 = each.lower()
                                                              
                    if lower == line2:
                             
                        count +=1
            if count >= 1 and count < 3:
                print((alert),":",lower,":","[",count,"]")
                   
            if count >= 3:
                print((Talert),":",lower,":","[",count,"]")           
           
                    
            
    except FileExistsError:
        print("The file is not there")
    except FileNotFoundError :
        print("No such file exists")        


def phrasecount():
    try:
        Talert = ("!!")
        words = ['under the table','if they find out', 'dont get caught','password bypass',
                 'junk packets','must be undetected','im going to corrupt']
        with open("logs 2.txt", 'r') as f:
            content = f.read()
# Iterate list to find each word
        for word in words:
            if word in content:
                print((Talert),':','"',word,'"','found in log')
                
    except FileExistsError:
         print("The file is not there")
    except FileNotFoundError :
         print("No such file exists")     



    
words()        
wordcount("logs 2.txt",['hack','hacking', 'infiltrate','pervade','spy','spoof','attack','ddos','backdoor'
                        ,'tailing','reconnaissance','recon','probe','steal','leak','dox'
                        ,'bruteforce','blackhat','greyhat','malware','virus','spyware','exploit'])

phrases()
phrasecount()
descripor()

   
