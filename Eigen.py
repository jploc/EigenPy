#Eigen.py
#Small Python script to calculate (normalized) Eigenvalues for an adjacency matrix.
#The end goal is a JS-based GUI for diagramming an adjacency matrix so I can run this math on it. This is just so I understand the math.

# centrality = iterate(adjacencyMatrix, iterationCount). Original equation is c[i,t+1] = sum[j]( d[ij] * c[j,t] )
def iterate(adjMatrix,iterCount):
    cjt=[0.5 for i in range(len(adjMatrix))]
    for t in range(iterCount):
        tPlusOne=[sum(adjMatrix[i][j]*cjt[j] for j in range(len(cjt))) for i in range(len(cjt))]
        cnorm=[tPlusOne[i]/sum(tPlusOne) for i in range(len(cjt))]
        cjt=cnorm
    return cjt

#same thing but iterates until a certain decimal precision is reached. add True to truncate to whatever precision you specified
def converge(adjMatrix,precision,trunc=False):
    cjt=[0.5 for i in range(len(adjMatrix))]
    conv=False
    while conv is False:
        tPlusOne=[sum(adjMatrix[i][j]*cjt[j] for j in range(len(cjt))) for i in range(len(cjt))]
        cnorm=[tPlusOne[i]/sum(tPlusOne) for i in range(len(cjt))]
        if round(cjt[0],precision) == round(cnorm[0],precision): #to avoid wasting computation
            if len(cjt) == sum(1 for x, y in zip(cjt,cnorm) if round(x,precision)==round(y,precision)): #jank
                conv = True
        cjt=cnorm
    if trunc is True:
        for i in range(len(cjt)): cjt[i]=round(cjt[i],precision)
    return cjt

# Make this any size! but it has to be a square, because it's an adjacency matrix.
matrixd=[[1,3,3,2,4],
         [0,1,0,5,3],
         [0,0,1,2,4],
         [0,2,3,1,0],
         [1,3,2,0,1]]

matrixc=converge(matrixd,10,True)

print(matrixc)
print(sum(matrixc)) #should equal 1, but due to precision loss, sometimes doesn't.