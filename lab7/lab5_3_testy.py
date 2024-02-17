from dimacs import *
from time import time

#additional given data
names=["simple_sat","simple_unsat","sat5_10","sat5_20",
"sat15_30","sat30_50","sat30_100","sat100_100","sat100_100",
"sat100_150","sat100_200","sat100_250","sat100_400"]

#---------------------------------------------#

def runtests(function):
    no_tests=len(names)
    passed=0
    total_time=0
    print("Sprawdzanie spełnialności formuły:")
    for i in range(no_tests):
        sol=int(readSolution("sat/"+names[i])[-1])
        V,F=loadCNFFormula("sat/"+names[i])
        a=time()
        result=function(V,F)
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
