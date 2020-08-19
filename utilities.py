def parser(file_input):
	try:
		file_input = file_input.decode('utf-8')
	except UnicodeDecodeError:
		file_input = file_input.decode('gbk')

	lines = []
	for line in file_input.split('\r'):
		if line.strip():
			lines.append(line.strip()+'\n')

	return lines

def deparser(file_output):
	new_lines = []
	for line in file_output:
		new_lines.append(line.encode('utf-8').decode('utf-8'))

	return new_lines
