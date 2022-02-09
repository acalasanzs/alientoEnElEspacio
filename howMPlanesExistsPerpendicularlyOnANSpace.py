dimension = 7
planeDimension = 3


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

    last = table[0]
    
    for i,x in enumerate(table):

        if set(x) == set(table[i]):

             table.remove(x)
        


    return table

""" table = table(planeDimension,dimension)

print(table,len(table)) """

if __name__ == "__main__":
    def cambioN():
        total = []

        for n in range(3,11):

            lens = []

            for m in range(2,n):

                lens.append([len(table(m,n)),(n,m)])

            total.append(lens)
        return total

    def cambioM():

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

    def cambioMA():

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
    print(cambioMA())
    print("\n")
    print(cambioM())

de3a10 = [[[3, (3, 2)]], [[6, (4, 2)], [3, (4, 3)]], [[10, (5, 2)], [6, (5, 3)], [3, (5, 4)]], [[15, (6, 2)], [10, (6, 3)], [6, (6, 4)], [3, (6, 5)]], [[21, (7, 2)], [15, (7, 3)], [10, (7, 4)], [6, (7, 5)], [3, (7, 6)]], [[28, (8, 2)], [21, (8, 3)], [15, (8, 4)], [10, (8, 5)], [6, (8, 6)], [3, (8, 7)]], [[36, (9, 2)], [28, (9, 3)], [21, (9, 4)], [15, (9, 5)], [10, (9, 6)], [6, (9, 7)], [3, (9, 8)]], [[45, (10, 2)], [36, (10, 3)], [28, (10, 4)], [21, (10, 5)], [15, (10, 6)], [10, (10, 7)], [6, (10, 8)], [3, (10, 9)]]]
de3a10M = [([2], 3), ([4, 2], 4), ([7, 4, 2], 5), ([11, 7, 4, 2], 6), ([16, 11, 7, 4, 2], 7), ([22, 16, 11, 7, 4, 2], 8), ([29, 22, 16, 11, 7, 4, 2], 9), ([37, 29, 22, 16, 11, 7, 4, 2], 10)]
de3a10MA = [([([2, 1], 2)], 3), ([([3, 2, 3], 2), ([2, 1], 3)], 4), ([([4, 3, 2, 6], 2), ([3, 2, 3], 3), ([2, 1], 4)], 5), ([([5, 4, 3, 2, 10], 2), ([4, 3, 2, 6], 3), ([3, 2, 3], 4), ([2, 1], 5)], 6), ([([6, 5, 4, 3, 2, 15], 2), ([5, 4, 3, 2, 10], 3), ([4, 3, 2, 6], 4), ([3, 2, 3], 5), ([2, 1], 6)], 7), ([([7, 6, 5, 4, 3, 2, 21], 2), ([6, 5, 4, 3, 2, 15], 3), ([5, 4, 3, 2, 10], 4), ([4, 3, 2, 6], 5), ([3, 2, 3], 6), ([2, 1], 7)], 8), ([([8, 7, 6, 5, 4, 3, 2, 28], 2), ([7, 6, 5, 4, 3, 2, 21], 3), ([6, 5, 4, 3, 2, 15], 4), ([5, 4, 3, 2, 10], 5), ([4, 3, 2, 6], 6), ([3, 2, 3], 7), ([2, 1], 8)], 9), ([([9, 8, 7, 6, 5, 4, 3, 2, 36], 2), ([8, 7, 6, 5, 4, 3, 2, 28], 3), ([7, 6, 5, 4, 3, 2, 21], 4), ([6, 5, 4, 3, 2, 15], 5), ([5, 4, 3, 2, 10], 6), ([4, 3, 2, 6], 7), ([3, 2, 3], 8), ([2, 1], 9)], 10)]