N = int(input("Saisir un nombre: "))
S = 0
for i in range(1, N+1):      #psq f python dernier valeur ma dkhlch c ta dire yhbs f "N"
    if N % i == 0:  
        S = S + i   
if S-N == N :                #psq le nombre parfait hwa li la somme ta3 9wasmo (apart lui meme) = nfso
    print(N , "est parfait")
else:
    print(N , "n'est pas parfait")
    