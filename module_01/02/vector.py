import copy

class Vector:
    
    def __init__(self, *args):
        self.vector = []
        if len(args) == 1 and isinstance(args[0], int):
            self.vector = [float(i) for i in range(args[0])]
        elif len(args) == 2 and all(type(a) == int for a in args):
            self.vector = [float(i) for i in range(args[0], args[1])]
        else:
            for i in args[0]:
                if isinstance(i, list):
                    self.vector.append(i)
                else:
                    self.vector.append([i])
            pass
        self.shape = (len(self.vector), len(self.vector[0]))
        print(self.shape)

    def dot(self, v2):
        if not isinstance(v2, Vector):
            raise TypeError("Arg is no a Vector class")
        if self.shape != v2.shape:
            raise ValueError("Vectors not equal shape")
        resp = float(0)
        for i in range(len(self.vector)):
            for j in range(len(self.vector[i])):
                resp += self.vector[i][j] * v2.vector[i][j] 
        return resp

    def T(self):
        transposed = [([0.0] * self.shape[0]) for i in range(self.shape[1])]
        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                transposed[j][i] += self.vector[i][j]
        res_v = Vector(1)
        res_v.vector = transposed
        return res_v

    def __repr__(self):
        return str("Vector(" + str(self.vector) + ")")

    def __mul__(self, number):
        aux = copy.deepcopy(self)
        if aux.shape[0] == 1:
            for i in range(len(aux.vector[0])):
                aux.vector[0][i] *= number
        else:
            for i in range(len(aux.vector)):
                for j in range(len(aux.vector[i])):
                    aux.vector[i][j] *= number
        return aux

    def __truediv__(self, number):
        try:
            if number == 0:
                raise ZeroDivisionError("division by zero")
        except ZeroDivisionError as e:
            print(e.__class__.__name__ + ':', e)
            return
        aux = copy.deepcopy(self)
        if aux.shape[0] == 1:
            for i in range(len(aux.vector[0])):
                aux.vector[0][i] /= number
        else:
            for i in range(len(aux.vector)):
                for j in range(len(aux.vector[i])):
                    aux.vector[i][j] /= number
        return aux

    def __str__(self):
        return str(self.vector)


if __name__ == '__main__':
    a = Vector(2)
    b = Vector([1.0], [1.5], [2.0], [2.5])
    c = Vector([1.0, 1.5])
    d = Vector(15, 29)
    e = Vector([0.0, 1.0])
    """
    print(b.shape)
    print(b)
    print(c.shape)
    print(c)
    """
  # print(b.dot(a))
  # print(a.T())
  # print(e)
    print(a)
    print(b)
    print(c)
    print(d)
    print(e)
