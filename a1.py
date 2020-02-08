#f = open("temp.txt", "r") ## input file to test program
#s = f.read() ## store file content as string
s = "34 2345 3.14 6tgbsauhd9sa67*I{OPKDSl;jaklh;" #swap commenting with lines above to use, demo string for testing purpose ( also tested with temp file)
keywords = ['!','@','#','$','%','^','&','*','(',')','-','_','+','=',',',';',':','{',',}','[',']','"',"'",'~','`','.''<','>','?','/','\\','|','/']
## identify lexical keywords above
for element in s.split(): ## iterate through input string and set 
  if(element.isdigit()): ## check if element is a digit
      print(int(element))
  elif(element.isdecimal()): ## check if element has a floating point
    print(float(element))
  else:
    for char in element: ## iterate through rest of string for string and other keywords
      if char in keywords:
        p1 = element.index(char) 
        print(element[:p1])
        print(char)
        element = element[p1+1:] ## substring element to check for next keyword / string
    if(element != ""):
      print(element)
