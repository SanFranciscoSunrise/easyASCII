#!/usr/bin/python3
#
# A simple python program to demonstrate writing numbers to the console
# in BIG ASCII style.
#

import sys
import os
import collections
import re
#import getopt
import argparse


def setup_ascii_dictionary(dictionary_file):

	# Open our acii character reprentation database.
	# translate it into a dictionary describing which position
	# each symbol/letter occurs at in our list that holds a set of
	# lists each holding 1 of 7 rows describing the ascii representation
	# of each symbol

	try:
		asciiCharacterDB = open(dictionary_file,"r")

		# The first line in our database is always a string of the letters that are being
		# represented. So we get our "alphabet" that will be used to create our
		# dictionary later {letter(key), drawingAs7RowList(value)}
		alphabet = asciiCharacterDB.readline()
		alphabet = re.findall("\S",alphabet)

		# The original DB had an extra line in between the characters and their
		# representation for readability.  So we move the pointer ahead one line
		asciiCharacterDB.readline()

		# File each row of each character into a list
		pixel_map = asciiCharacterDB.readlines()

	except:
		print("Error reading database file (check format)!")

	clean_pixel_map = []
	for i in pixel_map:
		clean_pixel_map.append(re.findall("(?<=\" \")[^\"]+",i))

	# Setup the dictionary using a dictinoary comprehension
	alphabet_dictionary = {character: number for number,
	                       character in enumerate(alphabet)}

	return alphabet_dictionary, clean_pixel_map


def write_ascii(phrase_to_translate, alphabet_dictionary, clean_pixel_map,
                output_file):

	# Main program, write ascii to screen :-)

	try:
		for row in range(7):    # iterate through every row of the screen

			line = ""

			# iterate through user input grabbing
			# each character and adding it's ascii representation
			# of the current row to the line we are on
			for column in range(len(phrase_to_translate)):
				keyValue = 0

				if phrase_to_translate[column] == ' ':
					line += '  '
				else:

					character = phrase_to_translate[column] # grab user input

					# lookup the position of
					# character in our dictionary
					# this should also match the position
					# of the character in the character database
					keyValue = alphabet_dictionary.get(character)    

					symbols = clean_pixel_map[row] # grab current row of every character from
								       # our database

					line += symbols[keyValue] # add the row of ascii for the current
						                  # character/column of our users input
								  # to the line we are on

			# print current line to the screen for the row we are on
			print(line)
			if output_file:
				output_to_file(output_file, line)

	except IndexError:
		print("Index Error!")

	except ValueError as err:
		print(err, "in", digit, " unacceptable value")

	except TypeError as err:
		print("Error: attempt to translate symbol not defined in current font file.")


def output_to_file(output_file, current_line):
	with open(output_file,'a') as outPut:
		outPut.write(current_line)
		outPut.write('\n')


def main():
	global dictionary_file
	global output_file
	global phrase_to_translate


	# The new way to parse command line using argparse

	if __name__ == "__main__":

		# Create argument parser from commandline
		parser = argparse.ArgumentParser(description='[*] writeASCII: \
	                                         Text to ASCII conversion tool',
		                                 formatter_class=\
		                                 argparse.ArgumentDefaultsHelpFormatter)

		parser.add_argument('Words',
		                    metavar='Words',
		                    nargs='+',
		                    help='Phrase to be converted to ASCII')

		parser.add_argument('-f', '--font',
		                    action='store',
		                    default='asciiCharacters.ezfnt',
		                    help='Db/Font used for translation',
		                    dest='character_db')

		parser.add_argument('-o', '--output',
		                    action='store',
		                    help='Output results to output_file',
		                    dest='output_file')

		parser.add_argument('-l', '--lengthwise',
		                    action='store_true',
		                    help='Force phrase to run horizontal. Often good \
		                          for writing output to a file. Usually not so \
		                          good for console output')

		parser.add_argument('-v', '--vertical',
		                    action='store_true',
		                    help='Force phrase to run fully vertical. Often good \
		                          for console output and/or grabing individual \
		                          characters one after another')

		args = parser.parse_args()

		# Setup our variables based on the arguments
		if os.path.exists(args.character_db):
			dictionary_file = args.character_db
			print('Using:', dictionary_file, ' as font for translation')
		else:
			parser.print_usage()
			print('File:', args.character_db, ' does not exist!')
			return(0)

		#if args.output_file and os.path.exists(args.output_file):
		#	print('Are you sure you want to overwrite ', args.output_file,' ?')

		output_file = args.output_file

		# Setup the pixelmap and dictionary to lookup correct position in pixelmap
		alphabet_dictionary, clean_pixel_map = setup_ascii_dictionary(dictionary_file)

		# Easy way to call the main part that outputs
		def heart_beat():
			write_ascii(word, alphabet_dictionary,
			            clean_pixel_map, output_file)

		# We either output verticle, horizontal, or each word on
		# it's own verticle line
		if args.vertical:
			phrase_to_translate = ''.join(args.Words)
			for word in phrase_to_translate:
				heart_beat()
		elif args.lengthwise:
			word = ' '.join(args.Words)
			heart_beat()
		else:
			phrase_to_translate = args.Words
			for word in phrase_to_translate:
				heart_beat()

main()


# The old way of seting up the dictionary, now replaced with a concise
# dictionary comprehension
#
# count = 0
# for character in alphabet:
#        alphabet_dictionary[character] = count
#        count += 1


# --The old way to parse command line using getopts-- (Depreciated)
# usage() comes from old way..although I still like the visual look of my usage
# better so until I figure out how to re-formate argparse help I'm keeping this
# def usage():
#        print("[*] writeASCII: Text to ASCII conversion tool")
#        print("Usage: writeASCII.py -d dictionary -o output_file -p phrase")
#        print()
#        print("-h --help                  - This usage message")
#        print("-d --dictionary            - Use dictionary as DB for translation")
#        print("-o --output                - Output results to output_file")
#        print("-p --phrase                - Phrase to translate (not optional)")
#        print("                             phrase must be...")
#        print()
#        print("-d and -o are optional.")
#        print("-d = asciiCharacters.db by default")
#        print("-o = stdout by default")
#        print()
#        print("Examples:")
#        print("writeASCII.py -d myAsciiCharacters.db -p \"Translate me\"")
#        print("writeASCII.py -d myAsciiCharacters.db -o myBigAscii.txt -p \"Transl$
#        print("writeASCII.py -p \"Translate me\"")
#        sys.exit(0)


# --The old way to parse command line using getopts-- (Depreciated)
#
# if not len(sys.argv[1:]):
#        usage()
#
# try:
#        opts, args = getopt.getopt(sys.argv[1:], "hd:o:p:",
#                                   ["dictionary", "output", "phrase"])
#
# except getopt.GetoptError as err:
#        print(str(err))
#        usage()
#
# for o,a in opts:
#        if o in ("-h", "--help"):
#                usage()
#        elif o in ("-d", "--dictionary"):
#                dictionaryFile = a
#        elif o in ("-o", "--output"):
#                outputFile = a
#       elif o in ("-p", "--phrase"):
#                phraseToTranslate = a
#        else:
#                assert False, "Unhandled Option"
