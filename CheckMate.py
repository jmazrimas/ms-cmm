# 
# Run CheckMate
#
import subprocess
import sys


def main():
	"""Main function
	"""
	run_checkmate("input.qif", "output.dmi")


def run_checkmate(input_file, output_file):
	"""Runs CheckMate to generate DMIS from the given input QIF file
	"""
	
	f = open(output_file, "w")
	f.write("<Placeholder for auto-generated CheckMate DMIS program>");
	f.close()
        
	# #define some paths
	# cm_exefile = r"C:\Program Files\Origin International Inc\CMEngine\CMEngine.exe"

	# # Call MBDVidia
	# subprocess.call([cm_exefile, 'CMEngine.exe', 'CMEQIF2QIF', input_file])


if (__name__ == "__main__"):
	"""Initial function called by interpreter at command line
	"""
	main()
