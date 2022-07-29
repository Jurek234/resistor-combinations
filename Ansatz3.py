#Import same as Toby
import itertools, time, os, math
import more_itertools
time_0 = time.time()

#Taking N as variable
N=2



#All Combinations
COMBS = [
    [1, 0, 0 ],
    [1, 0, 1 ],
    [1, 0, 2 ],
    [1, 1, 0 ],
    [1, 1, 1 ],
    [1, 1, 2 ],
    [1, 2, 0 ],
    [1, 2, 1 ],
    [1, 2, 2 ],
    [0, 1, 0 ],
    [0, 1, 1 ],
    [0, 1, 2 ],
    [0, 2, 0 ],
    [0, 2, 1 ],
    [0, 2, 2 ],
    [0, 0, 1 ],
    [0, 0, 2 ]
    ]   


#Plus Z5 to every Combination
lists = []
rr = 0

#ResetListen
COMBSRES = []
r = 0

for i in range(0,N+1):
    COMBSRES.append( [
    [1, 0, 0 ],
    [1, 0, 1 ],
    [1, 0, 2 ],
    [1, 1, 0 ],
    [1, 1, 1 ],
    [1, 1, 2 ],
    [1, 2, 0 ],
    [1, 2, 1 ],
    [1, 2, 2 ],
    [0, 1, 0 ],
    [0, 1, 1 ],
    [0, 1, 2 ],
    [0, 2, 0 ],
    [0, 2, 1 ],
    [0, 2, 2 ],
    [0, 0, 1 ],
    [0, 0, 2 ]
    ] ) 
    rr += 1


for i in range(0,N):
    for n in COMBS:
        n.append(i)
        lists.append(n)
    COMBS = COMBSRES[r]
    r += 1





comb = list(itertools.combinations_with_replacement(lists, N))

print(len(lists))
print(len(comb))



SumZ2, SumZ4 = 0, 0
poss = []
imposs = []

for n in comb:
    SumZ2, SumZ4 = 0, 0
    for x in n:
        SumZ2 = SumZ2 + x[0]
        SumZ4 = SumZ4 + x[1]
    #print (SumZ4 - SumZ2)
    if SumZ4 - SumZ2 == 0:
        poss.append(n)
    else:
        imposs.append(n)


check2c = 0
for x in poss:
    check2c += 1
    for n in x:
        if n[1] > 0 or n[2] > 0:
            if n[3] == 0:
                del poss[check2c]




print(len(poss))
#print (poss)
print("""

""")
#print(imposs)


























time_end = time.time()
print(time_end-time_0,"s")