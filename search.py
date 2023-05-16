import os
import itertools
from game_scope_prompt import prompt_choice
from game_scope import game_type

limit = 30
rootDir = "C:\\Users\lomax\OneDrive\Documentos\888poker\HandHistory\shimeji"
game_count = 0
global_win_count = 0
global_hand_count = 0

#cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
cards = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
combos = itertools.combinations(cards, 2)
pockets = [(i,i) for i in cards]
total_unique_hands = pockets + list(combos)

all_hands = {}
all_hands_suited = {}
all_hands_win = {}
all_hands_win_suited = {}
for card in total_unique_hands:
	all_hands[card[0]+card[1]] = 0
	all_hands_win[card[0]+card[1]] = 0

for card in total_unique_hands[13:]:
	all_hands_suited[card[0]+card[1]] = 0
	all_hands_win_suited[card[0]+card[1]] = 0

prompt_choice()
choice = input()

for realPath,dirs,files in os.walk(rootDir):
	
	for fileToOpen in files:	
		#if game_count > limit:
		#	break

		if game_type(fileToOpen, choice):
			game_count += 1
			#print(fileToOpen)
			
			fileToSearch = fileToOpen
			file_name = os.path.join(rootDir, fileToSearch)
			file = open(file_name, 'r')

			item = file.read()
			# add '()()()' to text blocks for demarcation
			text = item.replace("\n\n\n", "\n()()()")
			form_text = text.split("\n()()()")
			count = 0
			total_hands = 0
			my_hand = ""

			for text_block in form_text:
				next_text = text_block.split("\n")
				for line in next_text:
					if "Dealt to shimeji" in line:
						total_hands += 1
						my_hand = line[-10:]
						card1 = my_hand[2]; card2 = my_hand[6]
						card1_suit = my_hand[3]; card2_suit = my_hand[7]
						
						#e.g. 'KA' is considered the same as 'AK' in hands dictionary
						if card1+card2 in all_hands:
							hand_order = card1+card2
						else:
							hand_order = card2+card1
						all_hands[hand_order] += 1	
						if card1_suit == card2_suit:
							all_hands_suited[hand_order] += 1
					
					if "shimeji collected" in line:
						all_hands_win[hand_order] += 1
						if card1_suit == card2_suit:
							all_hands_win_suited[hand_order] += 1
						count += 1
						#don't recount side-pot collection
						break

			global_win_count += count
			global_hand_count += total_hands
			#print ("total wins: " + str(count))
			#print ("total hands: " + str(total_hands))

#printing in three columns between 30 spaces each
for a, b, c in zip(list(all_hands)[::3], list(all_hands)[1::3], list(all_hands)[2::3]):
	print('{:<30}{:<30}{:<}'.format(a + ": " + str(all_hands[a]),b + ": " + str(all_hands[b]), c + ": " + str(all_hands[c]) ))
#printing last item because it doesnt fit the columns
print(list(all_hands)[-1] + ": " + str(all_hands[list(all_hands)[-1]]) )
 
#for a, b, c, d in zip(list(all_hands)[::4], list(all_hands)[1::4], list(all_hands)[2::4], list(all_hands)[3::4]):
#	print('{:<30}{:<30}{:<30}{:<}'.format(a + ": " + str(all_hands[a]),b + ": " + str(all_hands[b]), c + ": " + str(all_hands[c]), d + ": " + str(all_hands[d]) ))

print("global wins: " + str(global_win_count))
print("global hands: " + str(global_hand_count))
print(game_count)

for a, b, c in zip(list(all_hands_win)[::3], list(all_hands_win)[1::3], list(all_hands_win)[2::3]):
	print('{:<30}{:<30}{:<}'.format(a + ": " + str(all_hands_win[a]),b + ": " + str(all_hands_win[b]), c + ": " + str(all_hands_win[c]) ))
print(list(all_hands_win)[-1] + ": " + str(all_hands_win[list(all_hands_win)[-1]]) )

"""
print("Space between")
for a, b, c in zip(list(all_hands_suited)[::3], list(all_hands_suited)[1::3], list(all_hands_suited)[2::3]):
	print('{:<30}{:<30}{:<}'.format(a + ": " + str(all_hands_suited[a]),b + ": " + str(all_hands_suited[b]), c + ": " + str(all_hands_suited[c]) ))

print("Suits wins")
for a, b, c in zip(list(all_hands_win_suited)[::3], list(all_hands_win_suited)[1::3], list(all_hands_win_suited)[2::3]):
	print('{:<30}{:<30}{:<}'.format(a + ": " + str(all_hands_win_suited[a]),b + ": " + str(all_hands_win_suited[b]), c + ": " + str(all_hands_win_suited[c]) ))

"""


"""
for k,v in all_hands.items():
	if v > 0:
		print(k + ":",v)
"""
