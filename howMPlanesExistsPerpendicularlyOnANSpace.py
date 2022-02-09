from itertools import combinations
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

    table = np.empty(getShape(axis))
    
    def combinar(table,axis,count):
        pass

    combinar(table,axis,[0 for _ in axis])

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