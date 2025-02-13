class Vector:
    def __init__(self, values):
        if (isinstance(values, list)):
            if len(values) > 1:
                if not (all(isinstance(sublist, list) for sublist in values) and all(isinstance(val, float) for sublist in values for val in sublist)):
                    raise TypeError("This is either not a list of lists or some of the lists have a non-float element")
                self.values = values
                self.shape = (len(self.values), 1)
            elif (len(values) == 1):
                if not (isinstance(values[0], list) and all(isinstance(val, float) for val in values[0])):
                    raise TypeError("This is either not a list of a list or not all elements of the list of a list are floats")
                self.values = values
                self.shape = (1, len(self.values[0]))
        elif (isinstance(values, int)):
            for i in range(values):
                self.values.append([float(i)])
        elif (isinstance(values, range)):
            if (values.start > values[-1]):
                raise ValueError("range values needs to be crescent")
            for i in values:
                self.values.append([float(i)])

    def dot(self, op):
        if not (isinstance(op, Vector) and self.shape == op.shape):
            raise TypeError("can only do dot product between two vectors, that have the same shape")
        res = 0
        for i in range(len(self.values)):
            for j in range(len(self.values[i])):
                res += self.values[i][j] * op.values[i][j]
        return res

    def T(self):
        lst = [[]]
        if self.shape[0] < self.shape[1]:
            lst = [[self.values[0][i]] for i in range(len(self.values[0]))]
            # for i in range(len(self.values[0])):
                # lst.append([self.values[0][i]])
        else:
            lst = [[self.values[i][0] for i in range(len(self.values))]]
            # lst[0] = []
            # for i in range(len(self.values)):
            #     lst[0] += self.values[i][0]
        return Vector(lst)

    def __add__(self, op):
        if (self.shape == op.shape):
            # new_values = [[]]
            if (self.shape[0] == 1):
                new_values = [[self.values[0][i] - op.values[0][i] for i in range(len(self.values[0]))]]
                # for i in range(len(self.values[0])):
                #     new_values[0][i] = self.values[0][i] + op.values[0][i]
            else:
                new_values = [[self.values[i][0] + op.values[i][0]] for i in range(len(self.values))]
                # for i in range(len(self.values)):
                #     new_values[i][0] = self.values[i][0] + op.values[i][0]
            return Vector(new_values)
                
    def __radd__(self, op):
        # add & radd : only vectors of the same shape.
        if (self.shape == op.shape):
            # new_values = [[]]
            if (self.shape[0] == 1):
                new_values = [[op.values[0][i] + self.values[0][i] for i in range(len(self.values[0]))]]
                # for i in range(len(self.values[0])):
                #     new_values[0][i] = op.values[0][i] + self.values[0][i]
            else:
                new_values = [[op.values[i][0] + self.values[i][0]] for i in range(len(self.values))]
                # for i in range(len(self.values)):
                #     new_values[i][0] = op.values[i][0] + self.values[i][0]
            return Vector(new_values)

    def __sub__(self, op):
        if (self.shape == op.shape):
            # new_values = [[]]
            if (self.shape[0] == 1):
                new_values = [[self.values[0][i] - op.values[0][i] for i in range(len(self.values[0]))]]
                # for i in range(len(self.values[0])):
                #     new_values[0][i] = self.values[0][i] - op.values[0][i]
            else:
                new_values = [[self.values[i][0] - op.values[i][0]] for i in range(len(self.values))]
                # for i in range(len(self.values)):
                #     new_values[i][0] = self.values[i][0] - op.values[i][0]
            return Vector(new_values)
            
    def __rsub__(self, op):
        # sub & rsub: only vectors of the same shape.
        if (self.shape == op.shape):
            # new_values = [[]]
            if (self.shape[0] == 1):
                new_values = [[op.values[0][i] - self.values[0][i] for i in range(len(self.values[0]))]]
                # for i in range(len(self.values[0])):
                #     new_values[0][i] = op.values[0][i] - self.values[0][i]
            else:
                new_values = [[op.values[i][0] - self.values[i][0]] for i in range(len(self.values))]
                # for i in range(len(self.values)):
                #     new_values[i][0] = op.values[i][0] - self.values[i][0]
            return Vector(new_values)

    def __truediv__(self, op):
        # truediv : only with scalars (to perform division of a Vector by a scalar).
        if (op == 0):
            print("ZeroDivisionError: division by zero")
            return
        if isinstance(op, (int, float)):
            # new_values = [[]]
            if (self.shape[0] == 1):
                new_values = [[val / op for val in self.values[0]]]
                # for i in range(len(self.values[0])):
                #     new_values[0][i] = self.values[0][i] / op
            else:
                new_values = [[self.values[i][0] / op] for i in range(len(self.values))]
                # for i in range(len(self.values)):
                #     new_values[i][0] = self.values[i][0] / op
            return Vector(new_values)
        return NotImplementedError

    def __rtruediv__(self, op):
        # rtruediv : raises an NotImplementedError with the message "Division of a scalar by a Vector is not defined here."
        raise NotImplementedError("Division of a scalar by a Vector is not defined here.")

    def __mul__(self, op):
        if isinstance(op, (int, float)):
            # new_values = [[]]
            if (self.shape[0] == 1):
                # for i in range(len(self.values[0])):
                    # new_values[0][i] = self.values[0][i] * op
                new_values = [[val * op for val in self.values[0]]]
            else:
                # for i in range(len(self.values)):
                #     new_values[i][0] = self.values[i][0] * op
                new_values = [[self.values[i][0] * op] for i in range(len(self.values))]
            return Vector(new_values)
        return NotImplemented

    def __rmul__(self, op):
        if isinstance(op, (int, float)):
            # new_values = [[]]
            if (self.shape[0] == 1):
                # for i in range(len(self.values[0])):
                    # new_values[0][i] = self.values[0][i] * op
                new_values = [[val * op for val in self.values[0]]]
            else:
                # for i in range(len(self.values)):
                #     new_values[i][0] = self.values[i][0] * op
                new_values = [[self.values[i][0] * op] for i in range(len(self.values))]
            return Vector(new_values)
        return NotImplemented

    def __str__(self):
        return (f"{self.values}")

    def __repr__(self):
        # must be identical, i.e we expect that print(vector) and vector within python interpretor to behave the same, see correspo
        return (f"{self.values}")