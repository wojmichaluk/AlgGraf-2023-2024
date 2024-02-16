from dimacs import *
from time import time

#additional given data
names=["clique5","clique20","clique100","clique1000",
"g1","grid5x5","grid100x100","path10","path1000",
"path10000","pp10","pp100","pp1000","rand20_100",
"rand100_500","rand1000_100000"]

functions=["Find/union:","BFS with binary search:",
"DFS with binary search:","Modified Dijkstra:"]

s=0
t=1

#---------------------------------------------#

def runtests(function,nr):
    no_tests=len(names)
    passed=0
    total_time=0
    print(functions[nr])
    for i in range(no_tests):
        sol=int(readSolution(names[i]))
        V,L=loadWeightedGraph(names[i])
        a=time()
        if nr==1 or nr==2: #BFS or DFS with binary search
            result=function(V,L,s,t,nr)
        else: result=function(V,L,s,t)
        b=time()
        print("Test ",i,":",sep='')
        print("Uzyskany wynik: ",result,sep='')
        print("Prawidłowy wynik: ",sol,sep='')
        print("Czas wykonania: {ex_time:.2f} s".format(ex_time=b-a))
        total_time+=b-a
        if result==sol:
            passed+=1
            print("Test zaliczony!")
        else: print("Test niezaliczony!")
        print()
    print("Liczba zaliczonych testów: ",passed,"/",no_tests,sep='')
    print("Łączny czas wykonania: {total:.2f} s\n".format(total=total_time))
