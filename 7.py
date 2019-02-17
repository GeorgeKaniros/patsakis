from random import randint
def posi(ar):
    if ar==1 or ar==4 or ar==7:
        return 0
    if ar==2 or ar==5 or ar==8:
        return 2
    else:
        return 4 

thesis=[["  ","|","  ","|","  "],["  ","|","  ","|","  "],["  ","|","  ","|","  "]]
grammi=["------------"]
sfalmata= []
print(' '.join(thesis[0])+ "\n" + ' '.join(grammi)+ "\n" +' '.join(thesis[1])+ "\n" +' '.join(grammi)+ "\n" +' '.join(thesis[2]))
for i in range(9):
    if i%2 == 0:
        player=int(input("Δωσε θεση που θελεις να παιξει ο παιχτης"))
        while player in sfalmata or player>10 or player<0:
            player = int(input("Δωσε σωστη θεση"))
        sfalmata.append(player)
        if player==3 or player==6 or player==9:
            thesis[int(player/3)-1][posi(player)] = " X "
            print(' '.join(thesis[0])+ "\n" + ' '.join(grammi)+ "\n" +' '.join(thesis[1])+ "\n" +' '.join(grammi)+ "\n" +' '.join(thesis[2]))
        else:
            thesis[int(player/3)][posi(player)] = " X "
            print(' '.join(thesis[0])+ "\n" + ' '.join(grammi)+ "\n" +' '.join(thesis[1])+ "\n" +' '.join(grammi)+ "\n" +' '.join(thesis[2]))
    else:
        ranpos=randint(1, 9)
        while ranpos in sfalmata:
            ranpos=randint(1, 9)
        sfalmata.append(ranpos)
        print ("Ο υπολογιστης εκανε την κινηση του")
        if ranpos==3 or ranpos==6 or ranpos==9:
            thesis[int(ranpos/3)-1][posi(ranpos)]=" O "
            print(' '.join(thesis[0])+ "\n" + ' '.join(grammi)+ "\n" +' '.join(thesis[1])+ "\n" +' '.join(grammi)+ "\n" +' '.join(thesis[2]))
        else:
            thesis[int(ranpos/3)][posi(ranpos)]=" O "
            print(' '.join(thesis[0])+ "\n" + ' '.join(grammi)+ "\n" +' '.join(thesis[1])+ "\n" +' '.join(grammi)+ "\n" +' '.join(thesis[2]))
    if i>=5:
        turn=" X "
        player="Παιχτης"
        for y in range(2):
            if thesis[0][0]==turn and thesis[1][2]==turn and thesis[2][4]==turn:
                print(player + " κερδισε")
                telos=input("Enter για κλεισιμο")    
                quit()
            elif thesis[0][4]==turn and thesis[1][2]==turn and thesis[2][0]==turn:
                print(player + " κερδισε")
                telos=input("Enter για κλεισιμο")    
                quit()
            elif thesis[0][0]==turn and thesis[1][0]==turn and thesis[2][0]==turn:
                print(player + " κερδισε")
                telos=input("Enter για κλεισιμο")   
                quit()
            elif thesis[0][2]==turn and thesis[1][2]==turn and thesis[2][2]==turn:
                print(player + " κερδισε")
                telos=input("Enter για κλεισιμο")   
                quit()
            elif thesis[0][4]==turn and thesis[1][4]==turn and thesis[2][4]==turn:    
                print(player + " κερδισε")
                telos=input("Enter για κλεισιμο")   
                quit()
            for j in range(3):
                win=0            
                for z in range(0,5,2):
                    if thesis[j][z]==turn: 
                        win += 1
                if win == 3:
                    print(player + " κερδισε")
                    telos=input("Enter για κλεισιμο")   
                    quit()
            turn=" O "
            player="Υπολογιστης"    
telos=input("Enter για κλεισιμο")
