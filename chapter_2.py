class A:    a = "I am a class attribute!"    x = A()y = A()print(x.a)print(A.a)# class Robot:    #     Three_Laws = {#         """A robot may not injure a human being or, through inaction, allow a human being to come to harm.""",#         """A robot must obey the orders given to it by human beings, except where such orders would conflict with the First Law.,""",#         """A robot must protect its own existence as long as such protection does not conflict with the First or Second Law."""#         }    #     def __init__(self, name, build_year):#         self.name = name#         self.build_year = build_year        # for number, text in enumerate(Robot.Three_Laws):#     print(str(number+1) + ":\n" + text)    # class C:    #     counter = 0    #     def __init__(self):#         type(self).counter += 1        #     def __del__(self):#         type(self).counter -= 1        # if __name__ == "__main__":#     x = C()#     print("Number of instances: : " + str(C.counter))#     y = C()#     print("Number of instances: : " + str(C.counter))#     del x#     print("Number of instances: : " + str(C.counter))#     del y#     print("Number of instances: : " + str(C.counter))class Robot:    __counter = 0        def __init__(self):        type(self).__counter += 1            # Notice we don't pass self    @staticmethod    def RobotInstances():        return Robot.__counter    if __name__ == "__main__":    print(Robot.RobotInstances())    x = Robot()    print(x.RobotInstances())    y = Robot()    print(x.RobotInstances())    print(Robot.RobotInstances())        