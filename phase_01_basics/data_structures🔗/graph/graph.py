INF = float('inf')
v = int(input("Enter no of vertices : "))
graph = []

for i in range(v):
    print("Enter row ",i+1," :",end = " ")
    row = list(map(int,input().split()))
    graph.append(row)

for i in range(v):
    for j in range(v):
        if i != j and graph[i][j] == 0:
            graph[i][j] = INF

print("\nClean Matrix .......")
print("="*20)
for row in graph:
    print(row)

print("="*20)

for k in range(v):
    for i in range(v):
        for j in range(v):
            if graph[i][k]+graph[k][j] < graph[i][j]:
                graph[i][j] = graph[i][k]+graph[k][j]
                
for row in graph:
    print(row)
print("="*20)