import unittest
def divide(a,b):
   div= a/b
   return div
print(divide(56,2))

class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(divide(9,3), 3)
