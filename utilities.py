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
