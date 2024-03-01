score = input("Enter number :")
try:
 fscore = float(score)
except :
 print("Error, enter numerical values")
 quit()
if fscore == 0:
 print("Number is zero")
elif fscore < 0:
 print("Negative number")
elif fscore >= 0:
 print ("Number is positive")
