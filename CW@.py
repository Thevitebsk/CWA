def run(code:str):
 s=[];p=0
 while p<len(code):
  if code[p]=="@":s.append(s[-1])
  elif code[p]=="#":s.pop()
  elif code[p]=="!":print(s[-1])
  elif code[p]==";":print(chr(s[-1]))
  elif code[p]=="+":s.append(s.pop()+1)
  elif code[p]=="-":s.append(s.pop()-1)
  elif code[p]=="?":s.append(int(input()))
  elif code[p]=="↷":s.insert(0,s.pop())
  p+=1
#Please note that the loop commands are beyond my coding skills, so i can't implement them
