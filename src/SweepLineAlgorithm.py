from AVLTree import *
from B_2_3Tree import *
from shapely.geometry import LineString
import time

class Point():
    
    def __init__(self, x, y, number = None, ptype = None, line = None):
        self.x = x
        self.y = y
        self.number = number
        self.ptype = ptype # 0 - start, 1 - end
        self.line = line

    def __lt__(self, point):
        if self.x < point.x:
            return True
        elif self.x == point.x:
            if self.y < point.y:
                return True
            elif self.y == point.y:
                if self.ptype < point.ptype:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    
    def __str__(self):
        return f'({self.x}, {self.y}), {self.number}, {self.ptype}'

class Line():

    def __init__(self, x1, y1, x2, y2, number):

        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.number = number

    def __str__(self):

        return f'({self.x1}, {self.y1}, {self.x2}, {self.y2}, {self.number})'

    def __lt__(self, line):
        
        if self.y1 < line.y1:
            return True
        elif self.y1 == line.y1:
            if self.number < line.number:
                return True
            else:
                return False    
        else:
            return False

    def split(self):

        return Point(self.x1, self.y1, self.number, 0, self), Point(self.x2, self.y2, self.number, 1, self)

def sweep_line(E, mode):

    E.sort()
    root = None

    if mode:
        tree = AVLTree()
        for elem in E:
            if elem.ptype == 0:
                root = tree.insert(root, elem.line)
                tmp = tree.next(root, tree.search(root, elem.line))
                current_line = elem.line
                line1 = LineString([(current_line.x1, current_line.y1), (current_line.x2, current_line.y2)])
                if tmp:
                    line2 = LineString([(tmp.value.x1, tmp.value.y1), (tmp.value.x2, tmp.value.y2)])
                    if line1.intersects(line2):
                        return f'Найдена пара пересекающихся отрезков: {current_line.number}, {tmp.value.number}'   

                tmp = tree.previous(tree.search(root, elem.line), root)

                if tmp:
                    line2 = LineString([(tmp.value.x1, tmp.value.y1), (tmp.value.x2, tmp.value.y2)])
                    if line1.intersects(line2):
                        return f'Найдена пара пересекающихся отрезков: {current_line.number}, {tmp.value.number}'   
            else:
                tmp1 = tree.next(root, tree.search(root, elem.line))
                tmp2 = tree.previous(tree.search(root, elem.line), root)
                if tmp1 and tmp2:
                    line1 = LineString([(tmp1.value.x1, tmp1.value.y1), (tmp1.value.x2, tmp1.value.y2)])
                    line2 = LineString([(tmp2.value.x1, tmp2.value.y1), (tmp2.value.x2, tmp2.value.y2)])
                    if line1.intersects(line2):
                        return f'Найдена пара пересекающихся отрезков: {tmp1.value.number}, {tmp2.value.number}' 
                root = tree.delete(root, elem.line)

        return 'Пересекающихся отрезков не найдено'
    else:
        tree = B_2_3Tree()
        for elem in E:
            if elem.ptype == 0:
                root = tree.insert(root, elem.line)
                el = tree.search(root, elem.line)
                tmp = tree.next(tree.search(root, elem.line), elem.line)
                current_line = elem.line
                line1 = LineString([(current_line.x1, current_line.y1), (current_line.x2, current_line.y2)])
                if tmp:
                    line2 = LineString([(tmp.x1, tmp.y1), (tmp.x2, tmp.y2)])
                    if line1.intersects(line2):
                        return f'Найдена пара пересекающихся отрезков: {current_line.number}, {tmp.number}'

                tmp = tree.previous(tree.search(root, elem.line), elem.line)

                if tmp:
                    line2 = LineString([(tmp.x1, tmp.y1), (tmp.x2, tmp.y2)])
                    if line1.intersects(line2):
                        return f'Найдена пара пересекающихся отрезков: {current_line.number}, {tmp.number}'
            else:
                tmp1 = tree.next(tree.search(root, elem.line), elem.line)
                tmp2 = tree.previous(tree.search(root, elem.line), elem.line)
                if tmp1 and tmp2:
                    line1 = LineString([(tmp1.x1, tmp1.y1), (tmp1.x2, tmp1.y2)])
                    line2 = LineString([(tmp2.x1, tmp2.y1), (tmp2.x2, tmp2.y2)])
                    if line1.intersects(line2):
                        return f'Найдена пара пересекающихся отрезков: {tmp1.number}, {tmp2.number}' 
                root = tree.delete(root, elem.line)

        return 'Пересекающихся отрезков не найдено'          