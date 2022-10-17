tab = '	'
eng_list = []
rus_list = []
with open('PythonTest.txt', 'r', encoding='utf-8') as file:
    for line in file:
        if line[0] != '#':
            if tab in line:
                index_tab = line.find(tab)
                eng_word = line.strip()[:index_tab]
                eng_list.append(eng_word)
                rus_word = line.strip()[(index_tab + 1):]
                rus_list.append(rus_word)
with open('English.txt', 'w', encoding='utf-8') as eng:
    for en in eng_list:
        eng.write(en + '\n')

with open('Russian.txt', 'w', encoding='utf-8') as rus:
    for ru in rus_list:
        rus.write(ru + '\n')
