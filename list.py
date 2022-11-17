file = open('file.txt', 'a')
while True:
	string = input("Bведите: ")
	if(string == "quit"):
		file.close()
		break;
	elif(string == 'show'):
		show_content()
	else:
		file.write(string + '\n')
def show_content():
	text = open('file.txt', 'r')
	print(text)
	input()