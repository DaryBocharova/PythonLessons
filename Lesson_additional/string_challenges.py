
# # Вывести последнюю букву в слове
word = 'Архангельск'
print(word[-1])


# # Вывести количество букв а в слове
word = 'Архангельск'
print(len(word))


# Вывести количество гласных букв в слове
word = 'Архангельск'

vowels = set("аоуыэяёеюи")
word_set = set(word.lower())
 
print('Гласных {}, согласных {}'.format(len(word_set.intersection(vowels)),
                                        len(word_set.difference(vowels))))



# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
sentence1 = sentence.split(" ")
print(len(sentence1))


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
sentence2 = sentence.split(" ")
n = 0
while n != len(sentence2):
    print(sentence2[n][0])
    n += 1




# # Вывести усреднённую длину слова.
sentence = 'Мы приехали в гости'
sentence2 = sentence.split(" ")
n = 0
sum = 0
while n != len(sentence2):
    a = len(sentence2[n])
    n +=1
    sum = sum + a
print(int(sum/len(sentence2)))



    
