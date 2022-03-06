def arithmetic_arranger(problems):
  #function: arithmetic-formatter
  #problems = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
  maxsp = 6
  minsp = 2
  boljmpline = False
  firstrow, thirdrow, secoundrow, fourthrow, result = ([] for i in range(5))
  finalstr = str()
  
  # Error Validations:
  if (len(problems) > 5):
    return 'Error: Too many problems'
  
  for item in problems:
    argm = item.split()
    if not (argm[1] == "-" or argm[1] == "+"):
      return "Error: Operator must be '+' or '-'"

    if not (argm[0].isnumeric or argm[2].isnumeric):
      return "Error: Numbers must only contain digits"

    if len(argm[0]) > 4 or len(argm[2])>4:
      return "Error: Numbers cannot be more than four digits"
  
  #Built output string
  for item in problems:
    argm = item.split()
    firstrow.append((" " * (maxsp - len(argm[0]))) + argm[0] + "   ")
    secoundrow.append(argm[1] + (" " * (maxsp -1 - len(argm[1])-len(argm[2]))) + " " + argm[2]+ "   ")
    thirdrow.append("-" * maxsp + "   ")
    fourthrow.append((" " * (maxsp - len(str(eval(item))))) + (str(eval(item))) + "   ")

  firstrow.append("\n")
  secoundrow.append("\n")
  thirdrow.append("\n")

  result.append(firstrow)
  result.append(secoundrow)
  result.append(thirdrow)
  result.append(fourthrow)
  
  for sublist in result:
    for element in sublist:
      boljmpline = True
      finalstr = finalstr + element
      #print(element, end = " ")    
      
  return finalstr

print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))