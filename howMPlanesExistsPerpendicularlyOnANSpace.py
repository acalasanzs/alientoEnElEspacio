from itertools import combinations
import string
import numpy as np
dimension = 7
planeDimension = 3

def tableCombinations(planeDimension,dimension):
    def do(planeDimension,dimension):

        def plane(o,m):

            return [x for x in range(o,m)]
        
        column = [] 

        planeSet = plane(0,dimension)

        for subset in combinations(planeSet,planeDimension):
            column.append(subset)

        return column
    return do(planeDimension,dimension)
def table(planeDimension,dimension):

    def do(planeDimension,dimension):
        def plane(o,m):

            return [x for x in range(o,m)]

        column = []

        for i in range(dimension):

            for j in range(dimension):

                if planeDimension+i+j <= dimension:

                    planeSet = plane(i+j+1,planeDimension+i+j)     # Ultimas combinaciones

                    dplane = [i] + planeSet

                    column.append(dplane)
        return column
    
    def inverse(planeDimension,dimension):
        def plane(o,m):
            return [x for x in range(o,m,-1)]
        column = []

        for i in range(dimension):

            for j in range(dimension-1,0,-1):

                if i+j >= i-planeDimension+j+1 and i+j <= dimension-1:
                    planeSet = plane(i+j,i-planeDimension+j+1)     # Ultimas combinaciones
                if planeSet[-1] > i:
                    dplane = [i] + planeSet

                    column.append(dplane)

        return column

    table = []

    for x,j in zip(do(planeDimension,dimension),inverse(planeDimension,dimension)):

        table.append(x)

        table.append(j)
    
    for i,x in enumerate(table):

        if set(x) == set(table[i]):
            
            table.remove(x)
        


    return table

def dimensionalTable(planeDimension, dimension):

    def arange(o,m):

        return [x for x in range(o,m)]
    def ejes(planeDimension, dimension):
        axis = []

        for i in range(planeDimension):

            axis.append(arange(0,dimension-i))

        return axis
    
    axis = ejes(planeDimension, dimension)
    
    def getShape(axis):
        shape = []

        for i in axis:

            shape.append(len(i))
        return shape

    table = np.chararray(getShape(axis),planeDimension*3-1)
    
    def checkAllAxis(table, coordenadas):
        def column(table,coordenadas,index):
            while True:
                cSet = [0 for _ in coordenadas]
                change = False
                if coordenadas[index] < table.shape[index]:
                    if index > 0:
                        if coordenadas[index-1] == dimension:
                            current = index
                            while current > 0:
                                current -= 1
                                coordenadas[current] = 0
                            coordenadas[index] += 1
                            change = False
                        else:
                            current = index
                            toSum = -planeDimension
                            if change:
                                while current > 0:
                                    current -= 1
                                    coordenadas[current] = 0
                                    toSum = 0
                            if coordenadas[index] < dimension:
                                if index > toSum:
                                    while coordenadas[toSum] >= dimension:
                                        toSum += 1
                                    coordenadas[toSum] += 1
                    else:
                        if not coordenadas[index + 1] > 0:
                            coordenadas[index] += 1 
                else:
                    if index+1 <= planeDimension:
                        index += 1
                        change = True
                    else:
                        break
                """ cSet = tuple([i-1 for i in coordenadas])
                print(cSet)
                table[cSet] = str(",".join(["n"+str(i) for i in coordenadas])) """
                print(coordenadas)
        index = 0
        column(table,coordenadas,index)

    coordenadas = [0 for _ in axis]

    checkAllAxis(table, coordenadas)


    return table

if __name__ == "__main__":
    def cambioN(table):
        total = []

        for n in range(3,11):

            lens = []

            for m in range(2,n):

                lens.append([len(table(m,n)),(n,m)])

            total.append(lens)
        return total

    def cambioM(table):

        total = []

        for n in range(3,11):

            lens = []

            for m in range(2,n):

                tab = table(m,n)
                count = 0
                last = tab[0][0]
                for k in range(0,len(tab)):
                    
                    if last == tab[k][0]:
                        count += 1

                    last = tab[k][0]
                lens.append(count)
            total.append((lens,n))
        return total

    def cambioMA(table):

        total = []

        def calculateK(tab):
            total = []
            def countK(count, total):
                realCount = 0
                last = tab[count][0]
                for k in range(count,len(tab)):
                    
                    if last == tab[k][0]:
                        count += 1
                        realCount += 1
                    else:
                        total.append(realCount)
                        countK(count,total)
                        break

                    last = tab[k][0]
                return count

            total.append(len(tab)-countK(0,total))
            return total

        for n in range(3,11):

            lens = []

            for m in range(2,n):

                tab = table(m,n)
                count = calculateK(tab)
                lens.append((count,m))
            total.append((lens,n))
        return total
    """ print(cambioMA())
    print("\n")
    print(cambioM())
    print("\n")
    print(cambioN())
    print("\n")
    pentaDimensionalSpaceTriDimensionalPlanes = table(3,5)
    print(pentaDimensionalSpaceTriDimensionalPlanes,len(pentaDimensionalSpaceTriDimensionalPlanes))
    """
    """ print(cambioMA(tableCombinations))
    print("\n")
    print(cambioM(tableCombinations))
    print("\n")
    print(cambioN(tableCombinations))
    print("\n")
    pentaDimensionalSpaceTriDimensionalPlanes = tableCombinations(3,5)
    print(pentaDimensionalSpaceTriDimensionalPlanes,len(pentaDimensionalSpaceTriDimensionalPlanes))
    """
    print(dimensionalTable(3,5))