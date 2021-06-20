import re
import json
from xml.dom import minidom

def handle_uploaded_file(f):
	if not get_extension(f.name) in ['json', 'xml', 'xlsx']:
		return None
	new_file_name = f'uploaded_files/test.{get_extension(f.name)}'
	file = open(new_file_name, 'wb+')
	for chunk in f.chunks():
		file.write(chunk)
	return new_file_name

def get_extension(file_name):
	res_search = re.search('\.[a-z]{1,5}$', file_name, flags=re.IGNORECASE)
	if res_search != None:
		return res_search.group(0).lower()[1:]
	else:
		return None

def handle_json(file_name):
	file = open(file_name, 'r')
	arr = json.loads(file.read())
	return arr

def handle_xml(file_name):
	file = open(file_name, 'r')
	alg_list = []

	doc = minidom.parse(file_name)
	alg_elements = doc.getElementsByTagName('alg')
	for alg_element in alg_elements:
		name = alg_element.getAttribute('name')
		anger = alg_element.getAttribute('anger')
		alg_list.append({'name': name, 'anger': anger})

	return alg_list