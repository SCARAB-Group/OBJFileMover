#!/usr/bin/python -tt

######################################################################################
# Written by: Niklas Malmqvist, 2016-02-01
#
# Description:
# ------------
# Makes a copy of the OBJ file from an environment (e.g. production)to one or many
# other environments (e.g. background servers)
#
######################################################################################

import sys
import os
import time
import json
import shutil
from pprint import pprint
from os import listdir
from os.path import isfile, join
import glob

def main():
	filename_suffix = '.OBJ'

	if len(sys.argv) < 2:
		targetEnv = "LIMSBBPROD.OBJ"
	else:
		targetEnv = sys.argv[1] + filename_suffix
	
	data_file = "config.json"
	configs = getConfigs(data_file)
	today = time.strftime("%y%m%d")
	source_dir = configs["sourcedir"]
	target_dirs = configs["targetdirs"]
	
	sourceFileListing = glob.glob(os.path.join(source_dir, targetEnv))
	
	if len(sourceFileListing) > 1:
		sys.exit("Found more than one OBJ file in source folder... exiting")
	else:
		sourceFileFullPath = sourceFileListing[0]
	
	for target_dir in target_dirs:
		targetFileListing = glob.glob(os.path.join(target_dir, targetEnv))
		
		if len(targetFileListing) > 1:
			sys.exit("Found more than one OBJ file in target folder... exiting")
			
		elif len(targetFileListing) == 0:
			# Just copy, no renaming needed
			copyfile(sourceFileFullPath, target_dir)
				
		else:
			targetFileFullPath = targetFileListing[0]
			
			# Rename file in target folder
			renamefile(targetFileFullPath, today)
			
			# and copy from source
			copyfile(sourceFileFullPath, target_dir)	

def copyfile(source_dir, target_dir):
	try:
		shutil.copy(source_dir, target_dir)
	
	except Exception, e:
		print "File copy operation failed!", e
	
	else:
		print "Successfully copied file: ", source_dir, "->", target_dir

def renamefile(source_dir, suffix):
	source_filename, source_file_extension = os.path.splitext(source_dir)
	newname = source_filename + "_" + suffix + source_file_extension
	
	try:
		shutil.move(source_dir, newname)
	
	except Exception, e:
		print "File rename operation failed!", e
		
	else:
		print "Successfully renamed file:", source_dir, "->", newname
		
def getConfigs(conf_file):
	with open(conf_file) as data_file:    
		data = json.load(data_file)
			
	return data

if __name__ == '__main__':
	main()