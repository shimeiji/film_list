import os
import itertools

from game_scope_prompt import prompt_choice
from game_scope import game_type

limit = 100
summary = 1
rootDir = "C:\\Users\lomax\OneDrive\Documentos\888poker\HandHistory\shimeji"
game_count = 0
profit_count = 0
summary_count = 0
ticket_count = 0

prompt_choice(summary)
choice = input()

for realPath,dirs,files in os.walk(rootDir):
	if game_count > limit:
		break
	for fileToOpen in files:	

		if game_type(fileToOpen, choice, summary):
			summary_count += 1
			#print(fileToOpen)
			#print(profit_count)
			fileToSearch = fileToOpen
			file_name = os.path.join(rootDir, fileToSearch)
			file = open(file_name, 'r')
			item = file.read()
			text = item.split("\n")
			for line in text:
				if "won" in line:
					print(line)
					profit_count += 1
			#print(text[-2])
			#print(item)
			if choice == '7':
				placement = int(text[-2][17:].split('/')[0])
				if placement < 11:
					ticket_count += 1
			elif choice == '8':
				placement = int(text[-2][17:].split('/')[0])
				if placement < 6:
					ticket_count += 1

		if game_type(fileToOpen, choice):
			game_count += 1

print("Total: ")
print(profit_count, "out of",game_count, "games")
print("\ntotal summaries found:", summary_count)

if choice == '7' or choice == '8':
	print("tickets: ", ticket_count)