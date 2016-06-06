# ������ 8. ������� 14.
# ����������� ���� "���������" (��. �.������ ������������� �� Python. ��.4) ���, ����� � ������� ����� ���������� ���������. ����� ������ �������� ����� �� ��������� � ��� ������, ���� � ���� ��� ������� �������������.
# ������������ ������� ���������� �����, �� ������� �� ������, ���������� ����� ��� ���������, �������� ������ ���, ��� �������� ���������.

# ������
# 4.06.2016

import random

# create a sequence of words to choose from
WORDS = ("������", "��������", "������", "��������", "�����", "�������� ���������")

hints = ("����� �������� ������� ���","�� ������ ����������� � ��������� ���","������� ������ � �������� �����", "������- �� ���� ���� ��� �������","��� �������� �������, ������� ����� � ������ ������ � �������?","��� ����� �� �����, �� ���� �����������, �� ����� ������� �������, ������ ����� �����, �������� �������, �������� � ������ �����, ��������� ���� ����������, � ������������� ��������, ����������, ������������� �������, ������� �������� ��������� ����, ��������������� ���� � ������ ��������?")
# pick one word randomly from the sequence
word = random.choice(WORDS)
wordNumber = WORDS.index(word)
# create a variable to use later to see if the guess is correct
correct = word
wantHint = "���������"
countHints = 0
countErrors = 0
# create a jumbled version of the word
jumble =""
while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]

# start the game
print(
"""
           Welcome to Word Jumble!
        
   Unscramble the letters to make a word.
(Press the enter key at the prompt to quit.)
"""
)
print("The jumble is:", jumble + " ���� �� ������������, ������� '���������' ")

guess = input("\nYour guess: ")
while guess != correct and guess != "":
	if guess==wantHint:
		print(hints[wordNumber])
		countHints +=1
	if  guess!=wantHint:
		print("Sorry, that's not it.")
		countErrors +=1
		print("����� ������: " +str(countErrors))
	guess = input("Your guess: ")
	
		
if guess == correct:
		print("That's it!  You guessed it!\n")
	
	

print("Thanks for playing.")
print("�� ��������� " + str(countErrors) + " ������, ������������ " + str(countHints) + " ��������� � ���������� " + str(100-5*countErrors-50*countHints) + " �����")

input("\n\nPress the enter key to exit.")