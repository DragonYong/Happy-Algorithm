class Solution:

    def addBinary(self, a, b):
        # res = int(a) + int(b)
        # binary = []
        # while res:
        #     binary.append(res % 2)
        #     res = res // 2
        # return binary[::-1]
        # return '{0:b}'.format(int(a, 2) + int(b, 2))
        x, y = int(a, 2), int(b, 2)
        while y:
            answer = x ^ y
            carry = (x & y) << 1
            x, y = answer, carry
        return bin(x)[2:]


if __name__ == '__main__':
    a = "11"
    b = "1"
    res = Solution()
    print(res.addBinary(a, b))
    # print(int('11', 2))
    # a = 'sdsjdk'
    # print(bin(2))
    # print(11 ^ 1)
    print(bin(1001+10011))
