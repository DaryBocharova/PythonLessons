'''
Скачайте файл по ссылке
Прочитайте содержимое файла в перменную, подсчитайте длинну получившейся строки
Подсчитайте количество слов в тексте
Замените точки в тексте на восклицательные знаки
Сохраните результат в файл referat2.txt
'''


with open ('referat.txt','r', encoding = 'utf-8') as f:
    content = f.read()
   # print(len(content))

    count_words = content.split(" ")
   # print(len(count_words))

    content = content.replace(".", "!")
    # print(content)



    
with open ('referat2.txt','w', encoding = 'utf-8') as l:
     content1 = l.write(content)
    
     print(content1)

