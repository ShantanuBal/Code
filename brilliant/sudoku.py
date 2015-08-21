#l = [[1,2,3],[2,3,1],[3,1,2]]
l = [[0,0,0],[0,0,0],[0,0,0]]
stack = []
i=0
j=0

def get_value(constraint):
    constraint += 1
    for index in range(constraint,4):
        dummy = l
        dummy[i][j] = index
        for p in range(0,3):
            list = dummy[p]
            while 0 in list:
                list.remove(0)
            if len(list) != len(set(list)):
                break
        else:
            return index
    return 0

while i < 3:
    j = 0
    while j < 3:
        print i,'\t',j
        if l[i][j] == 0 or 'fault' in str(l[i][j]):
            if l[i][j] == 0:
                constraint = 0
            else:
                constraint = int(l[i][j].split('|')[1])
            result = get_value(constraint) #get an valid incremental value and return result
            if result:
                l[i][j] = result
                stack.append([i,j,result])
            else:
                pop = stack.pop() 
                a,b,c = pop[0:3]
                l[a][b] = "fault|'%s'"%c
                i,j = a,b
                if b == 0:
                    i -= 1
                    j = 2
                else:
                    j -= 1
        j += 1 
    i += 1            

for i in range(0,3):
    for j in range(0,3):
        print l[i][j],'\t',
    print
