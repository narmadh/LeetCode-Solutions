class Solution:
    def fib(self, n: int) -> int:
        sum=1
        array=[0,1]
        if n==2 or n==1:
            return sum
        if n==0:
            return 0
        for i in range(2,n):
            tem=array[i-1]+array[i-2]
            array.append(tem)
            #print(array)
            sum+=array[i]
        return array[-1]+array[-2]