# import socket
# name = socket.gethostname()
# print(name)

import socket
a="www.google.com"
name = socket.gethostbyname(a)
print(name)

# import time
# print('Hello World')
# time.sleep(5)
# print('Vimal')

# import threading
# import time
# def fun1():
#     for i in range (5):
#         print('Task 1:',i)
#         time.sleep(2)
# def fun2():
#     for i in range (3):
#         print('Task 2:',i)
# fun1()
# fun2()
# print('task completed')

# import threading
# import time
# def fun1():
#     for i in range (5):
#         print('Task 1:',i)
#         time.sleep(2)
# def fun2():
#     for i in range (3):
#         print('Task 2:',i)
# fun1()
# fun2()
# t1=threading.Thread(target=fun1())
# t2=threading.Thread(target=fun2())
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print('completed')
#
# print(threading.current_thread().name)

# import threading
# import time
# def background_task():
#     for i in range(5):
#         print('background_task running', i)
#         time.sleep(1)
# t= threading.Thread(target=background_task)
# t.start()
# print('main thread finished')

# import threading
# import time
# def task1():
#     while True:
#         print('Task 1')
#         time.sleep(1)
# t=threading.Thread(target=task1)
# t.daemon=True
# t.start()
# print('Task over')

# import socket
# s=socket.socket()
# print('socket successfully created')
# port=2797
# host=socket.gethostname()
# s.bind((host,port))
# print('bind success!')
# s.listen(3)
# print('Socket now listening')
# while True:
#     c, addr = s.accept()
#     print('Got connection from', addr)
#     c.send('Thank you for connecting')
#      c.close()

# import threading
# def task1():
#     print("Thread name:",threading.current_thread().name)
# t1=threading.Thread(target=task1)
# t1.start()
# t1.join()