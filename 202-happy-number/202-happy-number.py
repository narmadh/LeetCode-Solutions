class Solution:
    def isHappy(self, n: int) -> bool:
        def sum_of_squares(num):
            _sum = 0
            while num > 0:
                rem = num%10
                _sum += rem*rem
                num //= 10
            return _sum
        
        fast, slow = n, n
        while True:
            slow = sum_of_squares(slow)
            fast = sum_of_squares(sum_of_squares(fast))
            print(slow,fast)
            if slow == fast:
                break
                
        return slow == 1
                