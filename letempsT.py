T = int(input("Veuillez entrer le temps T:"))
H = T// 3600
R = T % 3600
M = R // 60
S = R % 60
print("Il est:",H,"hr",M,"min",S,"Seconde")