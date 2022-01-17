import unittest

import test

calcTestSuit = unittest.TestSuite()
calcTestSuit.addTest(unittest.makeSuite(test.TestCalculator))

runner = unittest.TextTestRunner(verbosity=1)
runer.run(calcTestSuit)



