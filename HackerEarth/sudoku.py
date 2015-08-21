import time
start = time.time()
# Difficulty of sudoku example: Hard
sudoku = [
         [8,5,0, 0,0,2, 4,0,0],
         [7,2,0, 0,0,0, 0,0,9],
         [0,0,4, 0,0,0, 0,0,0],

         [0,0,0, 1,0,7, 0,0,2],
         [3,0,5, 0,0,0, 9,0,0],
         [0,4,0, 0,0,0, 0,0,0],

         [0,0,0, 0,8,0, 0,7,0],
         [0,1,7, 0,0,0, 0,0,0],
         [0,0,0, 0,3,6, 0,4,0]
         ]
stack = []
i=0
j=0

# checks if the 3x3 of the inserted element is valid
def check3x3(dummy, row_range, column_range, index):
    another_list = []
    for x in row_range:
        for y in column_range:
            if dummy[x][y] != 0:
                another_list.append(dummy[x][y])
    if len(another_list) == len(set(another_list)):
        return 1
    return 0

# fetches the dimensions of the 3x3 grid
def get_range(point):
    quotient = point/3
    if quotient == 0:
        return [0,1,2]
    elif quotient == 1:
        return [3,4,5]
    else:
        return [6,7,8]

# fetches the next value to be inserted in the sudoku
def get_value(constraint):
    constraint += 1
    for index in range(constraint,10):
        dummy = sudoku[:]
        dummy[i][j] = index

        # check the row
        h_list = dummy[i][:]
        while 0 in h_list:
            h_list.remove(0)
        if len(h_list) != len(set(h_list)):
            continue

        # check the column
        v_list = []
        for p in range(0,9):
            v_list.append(dummy[p][j])
        while 0 in v_list:
            v_list.remove(0)
        if len(v_list) != len(set(v_list)):
            continue
        
        # check the 3x3 grid
        row_range = get_range(i)
        column_range = get_range(j)
        result = check3x3(dummy, row_range, column_range, index)
        if result:
            return index
    return 0

# program starts here
while i < 9:
    j = 0
    while j < 9:
        # finds the next position to fill up in the sudoku 
        if sudoku[i][j] == 0 or 'fault' in str(sudoku[i][j]):
            if sudoku[i][j] == 0:
                constraint = 0
            else:
                constraint = int(sudoku[i][j].split('|')[1])
            #get an valid incremental value and return the result
            result = get_value(constraint) 

            # if result is valid, insert into sudoku
            if result:
                sudoku[i][j] = result
                stack.append([i,j,result])
            # else go back one step and find correct value again
            else:
                sudoku[i][j] = 0
                if len(stack) == 0:
                    print "\nInvalid Sudoku!!\n"
                    exit(0)
                pop = stack.pop() 
                a,b,c = pop[0:3]
                sudoku[a][b] = "fault|%s"%c
                i,j = a,b
                if b == 0:
                    i -= 1
                    j = 2
                else:
                    j -= 1
        j += 1 
    i += 1            

# print sudoku
print "\n\n"
for i in range(0,9):
    for j in range(0,9):
        print sudoku[i][j],
        if j!=8 and j%3 == 2:
            print '|',
        else: 
            print ' ',
    if i!=8 and i%3 == 2:
        print "\n----------+-----------+----------"
    elif i!=8:
        print '\n          |           |          '
print "\n\n"

print time.time() - start
