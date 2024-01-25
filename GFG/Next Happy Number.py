#User function Template for python3


class Solution:
    def nextHappy (self, N):
        # code here
        if N==1 or N==7:
            return N
        if N<=7:
            return 7
        while(True):
            N+=1;
            temp=N
            while(temp>=10):
                s=0
                while(temp):
                    r=temp%10
                    s+=(r**2)
                    temp//=10
               
                temp=s
            if(temp==1 or temp==7):
                return N
            



