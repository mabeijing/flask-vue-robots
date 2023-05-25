# def subgen():
#     while True:
#         x = yield
#         yield x + 10
#
# def delegator(gen):
#     yield from gen
#
# gen = subgen()
# de = delegator(gen)
#
# next(de)                          # 启动delegator
# print(de.send(2))                        # 等价于 gen.send(2)，输出12


"""
首先，生成器必须是主函数和生成器之间的来回切换

如果是独立的多个生气成，yield是无法互相切换的

一个主函数，可以关联多个生成器。来回调用

主函数可以给生成器发送数据，并且，在生成器下一次yield是，返回控制权

事件循环的概念，main函数中，新增了很多生成器函数，main函数循环发送数据，触发生成器执行，所以生成器函数，也就是协程函数，必须要有明确的yield，用于非阻塞返回

事件循环，必须是独立线程，反复的调用异步函数的next()


如果有yield from 这就是生成器代理，用于管理生成器的。
yield from gem 会next(gem),直接托管给gem的yield去转出控制权

gem的yield，会把控制权转给主线程。主线程可以发送在地调度yield from, 继续执行生成器

当gem 最后一个yield

"""


def file_space():


    print('666啊')
    x = yield 666
    print(x)
    yield 777
    yield 888

def main(gem):
    y = yield from gem
    print(y)
    return "beijing"


g = file_space()

m = main(g)

print(next(m))
print(m.send(33))
print(next(m))
print(next(m))

