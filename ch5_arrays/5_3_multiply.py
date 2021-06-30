
arr1 = [1, 9, 3, 7, 0, 7,7 ,2 ,1]
arr2 = [-7,6,1,8,3,8,2,5,7,2,8,7]
ans = [-1,4,7,5,7,3,9,5,2,5,8,9,6,7,6,4,1,2,9, 2, 7]


# problem: given two arrays,
# find the product of the two arrays where each element in the arrays are a single digit integer
# solution same process as elementary multiplication, multiplying one digit from an array with all digits from the other array.
# we have to add 0s for digits starting in higher slots (10s, 100s, 1000s), by adding 0s to a current product array.
# the number of 0s is calculated by subtracting the length of the array by the current iteration in reverse order:
# then, we add our current ans with the current product using numpy
# finally, switch the sign of the first digit of
# answer if only one of the arrays has a negative integer in the first index

#how to improve: how to cut down the number of times we reverse arrays?
# how to calculate number of digits the product will have to have a set array size
def array_mult(A: [int], B:[int]) -> [int]:
    ans = []
    for i in reversed(range(len(B))):
        product = [0] * (len(B) - i - 1)
        carry = 0
        for j in reversed(range(len(A))):
            current = abs(B[i] * A[j]) + carry
            carry = current // 10
            product.append(current % 10)
        if carry:
            product.append(carry)
        product.reverse()
        ans = add_arrays(product, ans)
    if A[0] * B[0] < 0:
        ans[0] = -ans[0]
    return ans


def add_arrays(A, B) -> [int]:
    a, b = len(A)-1, len(B)-1
    ans = []
    carry = 0
    while a >= 0 and b >= 0:
        current = A[a] + B[b] + carry
        carry = current // 10
        ans.append(current % 10)
        a -= 1
        b -= 1
    if a < b:
        a = b
        A = B
    for i in reversed(range(a+1)):
        current = A[i] + carry
        carry = current // 10
        ans.append(current % 10)
    if carry:
        ans.append(1)
    ans.reverse()
    return ans
# print(array_mult([1,2,3], [-1,1]))
print(array_mult(arr1,arr2) == ans)
# print(add_arrays([1,7,0,0], [1,0,0,0,0]))