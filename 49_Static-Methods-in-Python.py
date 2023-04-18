def mul(a, b):
    print('Outside Class !!')
    return a*b


class Math:
    @staticmethod
    def mul(a, b):
        print('hello')
        return a*b


a = Math()
print(a.mul(9, 2))
print(Math.mul(9, 2))
print(mul(9, 2))
'''
OUTPUT

hello
18
hello
18
Outside Class !!
18
'''
