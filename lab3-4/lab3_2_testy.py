from dimacs import *
from time import time

#additional given data
names=["clique5","clique20","cycle","geo20_2b","clique100",
"clique200","geo20_2c","geo100_2a","grid5x5","mc1","mc2",
"path","rand20_100","rand100_500","simple","trivial"]

#"grid100x100" takes too much time (about 7 minutes)

#---------------------------------------------#

def runtests(function):
    no_tests=len(names)
    passed=0
    total_time=0
    print("Znajdowanie spójności krawędziowej")
    print("przy użyciu algorytmu Stoera-Wagnera:")
    for i in range(no_tests):
        sol=int(readSolution("connectivity/"+names[i]))
        V,L=loadWeightedGraph("connectivity/"+names[i])
        a=time()
        result=function(V,L)
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
