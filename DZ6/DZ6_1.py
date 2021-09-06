from time import sleep
# class TrafficLight:
#     __color = ['Red', 'Yellow', 'Green']
#
#     def running(self):
#         i = 0
#         while i != 3:
#             print(TrafficLight.__color[i])
#             if i == 0:
#                 sleep(7)
#             elif i == 1:
#                 sleep(2)
#             elif i == 2:
#                 sleep(4)
#             i += 1
class TrafficLight:
     colors = ('Red', 'Yellow', 'Green')
     time_color = (7, 2, 4)
     def __init__(self):
         self.__colors = 'Red'
     def running(self):
         while True:
             for i in self.colors:
                 self.__colors = i
                 print(self.__colors)
                 sleep(self.time_color[self.colors.index(self.__colors)])
a = TrafficLight()
a.running()
