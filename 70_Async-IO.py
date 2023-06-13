import asyncio
import time 

s = time.time()

async def fun1():
    await asyncio.sleep(5)
    print('function1')
    return 'function1'
async def fun2():
    await asyncio.sleep(5)
    print('function2')
    return 'function2'
async def fun3():
    await asyncio.sleep(5)
    print('function3')
    return 'function3'

async def main():
    # await fun1()
    # await fun2()
    # await fun3()
    L = await asyncio.gather(fun1(), fun2(), fun3())
    print(L)

asyncio.run(main())
e = time.time() - s
print(e)
'''
OUTPUT

function1
function2
function3
['function1', 'function2', 'function3']
5.014193058013916
'''