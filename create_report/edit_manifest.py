import ast
import os
import json
def append_files_in_manifest(files=[]):
	'''
		This method apppends created files to manifest.py
	'''
	# Read file
	f = open('__manifest__.py','r')
	# Convert string from all file
	manifest = str(f.read())
	manifest_str = '{' + manifest.split('{')[1]
	f.close()
	# Create dic from string
	manifest_dic = ast.literal_eval(manifest_str)
	# get data list
	data = manifest_dic.get('data',[])
	data = data+files
	# get last data element
	data_text = manifest_str.split('"data" :')[1].split(']')[0]+'],'
	# Formated text
	eight_spaces = "        "
	new_text = str(data).replace(',',',\n%s'%'       ').replace(']','],').replace('[',eight_spaces)
	new_manifest = str(manifest.replace(data_text,"[\n"+new_text))
	file = open('__manifest__.py','w')
	#replace tabs to space
	file.write(new_manifest)
	file.close()
	return " -> manifest.py updated \n %s"%new_manifest