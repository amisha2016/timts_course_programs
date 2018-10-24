from string import ascii_lowercase

LETTERS = {letter: str(index) for index, letter in enumerate(ascii_lowercase, start=1)} 
def number_alphabet(number):
    alphabet=list(LETTERS.keys())[list(LETTERS.values()).index(number)]
    return alphabet

def print_rangoli(size):
    # your code goes here
    if (0<n<27):
        m=[[0 for x in range (2*n-1)] for y in range (2*n-1) ]
        for i in range(0,n):
            for j in range(0,n-i-1):
                m[i][j]="-"
                print (m[i][j],"-",end='',sep='')             
            g=n
            for j in range(n-i-1,n):
                m[i][j]=number_alphabet(str(g))
                if (n!=1):
                    print (m[i][j],"-",end='',sep='') 
                else: print (m[i][j],end='',sep='')
                g=g-1
            p=n-2                                                           
            for j in range(n,2*n-1):                                        
                m[i][j]=m[i][p]  
                if(j!=2*n-2):
                    print (m[i][j],"-",end='',sep='')                           
                else: print (m[i][j],end='',sep='')
                p=p-1   
            print ()
        r=n-2                                                               
        for i in range(n,2*n-1):                                                                   
            for j in range(0,2*n-1):                                        
                m[i][j]=m[r][j]                                             
                if(j!=2*n-2):                                               
                   print(m[i][j],"-",end='',sep='')                        
                else: print (m[i][j],end='',sep='')                         
            r=r-1  
            print()

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
