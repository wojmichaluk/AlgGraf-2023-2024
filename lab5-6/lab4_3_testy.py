from dimacs import *
from time import time

#additional given data
names=["AT","clique4","clique5","clique20",
"clique100","clique200","cycle3","example-fig5",
"house","interval-rnd6","interval-rnd8","interval-rnd10",
"interval-rnd20","interval-rnd30","interval-rnd50",
"interval-rnd100","nonplanar-ex1","path","simple",
"simple-noninterval1","simple-noninterval2"]

#---------------------------------------------#

def runtests(function):
    no_tests=len(names)
    passed=0
    total_time=0
    print("Znajdowanie liczby chromatycznej grafu:")
    for i in range(no_tests):
        sol=int(readSolution("coloring/"+names[i]))
        V,L=loadWeightedGraph("coloring/"+names[i])
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
