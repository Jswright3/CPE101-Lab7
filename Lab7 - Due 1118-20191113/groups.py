# Lab 7
#
# Name: John Wright
# Instructor: Sussan Einakian
# Section: 101-05

def groups_of_3(list):
#splits list into nested lists of 3
#list -> list
   newlist = []
   i = 0
   while i+2 < len(list):
      newlist.append([list[i],list[i+1],list[i+2]])
      i += 3
   if i+1 < len(list):
      newlist.append([list[i],list[i+1]])
   elif i < len(list):
      newlist.append([list[i]])
   return newlist
