import random
digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
stop_list = 'il1Lo0O'
massiv = ''
chars = ''
r = ''
# ======================================================================
cnt_Pw = int(input('Укажите количество паролей для генерации:'))
len_Pw = int(input('Укажите длину одного пароля:'))
dig_On = input('Включать ли цифры 0123456789? (y/n)')
ABC_On = input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? (y/n)')
abc_On = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? (y/n)')
ch_On = input('Включать ли символы !#$%&*+-=?@^_? (y/n)')
exc_On = input('Исключать ли неоднозначные символы il1Lo0O? (y/n)')
# ======================================================================
if dig_On == 'y':
    massiv += digits
if ABC_On == 'y':
    massiv += lowercase_letters
if abc_On == 'y':
    massiv += uppercase_letters
if ch_On == 'y':
    massiv += punctuation
# ======================================================================
for _ in range(cnt_Pw):
    for _ in range(len_Pw):
        while exc_On == 'y':
            r = random.choice(massiv)
            if r not in stop_list:
                chars += random.choice(massiv)
                break
        while exc_On == 'n':
            r = random.choice(massiv)
            chars += random.choice(massiv)
            break
    chars += '~'
chars = chars[:-1]
# ======================================================================
print(*chars.split('~'), sep = '\n')
# ======================================================================