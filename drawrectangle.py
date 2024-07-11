'''
Please draw a rectangle with row=4, col =6 and result

******
*    *
*    *
******

'''

def drawRectangle(m,n):
    for row in range(m):
        if row == 0 or row == (m-1):
            print("*" * n);
        else:
            print("*" + " " * (n-2) + "*");
            
drawRectangle(4,6);