#-*- coding: utf-8 -*-
import random 
import subprocess
import getpass

# codigo hecho por Diego Jonás Pérez.


def lov(l1, l2, l3, l4):
	subprocess.call(["cmd.exe", "/c", "cls"])
	count = 0
	count2 = 0
	for i in infinitive:
		ran = random.randint(0, 2)
		if ran == 1:
			print("{} / {} / {} /".format(l1[count], l2[count], l3[count], l4[count2]))
			count2 += 1
		else:
			continue
		count += 1
	print("")
	print("")
	if count2 != 64:
		print("not all the verbs are in the list ")
	if count2 >= 24:	
		print("scroll up for more verbs")
	getpass.getpass("press enter to exit.")
	count2 = count2 % 2
	return count2 + 1

def questions2(q, s1, s2, s3, s4, answ):
	resp = str()
	while len(resp) != 1:
		subprocess.call(["cmd.exe","/c","cls"])
		print(q)
		print(s1)
		print(s2)
		print(s3)
		print(s4)
		resp =input("your answer: ")
	if resp.upper() == answ:
		print("correct :)")
		getpass.getpass("press enter to continue...")
		return 1
	else:
		print("incorrect, the correct answer is: {}".format(answ))
		getpass.getpass("press enter to continue...")
		return -1


def questions(years, name, check):
	# real test: englishtag.com/tests/level_test.asp
	subprocess.call(["cmd.exe", "/c", "cls"])
	if check == False:
		print("You can only answer these questions once")
		getpass.getpass("press enter to exit.")
		return 0
	q1 = questions2("How old are you?", "A. I have {} years old".format(years), "B. I have {} years".format(years), "C. I am fine", "D. I am {} years old".format(years), "D")
	q1 += questions2("He went to the Stadium .....", "A. with taxi", "B. by taxi", "C. on taxi", "D. in taxi", "B")
	q1 += questions2("Choose the correct sentence.", "A. He like going to the movies", "B. He likes going to the movies", "C. He liked go to the movies", "D. He like the movies", "B")
	q1 += questions2("Peter ..... fly to San Francisco tomorrow.", "A. to going", "B. goes to", "C. is going to","D. go to", 'C')
	q1 += questions2("He plays soccer .....", "A. on Wednesdays", "B. in Wednesdays", "C. at Wednesdays","D. by Wednesdays", 'A')
	q1 += questions2("It's no use ..... to him. He doesn't listen.", "A. speaking", "B. to speak", "C. spoke", "D. have spoken", 'A')
	q1 += questions2(".... some more coffee?", "A. Do you?", "B. Do you like?", "C. You'd like","D. Would you like?", 'B')
	if q1 > 3 and q1 <= 6:
		return 1
	elif q1 == 7:
		return 2
	elif q1 <= 3 and q1 < 1:
		return -1
	elif q1 < 1:
		return -2


def verbs(time, inf, verb):
	score = 0
	while score < 10:
		if score < -5:
			break
		subprocess.call(["cmd.exe", "/c", "cls"])
		vrb = random.randint(0, 29)
		print("write this verb in {}: {}".format(verb, inf[vrb]))
		print("write 'back' if you want to exit")
		print("score: {}".format(score))
		answ = input("> ")
		answ = answ.lower()
		if answ == time[vrb]:
			score += 1
		elif answ == "back":
			return 0
		else:
			score -= 1
	if score == 10:
		return 1
	elif score < -5:
		return -1
def finish(tier):
	subprocess.call(["cmd.exe","/c","cls"])
	print("finally you finish the english test.")
	print("your english tier is: {}".format(tier))


if __name__ == '__main__':
	check = True
	subprocess.call(["cmd.exe","/c","cls"])
	name = input("what is your name?: ")
	years = int(input("how old are you?: "))
	infinitive = ("arise", "awake", "bear", "beat", "become", "begin", "bend", "bet", "bind", "bite", "blow", "break", "bring", "build", "burn","burst", "buy", "catch", "choose", "cling", "come", "cost", "creep", "cut", "deal", "dig", "do", "draw", "drink", "drive", "fall", "feed", "feel", "fight", "find", "flee", "fly", "forbid", "foresee", "forget", "forgive","freeze","get","give","go","grind","grow","hang","have","hear","hide","hit","hold","hurt","keep","know","lay","lead","lean","learn","leave","lend")
	past = ("arose", "awoke", "bore", "beat", "became", "began", "bent", "bet", "bound", "bit", "blew", "broke", "brought", "built", "burnt", "burst", "bought", "caught", "chose", "clung", "came", "cost", "crept", "cut", "dealt", "dug", "did", "drew", "drank", "drove", "fell", "fed", "felt", "fought", "found", "fled", "flew", "forbade", "foresaw", "forgot","forgave","froze","got","gave","went","ground","grew","hung","had","heard","hid","hit","held","hurt","kept","knew","laid","led","leant","learnt","left","lent")
	pp = ("arisen", "awoken", "born", "beaten", "become", "begun", "bent", "bet", "bound", "bitten", "blown", "broken", "brought", "built", "burnt", "burst", "bought", "caught", "chosen", "clung", "come", "cost", "crept", "cut", "dealt", "dug", "done", "drawn", "drunk", "driven", "fallen", "fed", "felt", "fought", "found", "fled", "flown", "forbidden", "foreseen", "forgotten","forgotten","forgiven","frozen","got","given","gone","ground","grown","hung","had","heard","hid","hit","held","hurt","kept","known","laid","led","leant","learnt","left","lent")
	gerund = ("arising", "awakening", "bearing", "beating", "becoming", "beginning", "bending", "betting", "binding", "biting", "blowing", "breaking", "bringing", "building", "burning", "bursting", "buying", "catching", "choosing", "clinging", "coming", "costing", "creeping", "cutting", "dealing", "doing", "drawing", "drinking", "driving", "falling", "feeding", "feeling", "fighting", "finding", "fleeing", "flying", "forbidding", "foreseeing", "forgetting", "forgiving", "freezing", "getting", "giving", "going", "grinding", "growing", "hanging", "having", "hearing", "hiding", "hitting", "holding", "hurting", "keeping", "knowing", "laying", "leading", "leaning", "learning", "leaving", "lending")
	choice = str()
	points = 0
	while choice != "exit":
		if points < - 3:
			finish("low")
			break
		elif points > 5:
			finish("high")
			break
		subprocess.call(["cmd.exe","/c","cls"])
		choice = str(input('''
            E N G L I S H   T E S T

            By: Diego Jonas Perez
            
            Total Points of {}: {}

            [1] past
            [2] past participle
            [3] gerund
            [4] basic questions
            [5] list of verbs	
            

            write [exit] to quit

            > '''.format(name, points)))
		if choice == "1":
			past_verbs = verbs(past, infinitive, "past")
			points += past_verbs
		elif choice == "2":
			pp_verbs = verbs(pp, infinitive, "past participle")
			points += pp_verbs

		elif choice == "3":
			gerund_verbs = verbs(gerund, infinitive, "gerund")
			points += gerund_verbs

		elif choice == "4":
			q = questions(years, name, check)
			points += q
			check = False 

		elif choice == "5":
			lsv = lov(infinitive, past, pp, gerund)
			points -= lsv

