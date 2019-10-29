def read_file(filename):
	lines = []
	with open(filename, 'r', encoding = 'utf-8-sig') as file:
		for line in file:
			lines.append(line.strip())
		# print(lines)
	return lines

def convert(lines):
	chat = []
	person = None #虛無的 == None
	for line in lines:
		if line == 'Allen':
			person = 'Allen'
			continue
		elif line == 'Tom':
			person = 'Tom'
			continue
		else:	
			chat.append(person + ': ' + line)
	return chat

def write_file(filename1, chat):
	with open(filename1, 'w', encoding = 'utf-8') as f:
		for p in chat:
			f.write(p + '\n')


def main():
	lines = read_file('input.txt')
	chat = convert(lines)
	write_file('output.txt', chat)

main()
