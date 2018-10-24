def count_substring(string, sub_string):
    #for j in range(0,len(sub_string)):
    j=0
    count=0
    for i in range(0,len(string)):
       # print("i",i)
        #print("j",j)
        if(string[i]==sub_string[j] and j<len(sub_string)):
            j=j+1
            if(j==len(sub_string)):
                count=count+1
        elif(string[i]!=sub_string[j]):
            j=0
        if(j>=len(sub_string)):
            if(isPalindrome(sub_string)):
                j=1
            else: j=0
        #i=i+1            
     #   elif(string[i]==sub_string[j]):       
      #          i=i+1
       #         j=j+1
    return count

# function to check string is 
# palindrome or not

def isPalindrome(s):
     
    # Using predefined function to 
    # reverse to string print(s)
    rev = ''.join(reversed(s))
 
    # Checking if both string are 
    # equal or not
    if (s == rev):
        return True
    return False

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
