#-*- coding: utf-8 -*-
import random 
import subprocess
import getpass

# codigo hecho por Diego Jonás Pérez.

def question(time, inf):
	score = 0
	while score < 10:
		subprocess.call(["cmd.exe", "/c", "cls"])
		vrb = random.randint(0, 29)
		print("write this verb in infinitve: {}".format(time[vrb]))
		print("write 'back' if you want to exit")
		print("score: {}".format(score))
		answ = input("> ")
		if answ == inf[vrb] or answ.upper() == inf[vrb].upper():
			score += 1
		elif answ == "back":
			break
		else:
			score -= 1


def check(word, your_word):
	if word == your_word:
		return True
	else:
		return False

if __name__ == '__main__':
	infinitive = ("arise", "awake", "bear", "beat", "become", "begin", "bend", "bet", "bind", "bite", "blow", "break", "bring", "build", "burn","burst", "buy", "catch", "choose", "cling", "come", "cost", "creep", "cut", "deal", "dig", "do", "draw", "drink", "drive", "fall", "feed", "feel", "fight", "find")
	past = ("arose", "awoke", "bore", "beat", "became", "began", "bent", "bet", "bound", "bit", "blew", "broke", "brought", "built", "burnt", "burst", "bought", "caught", "chose", "clung", "came", "cost", "crept", "cut", "dealt", "dug", "did", "drew", "drank", "drove", "fell", "fed", "felt", "fought", "found")
	pp = ("arisen", "awoken", "born", "beaten", "become", "begun", "bent", "bet", "bound", "bitten", "blown", "broken", "brought", "built", "burnt", "burst", "bought", "caught", "chosen", "clung", "come", "cost", "crept", "cut", "dealt", "dug", "done", "drawn", "drunk", "driven", "fallen", "fed", "felt", "fought", "found")
	choice = str()
	while choice != "exit":
		subprocess.call(["cmd.exe","/c","cls"])
		choice = str(input('''
            E N G L I S H   T E S T
            [1] past
            [2] past participle
            [3] list of verbs
           

            [exit]

            > '''))
		if choice == "1":
			question(past, infinitive)
		elif choice == "2":
			question(pp, infinitive)

		elif choice == "3":
			subprocess.call(["cmd.exe", "/c", "cls"])
			count = 0
			count2 = 0
			for i in infinitive:
				ran = random.randint(0, 1)
				if ran == 1:
					print("{} / {} / {}".format(i, past[count], pp[count]))
					count2 += 1
				else:
					continue
				count += 1
			print("")
			print("")
			if count2 != 30:
				print("not all the verbs are in the list ")
			if count2 >= 23:
				print("scroll up for more verbs")

			getpass.getpass("press enter to exit.")

	


		
	