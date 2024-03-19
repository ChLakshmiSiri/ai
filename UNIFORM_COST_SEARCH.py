#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#UNIFORM COST SEARCH
# source code
g=eval(input('Enter graph: '))
c=eval(input('Enter costs: '))
s=input('Enter source: ')
d=input('Enter destination: ')

q=s
l=[]
cost=0
minc=[]

def add():
  k=0
  if q not in g:
    return
  for i in g[q]:
    l.append([cost+c[q][k],q,i])
    if i==d:
      minc.append(cost+c[q][k])
    k+=1

if q!=d:
  add()

while l:
  j=min(l)
  print(j)
  q=j[2]
  cost=j[0]
  l.remove(j)

  if q!=d:
    add()

print('Minimum cost =',min(minc))

"""
output-1
Enter graph: { 'siri':['cupid','arjun'], 'cupid':['devi'], 'arjun':['ammu'], 'ammu':['devi']}
Enter costs: { 'siri':[88,56], 'cupid':[78], 'arjun':[34], 'ammu':[120] }
Enter source: siri
Enter destination: devi
[56, 'siri', 'arjun']
[88, 'siri', 'cupid']
[90, 'arjun', 'ammu']
[166, 'cupid', 'devi']
[210, 'ammu', 'devi']
Minimum cost = 166

output-2
Enter graph: {'a':['b','c'],'b':['d'],'c':['e'],'d':['f'],'e':['f']}
Enter costs: {'a':[5,4],'b':[3],'c':[1],'d':[2],'e':[3]}
Enter source: a
Enter destination: f
[4, 'a', 'c']
[5, 'a', 'b']
[5, 'c', 'e']
[8, 'b', 'd']
[8, 'e', 'f']
[10, 'd', 'f']
Minimum cost = 8

"""

