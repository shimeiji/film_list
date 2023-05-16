def game_type(fname, choice, summary = 0):
	if not summary:
		file_termination = "Holdem.txt"
	else:
		file_termination = "Summary.txt"
	if choice.isnumeric():
		choice = int(choice)

	if choice == "":
		return fname.endswith(file_termination)
	elif choice == 1:
		return "Sit & Go $0.36 + $0.04 Double or Nothing" in fname and fname.endswith(file_termination)
	elif choice == 2:
		return "Sit & Go $0.91 + $0.09 Double or Nothing" in fname and fname.endswith(file_termination)
	elif choice == 3:
		return "Sit & Go $0.35 + $0.05 6 Handed Turbo" in fname and fname.endswith(file_termination)
	elif choice == 4:
		return ("Sit & Go $0.90 + $0.10" in fname or "Sit & Go $0.85 + $0.15" in fname) and fname.endswith(file_termination)
	elif choice == 5:
		return "Sit & Go $2.70 + $0.30" in fname and fname.endswith(file_termination)
	elif choice == 6:
		return "Sit & Go $4.50 + $0.50" in fname and fname.endswith(file_termination)
	elif choice == 7:
		return "Tournament $0.09 + $0.01 $1 Tournament Ticket - 10 GTD" in fname and fname.endswith(file_termination)
	elif choice == 8:
		return "Tournament $0.91 + $0.09 $5.50 Tournament Ticket - 5 GTD" in fname and fname.endswith(file_termination)
	elif choice == 9:
		return "Tournament $0.91 + $0.09" in fname and "Ticket" not in fname and fname.endswith(file_termination)
	elif choice == 10:
		return "Tournament $4 + $0.40" in fname and fname.endswith(file_termination)
	elif choice == 11:
		return "Tournament $5 + $0.50" in fname and fname.endswith(file_termination)
	elif choice == 12:
		return "Tournament Free The $500 Fabulous Winner Spinner Freeroll" in fname and fname.endswith(file_termination)
	elif choice == 13:
		return "Tournament Free $500 Noble Kingdom Freeroll" in fname and fname.endswith(file_termination)
	elif choice == 14:
		return "Tournament $0.91 + $0.09 $16.50 Tournament Ticket - 2 GTD" in fname and fname.endswith(file_termination)
	elif choice == 15 and not summary:
		return "$0.01-$0.02" in fname and fname.endswith(file_termination)
	else: 
		return fname.endswith(file_termination)
		