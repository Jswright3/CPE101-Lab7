# Lab 7
#
# Name: John Wright
# Instructor: Sussan Einakian
# Section: 101-05
import sys

def main():
   args = sys.argv
   print(args)
   if len(args) ==  0:
      print('Usage: [-s] file_name')
      exit()
   floatcount = 0
   intcount = 0
   othercount = 0
   sum = 0
   try:
      for i in filename:
         try:
            i + 1
         except TypeError:
            othercount += 1
         
         try:
            i = int(i) 
         except ValueError:
            floatcount += 1

         try:
            i = float(i)
         except ValueError:
            intcount += 1

   except:
      print('Unable to open '+str(filename))
      exit()
   
   print('Ints: '+str(intcount))
   print('Floats: '+str(floatcount))
   print('Other: '+str(othercount))
   try:
      if len(args)>2 and args[2] == '-s':
          print("Sum: %.2f"%sum1)
   except:
      print('Usage [-s] file_name')
      exit()
   if __name__ == "__main__":
      main()
