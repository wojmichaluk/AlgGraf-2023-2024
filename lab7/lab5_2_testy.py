from dimacs import *
from time import time

#additional given data
names=["clique5","clique20","clique100","grid5x5",
"grid100x100","pp100","rand20_100","rand100_500",
"simple","simple2","trivial","trivial2","worstcase"]

#---------------------------------------------#

def runtests(function):
    no_tests=len(names)
    passed=0
    total_time=0
    print("Znajdowanie maksymalnego przepływu:")
    for i in range(no_tests):
        sol=int(readSolution("flow/"+names[i]))
        V,L=loadDirectedWeightedGraph("flow/"+names[i])
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
