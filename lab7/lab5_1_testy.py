from dimacs import *
from time import time

#additional given data
names=["16-cell","AT","chvatal","clique4","clique5",
"clique20","clique100","clique200","cycle","example-fig5",
"franklin","from-paper","grid5x5","grotzsch","house","K33",
"nonplanar-ex1","nonplanar-ex2","path","petersen",
"simple","simple-noninterval1","simple-noninterval2"]

#---------------------------------------------#

def runtests(function):
    no_tests=len(names)
    passed=0
    total_time=0
    print("Sprawdzanie czy graf jest planarny:")
    for i in range(no_tests):
        sol=int(readSolution("plnar/"+names[i]))
        V,L=loadWeightedGraph("plnar/"+names[i])
        a=time()
        result=function(V,L)
        b=time()
        print("Test ",i,":",sep='')
        print("Uzyskany wynik: ",result,sep='')
        print("Prawidłowy wynik: ",bool(sol),sep='')
        print("Czas wykonania: {ex_time:.2f} s".format(ex_time=b-a))
        total_time+=b-a
        if result==sol:
            passed+=1
            print("Test zaliczony!")
        else: print("Test niezaliczony!")
        print()
    print("Liczba zaliczonych testów: ",passed,"/",no_tests,sep='')
    print("Łączny czas wykonania: {total:.2f} s\n".format(total=total_time))
