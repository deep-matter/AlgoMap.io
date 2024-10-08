
def sum_triples(Array):
    start = 0 
    Slicer = start - len(Array) // 2
    triples = []

    for i in range(1 , len(Array)):
        # print(Array[start])
        # print(Array[i] )
        # print( Array[Slicer - 1])
        sums = Array[start] + Array[i] + Array[Slicer]
        if sums == 0 :
             triples.append([start, i, Slicer - 1])
        #start +=1
        #Slicer +=1

        
    return triples

        




if __name__ == "__main__":
    Array = [-1,0,1,2,-1,-4]

    output = sum_triples(Array)
    print(output)

