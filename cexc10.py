alturachico=1.50
alturajuca= 1.10

anos=0  #variavel contadora 

while alturajuca <= alturachico:
    alturachico+= 0.02
    alturajuca+=0.05
    anos+=1

print(f'a quantidade de anos para que juca seja mais alto que chico é {anos} anos')