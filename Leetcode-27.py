if __name__ == "__main__":
    nums = list(map(int,input().split()))
    val = int(input())
    num = list()
    for i in nums:
        if i!= val:
            num.append(i)
    nums.clear()
    for i in num:
        nums.append(i)
    print(nums)