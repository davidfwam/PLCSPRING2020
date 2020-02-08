#f = open("temp.txt", "r") ## input file to test program
#s = f.read() ## store file content as string
s = "34 2345 3.14 6tgbsauhd9sa67*I{OPKDSl;jaklh;" #swap commenting with lines above to use, demo string for testing purpose ( also tested with temp file)
keywords = ['!','@','#','$','%','^','&','*','(',')','-','_','+','=',',',';',':','{',',}','[',']','"',"'",'~','`','.''<','>','?','/','\\','|','/']

for element in s.split(): ## iterate through input string and set 
  if(element.isdigit()):
      print(int(element))
  elif(element.isdecimal()):
    print(float(element))
  else:
    for char in element:
      if char in keywords:
        p1 = element.index(char)
        print(element[:p1])
        print(char)
        element = element[p1+1:]
    if(element != ""):
      print(element)
