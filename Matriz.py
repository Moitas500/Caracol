matriz = [[1,2,3],[4,5,6],[7,8,9]]

def ordenarcaracol():
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if(i==0 and j<len(matriz)-1):
                print(matriz[i][j])
            if(j==2 and i<len(matriz)-1):
                print(matriz[i][j])
            if(i==2 and j<len(matriz)-1):
                print(matriz[i][(len(matriz)-1)-j])
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if(j==0 and i<len(matriz)-1):
                print(matriz[(len(matriz)-1)-i][j])
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if(i==1 and 0<j<len(matriz)-1):
                print(matriz[i][j])
def main():
    ordenarcaracol()

main()
