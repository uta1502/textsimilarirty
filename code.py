#!/usr/bin/python
import sys
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

name = input("Enter the institute name : ")
flag = 0

with open('data.txt', 'r') as searchfile:
	for line in searchfile:
		if (name.lower() in line.lower()):
			print (line)
			flag = 1

if(flag == 0):
	print("Sorry, the institute name you are trying to search does not exist in the database")