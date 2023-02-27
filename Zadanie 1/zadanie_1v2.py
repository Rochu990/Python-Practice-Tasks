print('Hej! Wprowadź dowolne zdanie!!!')

user_choice = input()
words_list = user_choice.split()

for i in words_list:
    print(i + " " + str(len(i)))