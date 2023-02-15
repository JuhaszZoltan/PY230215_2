from module import Kategoria

utaskategoriak:list[Kategoria] = []

file = open(file='titanic.txt', mode='r', encoding='utf-8')
for s in file: utaskategoriak.append(Kategoria(s))

print(f'2. feladat: {len(utaskategoriak)} db')

f3:int = 0
for k in utaskategoriak:
    f3 += (k.eltuntek + k.tulelok)
print(f'3. feladat: {f3} fő')

f4:str = input('4. feladat: Kulcsszó: ')
f5:bool = False
for k in utaskategoriak:
    if f4 in k.nev:
        print(f'\tVan találat!')
        f5 = True
        break
else: print('\tNincs találat!')

if f5:
    print('5. feladat:')
    for k in utaskategoriak:
        if f4 in k.nev:
            print(f'\t{k.nev} {k.eltuntek + k.tulelok} fő')

f6:list[str] = []
for k in utaskategoriak:
    if k.eltuntek > (k.eltuntek + k.tulelok)*.6:
        f6.append(k.nev)
print('6. feladat:')
for n in f6:
    print(f'\t{n}')

m:int = 0
for i in range(len(utaskategoriak)):
    if utaskategoriak[i].tulelok > utaskategoriak[m].tulelok:
        m = i
print(f'7. feladat: {utaskategoriak[m].nev}')