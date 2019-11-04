##########################################################
#           creates basic report for odoo v10, v12
#           @author jd4niel - python3 2019
##########################################################
from resources.init_text import created_by_10, created_by_12
from resources.init_text import get_odoo_version, get_module_name
from resources.python_file import get_report_def
from resources.xml_files import get_paperstyle_format,get_template
# ast -> to create str to dic
import ast
import os

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
	print(" -> manifest.py updated \n %s \n"%new_manifest)

def write_template_xml(report_folder, template_xml, report_name):
	f = open(report_folder+'/'+template_xml,'w')
	f.write(get_template(report_name, get_module_name(), get_odoo_version()))
	f.close()

def write_paperstyle_file(report_folder, paperstyle_xml, report_name, model_name):
	f = open(report_folder+'/'+paperstyle_xml,'w')
	model_string = input('\n    Report string: ')
	f.write(get_paperstyle_format(get_module_name(), report_name, model_name, model_string, get_odoo_version()))
	f.close()

def write_python_file(report_folder, python_file, report_name, model_name):
	# open py file and write report definition
	f = open(report_folder+'/'+python_file,'w')
	f.write(get_report_def(report_name,python_file,get_module_name(),model_name,get_odoo_version()))
	f.close()

def write_init_file(python_file,report_folder,file_exist=False):
	# write in init file to add dependency
	init_file = "%s/__init__.py"%report_folder
	if os.path.isfile(init_file):
		file_exist = True
	import_text = ''
	# If file is already created it wont write 'created by' text
	if get_odoo_version() == 10:
		created_by_10 = created_by_10 if not file_exist else ''
		import_text = created_by_10 + '\nimport %s'%python_file.replace('.py','')
	else:
		created_by_12 = created_by_12 if not file_exist else ''
		import_text = created_by_12 + '\nfrom . import %s'%python_file.replace('.py','')
	
	if file_exist:
		# append import
		with open(init_file, "a") as myfile:
			myfile.write(import_text)
	else:
		f= open(init_file,"w")
		f.write(import_text)
		f.close()

def create_reports_folder(command,python_file=None):
	# creates report folder and init file
	os.system("mkdir reports")
	os.system(command+" reports/__init__.py")
	if python_file:
		# writes inside __init__ 
		write_init_file(python_file, 'reports')
	return 'reports'
		

def create_report_files(name):
	python_file = "%s_report.py"%name.lower()
	paperstyle_xml = "%s_report_view.xml"%name.lower()
	template_xml = "%s_report_view_pdf.xml"%name.lower()

	report_folder = 'report' if os.path.isdir('report') else 'reports'
	# touch command is used for create files 
	create_file = "touch %s/%s %s/%s %s/%s"%(report_folder,python_file,report_folder,paperstyle_xml,report_folder,template_xml)
	# init process
	try:
		# creates report files 
		if os.path.isdir('reports') or os.path.isdir('report'):
			os.system(create_file)
			write_init_file(python_file, report_folder)
		else:
			# If folder not exist creates new one
			report_folder = create_reports_folder(create_file,python_file)
		# write python_file.py and xml files
		report_name = input('\n - Report template name: ')
		model_name = input('\n - Model name: ')
		write_python_file(report_folder,python_file, report_name, model_name)
		write_paperstyle_file(report_folder, paperstyle_xml, report_name, model_name)
		write_template_xml(report_folder, template_xml, report_name)
		list_files = list(map(lambda x: '%s/%s'%(report_folder,x),[paperstyle_xml, template_xml]))
		# write in manifest.py created files
		append_files_in_manifest(list_files)
	except error:
		print("\n ups! something wrong... \n %s \n\n"%error)
	
  
print("""  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
	Creates or add new report in odoo | jd4niel

	you should be located inside odoo module/addon
 - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

""")
name = input("    Enter report name: ")

create_report_files(name)
print("\n ==    Report created successfully! :)    ==")