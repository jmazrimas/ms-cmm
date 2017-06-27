#
# Run CheckMate
#
#import subprocess
import os
import sys


def main():
	"""Main function
	"""
	run_checkmate('C:\\tmp\\test2.qif', 'C:\\tmp\\test2.dmi')


def run_checkmate(input_file, output_file):
	"""Runs CheckMate to generate DMIS from the given input QIF file
	"""

##	f = open(output_file, 'w')
##	f.write('<Placeholder for auto-generated CheckMate DMIS program>');
##	f.close()

	# #define some paths
	cm_exefile = 'C:\\Program Files\\Origin International Inc\\CMEngine\\CMEngine.exe'

	# # Call CMEngine
	#subprocess.call([cm_exefile, 'CMEngine.exe', 'CMEQIF2QIF', input_file])
	os.spawnl(os.P_WAIT, cm_exefile, 'CMEngine.exe', 'CMEQIF2QIF', 'SILENT', input_file)

	# CMEngine creates a DMIS file with name based on input file
	dmis_file = os.path.splitext(input_file)[0] + '.DMI'

	# rename DMIS file to output_file if necessary
	if(dmis_file != output_file):
		os.rename(dmis_file, output_file)



if (__name__ == "__main__"):
	"""Initial function called by interpreter at command line
	"""
	main()