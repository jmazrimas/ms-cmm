# 
# Run MBDVidia
#
import subprocess
import sys


def main():
	"""Main function
	"""
	run_mbdvidia("input.prt", "input.qif")


def run_mbdvidia(input_file, output_file):
	"""Runs MBDVidia to convert the given input file
	"""

	#define some paths
	mbdvidia_exefile = r"C:\Program Files\Capvidia\MBDVidia x64 Edition\converter.exe"
	config_file = r"no_aux.xml"
	# output_file = r"C:\Users\dcampbell\Desktop\result.qif"

	# Call MBDVidia
	subprocess.call([mbdvidia_exefile, input_file, output_file, config_file, "9772"])


if (__name__ == "__main__"):
	"""Initial function called by interpreter at command line
	"""
	main()
