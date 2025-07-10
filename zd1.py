# with open('zd1.txt', 'r') as fail, open('zd12.txt', 'r') as fail2:
#     text = fail.readlines()
#     text2 = fail2.readlines()
#     for i in range(len(text)):
#         if text[i] != text2[i]:
#             print(f'Первывй список индекс {i} {text[i]}Второй список индекс {i} {text2[i]}')

# with open('zd1.txt', 'r',encoding='utf-8') as fail, open('zd12.txt', 'w',encoding='utf-8') as fail2:
#     text = fail.readlines()
#     sim = 0
#     str = 0
#     glasb = 0
#     soglb = 0
#     kolchil = 0
#     for i in text:
#         str +=1
#         for j in i:
#             sim += 1
#             print(j)
#             if j in ['А', 'О', 'У', 'Ы', 'Э', 'И', 'Я', 'Ё', 'Ю', 'Е']:
#                 glasb += 1
#             elif j in ['Б', 'В', 'Г', 'Д', 'Ж', 'З', 'Й','К', 'Л', 'М', 'Н', 'П', 'Р', 'С', 'Т', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ']:
#                 soglb += 1
#             elif j in ['1','2','3','4','5','6','7','8','9','0']:
#                 kolchil += 1
#     print(glasb)
#     stats = [
#         f"Всего символов: {sim}\n",
#         f"Всего строк: {str}\n",
#         f"Гласных букв: {glasb}\n",
#         f"Согласных букв: {soglb}\n",
#         f"Цифр: {kolchil}\n"
#     ]
#     fail2.writelines(stats)

# with open('zd3.txt', 'r',encoding='utf-8') as fail, open('zd3ot.txt', 'w',encoding='utf-8') as fail2:
#     text = fail.readlines()
#     text.pop(-1)
#     fail2.writelines(text)

# with open('zd3.txt', 'r',encoding='utf-8') as fail, open('zd3ot.txt', 'w',encoding='utf-8') as fail2:
#     text = fail.readlines()
#     a = max(text, key=len)
#     print(len(a.strip()))

with open('zd3.txt', 'r', encoding='utf-8') as fail:
    a = input()
    kil = 0
    for i in fail:
        words = i.strip().split()
        for j in words:
            if j == a:
                kil += 1
    print(kil)

with open('zd3.txt', 'r', encoding='utf-8') as fail:
    a = input()
    b = input()
    line = fail.readlines()
with open('zd3.txt', 'w', encoding='utf-8') as fail:
    for i in line:
        words = i.strip().split()
        word = []
        for j in words:
            if j == a:
                word.append(b)
            else:
                word.append(j)
        fail.write(' '.join(word) + '\n')