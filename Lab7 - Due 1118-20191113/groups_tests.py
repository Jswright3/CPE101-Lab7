# Lab 7
#
# Name: John Wright
# Instructor: Sussan Einakian
# Section: 101-05

import unittest
from groups import *

class TestChar(unittest.TestCase):
   def test_groups_of_3(self):
      list1 = [1,2,3,4,5,6,7,8]
      list2 = [1,2,3,4,5,6,7,8,9]
      list3 = [1,2,3,4,5,6,7,8,9,10]
      self.assertEqual(groups_of_3(list1),[[1, 2, 3], [4, 5, 6], [7, 8]])
      self.assertEqual(groups_of_3(list2),[[1, 2, 3], [4, 5, 6], [7, 8, 9]])
      self.assertEqual(groups_of_3(list3),[[1, 2, 3], [4, 5, 6], [7, 8, 9], [10]])





if __name__ == '__main__':
   unittest.main()


