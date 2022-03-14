from multiprocessing.sharedctypes import Value


def arithmetic_arranger(problems, *args):
  #function: arithmetic-formatter

  # Error Validations:
  if (len(problems) > 5):
    return "Error: Too many problems."
  
  result = []
  for index, value in enumerate(problems):
    argm = value.split()
    
    #Error check
    if argm[1] not in "-+":
      return "Error: Operator must be '+' or '-'."
    
    if len(argm[0]) > 4 or len(argm[2])>4:
      return "Error: Numbers cannot be more than four digits."

    try:
      operator01 = int(argm[0])
      operator02 = int(argm[2])
    except ValueError:
      return "Error: Numbers must only contain digits."
      
    #Built output string
    #calculate biggest value:
    maxlng = max(len(argm[0]),len(argm[2]))
    maxspc = maxlng + 2

    firstline = f"{argm[0]:>{maxspc}}"
    secoundline = argm[1] + f"{argm[2]:>{maxspc-1}}"
    dsh = "-" * maxspc

    try:
      result[0] += (' '* 4) + firstline 
    except IndexError:
      result.append(firstline)

    try:
      result[1] += (' '* 4) + secoundline
    except IndexError:
      result.append(secoundline)

    try:
      result[2] += (' '* 4) + dsh
    except IndexError:
      result.append(dsh)

    if args:
      if argm[1] == "+":
        ans = int(argm[0]) + int(argm[2]) 
      else: 
        ans = int(argm[0]) - int(argm[2])
      a = f"{str(ans):>{maxspc}}"
      
      try:
        result[3] += (' ' * 4) + a
      except IndexError:
        result.append(a)
        
      output = f"{result[0]}\n{result[1]}\n{result[2]}"
      output = output + f"\n{result[3]}"
    else:
      output = f"{result[0]}\n{result[1]}\n{result[2]}"
  
  return output

desc = "restaurant and more food for dessert"
value = -15.89
if len(desc) >= 23:
  desc = desc[:23]
else:
  desc = f"{str(desc):>{23 - len(desc)}}"
if len(str(value))>5:
  endvalue = str(value)[:5]
else:
  endvalue = " " * (5 - len(str(value))) + str(value)

finalout = desc + " " + endvalue + "\n"
print(finalout)