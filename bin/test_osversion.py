"""Test osversion file
"""
from osversion import *

__author__ = "help@castellanidavide.it"
__version__ = "1.0 2020-9-18"

def test():
	"""Tests the osversion function in the osversion class
	Write here all test you want to do.
	REMEMBER to test your programm you can't use __init__ function
	"""
	assert osversion.osversion() == "osversion", "test failed"
	#assert osversion.<function>(<values>) == <the result(s) you would like to have>, "<the fail message>"
	
if __name__ == "__main__":
	test()
