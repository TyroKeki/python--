class Solution:
    def sum(self, num1: int, num2: int) -> int:
        return num1 + num2

    def repeatedNTimes(self, nums: list[int]) -> int:
        a = set()
        for num in nums:
            if num in a:
                rst = num
                break
            else:
                a.add(num)
        return rst

if __name__ == '__main__':
    sol = Solution()
    rst = sol.repeatedNTimes([1,2,3,3])
    print(rst)