import random

def primary():

 f = open("quotes.txt")
 quotes = f.readlines()
 #f.write("Don't delete existing data \n")
 f.close()
 
 #f = open("quotes.txt", "r")
 
 last = len(quotes) -1
 rnd1 = random.randint(0, last)
 rnd2 = random.randint(0, last)
 
 
 print(quotes[rnd1], quotes[rnd2], sep="\n")
 
 #print(quotes[rnd1], end =" "),
 #print(quotes[rnd2])
 
 #mylist = [quotes[rnd1], quotes[rnd2]]
 #for i in mylist:
 #  print (i, end=" ")

if __name__== "__main__":
 primary()
