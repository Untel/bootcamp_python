import sys
import string
import re

def text_analyzer(txt = None):
	"""This function counts the number of upper characters, lower characters,    punctuation and spaces in a given text.
"""
	if (txt == None):
		print("What is the text to analyse?")
		txt = input(">> ")
	reupper = re.compile("[A-Z]")
	upper = reupper.findall(txt)
	relower = re.compile("[a-z]")
	lower = relower.findall(txt)
	repunct = re.compile("[.,\/#!$%\^&\*;:{}=\-_`~()]")
	punct = repunct.findall(txt)
	respaces = re.compile("\s")
	spaces = re.findall(respaces, txt)
	print("The text contains " + str(len(txt)) + " characters:")
	print("- " + str(len(upper)) + " upper letters")
	print("- " + str(len(lower)) + " lower letters")
	print("- " + str(len(punct)) + " punctuation marks")
	print("- " + str(len(spaces)) + " spaces")

# text_analyzer("Python 2.0, released 2000, introduced features like List comprehensions and a garbage collection system capable of collecting reference cycles.")