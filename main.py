from math import sqrt
class Tohcka:
    x = 0
    y = 0
    def __init__(self):
        print("Введите координаты точки")
        self.x = float(input("Введите координату оси x: "))
        self.y = float(input("Введите координату оси y: "))
#Тут я сделал класс точки для того чтобы в него вводить данные координат и затем уже их использовать в фигурах.
    def dima(self):
        print("Точка координатами:({0};{1})".format(self.x, self.y))# Эта шняга сделана для нормального вывода в принте.
    def DISTANT(self, b):
        return sqrt((b.y - self.y) ** 2 + (b.x - self.x) ** 2)# Формула стороны, специально сделал в классе чтобы не делать по кучу строчек(как показанно далее)
class Treygolnick:
    def __init__(self):
        print("Введите треугольник с тремя точками.")
        self.k = Tohcka()#
        self.j = Tohcka()# А это друзья мои точкии мы их сюда пихнули благодаря классу Tohcka.
        self.b = Tohcka()#

    def dima(self):
        t.k.dima()
        print("Координаты вершин треугольника:({0};{1}), ({2},{3}), ({4},{5})".format(self.k.x,self.k.y,self.j.x,self.j.y,self.b.x,self.b.y))
        
print("Работа с геометрическими фигурами")
figura = int(input("Введите Фигуру с которой хотите работать: 1.Треугольник, 2.Окружность, 3.Прямоугольник. ? "))
if figura == 1:#Вот эта страшная вещь сверху, сделанна для грамотного принта(можно сделать лучше).
    t = Treygolnick()
    # По идее можно сделать так как написанно снизу: тогда можно обойтись без формулы в классе.(но это не практично).
    #ab = sqrt((t.k.y - t.j.y)**2 + (t.k.x - t.j.x)**2)
    #ac = sqrt((t.k.x - t.b.x)**2 + (t.k.y - t.b.y)**2)
    #cb = sqrt((t.b.y - t.j.y)**2 + (t.b.x - t.j.x)**2)
    ab = t.k.DISTANT(t.j)
    ac = t.k.DISTANT(t.b)# Тут я вызываю ту самую формулу из класса и с помощью нее вычисляю.
    cb = t.j.DISTANT(t.b)
    p = (ab + ac + cb)
    px = p/2
    s = sqrt(px*(px-ab)*(px-ac)*(px-cb))#Формула площади.
    t.dima()
    print('Площадь: ', s, 'Периметр: ', p)
else:
    print("Вы ввели не тот символ, попробуйте еще раз")





