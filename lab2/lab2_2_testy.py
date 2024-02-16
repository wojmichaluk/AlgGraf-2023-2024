from dimacs import *
from time import time

#additional given data
names=["clique5","clique20","clique100","cycle",
#"clique200","grid100x100" take too much time
"grid5x5","path","rand20_100","rand100_500","simple"]

functions=["Connectivity using modified FF with BFS:",
"Connectivity using modified FF with DFS:"]

#---------------------------------------------#

def runtests(function,nr):
    no_tests=len(names)
    passed=0
    total_time=0
    print(functions[nr])
    for i in range(no_tests):
        sol=int(readSolution("connectivity/"+names[i]))
        V,L=loadWeightedGraph("connectivity/"+names[i])
        a=time()
        result=function(V,L,nr)
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
