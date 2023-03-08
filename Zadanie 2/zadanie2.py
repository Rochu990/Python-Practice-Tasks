print("Hej! Podaj nazwę pliku, który chciałbys otworzyć(wraz z rozszerzeniem)")
user_choice = input()

with open(user_choice) as f:
    for line in f:
        print(line)

words_list = line.split()

for i in words_list:
    print(i + " " + str(len(i)))