import random
import time
import sys
import numpy as np
import matplotlib.pyplot as plt

def initRandomLists(options):
    
    if options == 1:
       ret = random_list(1, 100, 50)
    elif options == 2:
        ret = random_list(1, 1000, 500)
    elif options == 3:
        ret = random_list(1, 10000, 5000)
    elif options == 4:
         ret = random_list(1, 100000, 50000)
    else:
        print('Niste uneli odgovarajuci parametar\nPokrenite opet program kada unesete odgovarajuci parametar\n')
        ret = []
    return ret

def random_list (min, max, elements):
    list = random.sample(range(min, max), elements)
    return list

def printList(l):
    print(l)

def racunanjeVremena(vrstaSorta,l):
    print('Ulazni lista elemenata: ')
    printList(l)
    daLiJeSortirano(l)
    start_time = time.clock()
    vrstaSorta(l)
    end_time = time.clock() - start_time
    print("Duration: ", end_time)
    print('\n')
    printList(l)
    daLiJeSortirano(l)

def racunanjeVremenaQuicksorta(l,duzina):
    print('Ulazni lista elemenata: ')
    printList(l)
    daLiJeSortirano(l)
    print('\n QUICKSORT \n')
    start_time = time.clock()
    randomizedQuicksort(l,0,duzina-1)
    end_time = time.clock() - start_time
    print("Duration: ", end_time)
    print('\n')
    printList(l)
    daLiJeSortirano(l)

def daLiJeSortirano(l):
    sorted=l[:]
    sorted.sort()
    if(sorted==l):
        print("\nSortirano!\n-------------------------------------------------------------------\n")
    else: 
        print("\nNije sortirano!\n--------------------------------------------------------------\n")

def selectionSort(l):
    print('\n SELECTION SORT \n')
    n=len(l)
    for i in range(0,n-1):
        najmanji=i
        for j in range (i+1,n):
            if(l[j]<l[najmanji]):
               najmanji=j
        l[i],l[najmanji]= l[najmanji], l[i]


def radixSort(l):
    print('\n RADIKS SORT \n')
    najveci=max(l)
    eksponent=1
    while najveci/eksponent > 0:
        countingSort(l,eksponent)
        eksponent*=10         #10^i

def countingSort(l, eksp):

    sortiran = [0] * len(l)  #u njega smestamo
    brojac = [0] * 10        
  
    for it in range(0, len(l)):
        pozicija = (l[it]/eksp)        #indeksi elemenata u nizu
        brojac[ pozicija%10 ] += 1  
    for it in range(1,10):             #indeksi brojaca
        brojac[it] += brojac[it-1]
    
    i = len(l)-1
    while i>=0:                           #vadjenje iz bucketa
        pozicija = (l[i]/eksp)
        sortiran[ brojac[ pozicija%10 ] - 1] = l[i]
        brojac[ pozicija%10 ] -= 1
        i -= 1
 
    for i in range(0,len(l)):     #nova sortirana lista
        l[i] = sortiran[i]

def randomizedQuicksort(L,p,r):
    if p<r:
        q=randomizedPartition(L,p,r)
        randomizedQuicksort(L,p,q-1)
        randomizedQuicksort(L,q+1,r)

def randomizedPartition(L,p,r):
    k= random.randint(p,r)
    L[r],L[k] = L[k], L[r]
    return partition(L,p,r)

def partition(L,p,r):
    i=p-1
    for j in range(p,r):
        if L[j]<= L[r]:
            i=i+1
            L[i],L[j]=L[j],L[i]
    L[i+1],L[r]=L[r],L[i+1]
    return i+1

def CreatePlot(input_data, exec_time, algo_name):
    fig = plt.figure()     
    fig.suptitle(algo_name, fontsize=14, fontweight='bold')    
    
    ax = fig.add_subplot(111)
    fig.subplots_adjust(top=0.85)       
    ax.set_title('Vreme izvrsenja')
    ax.set_xlabel('Ulaz [n]')    
    ax.set_ylabel('Vreme [ms]')
    ax.plot(input_data, exec_time, '-', color='green')

    
    print(algo_name)
    for i in range(0, len(input_data)):
        print("input_data: ", input_data[i], ", exec_time: ", exec_time[i])

    return fig

def ShowPlot():
    plt.show()
    
    


def AnalizaQuicksorta():
    # Measure exeuction time
    algo_name = "[Quick sort] "
    input_data = [1,10,100,1000,10000,100000,1000000]
    exec_time = []
    for n in input_data:
        l=random.sample(range(0,1000001),n)
        start_time = time.clock() # expressed in seconds
        randomizedQuicksort(l,0,len(l)-1)
        end_time = time.clock()
        exec_time.append((end_time - start_time)*1000) #get miliseconds
        
    
    CreatePlot(input_data, exec_time, algo_name)

def Analiza(vrstaSorta):
    algo_name = "[Uporedna analiza] "
    input_data = [1,10,100,1000,10000] #,100000,1000000]
    exec_time = []
    
    for n in input_data:
        l=random.sample(range(0,1000001),n)
        start_time = time.clock() # expressed in seconds
        vrstaSorta(l)
        end_time = time.clock()
        exec_time.append((end_time - start_time)*1000) #get miliseconds
    
    CreatePlot(input_data, exec_time, vrstaSorta.__name__)

#####################___________________________TESTNI SLUCAJEVI________________________#######################    

#za argumente izabrati od 1 do 4
# 1 --> lista od 50 random elemenata u opsegu od 1 do 100
# 2 --> lista od 500 random elemenata u opsegu od 1 do 1000
# 3 --> lista od 5000 random elemenata u opsegu od 1 do 10000
# 4 --> lista od 50000 random elemenata u opsegu od 1 do 100000

#L = initRandomLists(1)
#racunanjeVremena(selectionSort,L)


#L=initRandomLists(1)
#racunanjeVremena(radixSort,L)


#L=initRandomLists(1)
#racunanjeVremenaQuicksorta(L,len(L))


################____________GRAFICKA ANALIZA_____________###############################################

Analiza(selectionSort)  #smanjiti vreme na 10000 jer se dugo izvrsava
#Analiza(radixSort)
#AnalizaQuicksorta()

ShowPlot()
###########_________________________________________##################################

 



