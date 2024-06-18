import sys
import typing

def findTwoSum(nums: typing.List, target: int) -> typing.List:
    for p1 in range(0,len(nums)):
        numberToFind: int = target - nums[p1]
        for p2 in [p1+1, len(nums)-1]:
            if numberToFind == nums[p2]:
                return [p1,p2]
    return [-1,-1]

def main() -> int:
    nums: typing.List = [1,2,3,4,5,9]
    result: typing.List = findTwoSum(nums, 11)
    if (result[0] != -1 and result[1] != -1):
        print("Indices {},{}".format(result[0], result[1]))
    else:
        print("No two sum solution")
    return 0

if __name__ == '__main__':
    sys.exit(main())
