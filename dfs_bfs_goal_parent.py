#!/usr/bin/env python
# coding: utf-8

# In[1]:


def DFS(graph,start,goal):
    visited=[]
    frontier=[]
    visited.append(start)
    frontier.append(start)
    while frontier:
        node=frontier.pop()
        print(node,end=' ')
        if node==goal:
            print("\nGoal Node is Reached")
            break;
        for i in graph[node]:
            if i not in visited:
                visited.append(i)
                frontier.append(i)
                
n=input("Enter Goal Node : ")
graph_dict={
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
DFS(graph_dict,'A',n)


# In[2]:


def DFS(graph,start):
    visited=[]
    frontier=[]
    visited.append(start)
    frontier.append(start)
    while frontier:
        node=frontier.pop()
        print(node,end=' ')
        for i in graph[node]:
            if i not in visited:
                visited.append(i)
                frontier.append(i)
                
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
DFS(graph,'A')


# In[5]:


def bfs(graph,start):
    frontier=[]
    explored=[]
    frontier.append(start)
    explored.append(start)
    while frontier:
        node=frontier.pop(0)
        print(node,end=' ')
        for i in graph[node]:
            if i not in explored:
                explored.append(i)
                frontier.append(i)
                
                
graph= {
    'A' : ['B','C'],
    'B' : ['D','E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}
bfs(graph,'A')


# In[9]:


def bfs(graph,start,goal):
    frontier=[]
    explored=[]
    frontier.append(start)
    explored.append(start)
    while frontier:
        node=frontier.pop(0)
        print(node,end=' ')
        if node==goal:
            print("\nReached the goal node")
            break
        for i in graph[node]:
            if i not in explored:
                explored.append(i)
                frontier.append(i)
                
n=input("Enter the goal node   ")                
graph= {
    'A' : ['B','C'],
    'B' : ['D','E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}
bfs(graph,'A',n)


# In[16]:


def bfs(graph,start,goal):
    explored=[]
    frontier=[(start,None)]
    explored.append(start)
    while frontier:
        node,parent=frontier.pop(0)
        print(node,parent)
        
        if node==goal:
            print("\nReached the goal node")
            print("parent of the goal node is ",parent)
            break
        for i in graph[node]:
            if i not in explored:
                explored.append(i)
                frontier.append((i,node))
                
n=input("Enter the goal node   ")                
graph= {
    'A' : ['B','C'],
    'B' : ['D','E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}
bfs(graph,'A',n)


# In[ ]:





# In[ ]:





# In[ ]:




