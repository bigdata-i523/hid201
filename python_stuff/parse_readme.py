#use python 2.7.13

##use library pyyaml for reading as yaml
# install using "pip install pyyaml"

##usage
# python parse_readme.py <path_to_readme>

import sys
import yaml

filename = str(sys.argv[1])
file = open(filename,'r')
between_markers = False

yaml_lines = []
yaml_content = []

#read lines between the ``` markers
print "The lines between ``` markers are :\n"
s = ''
for line in file:
	if line.startswith("```") and between_markers:
		between_markers = False
		yaml_content.append(s)
		s = ''
	elif line.startswith("```") and not between_markers:
		between_markers = True
	else:
		if between_markers:
			yaml_lines.append(line)
			s += line
			print line

#check if a yaml line has TAB
for line in yaml_lines:
	if "\t" in line:
		print "ERROR!! in line :"
		print line, "contains a TAB.. use spaces\n"


#read content as yaml strings
#print dictionaries
#check and display errors
print "\nDictionaries in the file are:\n"
try:
	for data in yaml_content:
		dictionary = yaml.load(data)
		print dictionary
except Exception as e:
	print e
else:
	print "\n\tNo errors were found. Format seems to be correct"