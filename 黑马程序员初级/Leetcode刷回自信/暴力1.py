class Solution:
    def countGoodTriplets(self, arr: list[int], a: int, b: int, c: int) -> int:
        length = len(arr)
        res = 0
        for i in range(length):
            for j in range(i+1,length):
                for k in range(j+1,length):
                    if abs(arr[i] - arr[j])<=a:
                        if abs(arr[j]-arr[k])<=b:
                            if abs(arr[i]-arr[k])<=c:
                                res+=1

        return res

if __name__ == '__main__':
    s = Solution()
    res = s.countGoodTriplets([3, 0, 1, 1, 9, 7], 7, 2, 3)
    print(res)