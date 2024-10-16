import random

def shifr ():
    chislo = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    li_st = list(range(3, 21))
    shi_fr = random.choice(li_st)
    return shi_fr

def password(n):
    passs = {}
    passs.update({3: 12, 4: 13, 5: 1423, 6: 121524, 7: 162534, 8: 13172635, 9: 1218273645})
    passs.update({10: 141923283746, 11: 11029384756, 12: 12131511124210394857, 13: 112211310495867})
    passs.update({14: 1611325212343114105968, 15: 1214114232133124115106978})
    passs.update({16: 1317115262143531341251161079, 17: 11621531441351261171089})
    passs.update({18: 12151811724272163631545414513612711810, 19: 118217316415514613712811910, 20: 13141911923282183731746416515614713812911})
    passcord = passs.get(n)
    return passcord

a = shifr()
print(a, "Parol: ")
chis1 = list(range(1, a))
chis2 = list(range(1, a))
par = []
itog = ''

for i in chis1:
    for j in chis2:
        ch1 = i
        ch2 = j
        if ch1 >= ch2:
            continue
        else:
            kratno = a % (ch1 + ch2)
            if kratno == 0:
                par.append([ch1, ch2])
                itog = itog + str(ch1) + str(ch2)

print("Pars", *par)
print("Parol", itog)
if int(itog) == password(a):
    print("Nace")

