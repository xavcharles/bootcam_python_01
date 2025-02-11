class Vector:
    def __init__(self, values:list):
        self.values = values
        if len(self.values > 1):
            self.shape = (len(self.values), 1)
        else:
            self.shape = (1, len(self.values[0]))

def __add__(self, op):
    if (self.shape == op.shape):
        if (self.shape[0] == 1):
            for i in range(len(self.values[0])):
                self.values[0][i] += op.values[0][i]
            return Vector(self.values)
        else:
            for i in range(len(self.values)):
                self.values[i][0] += op.values[i][0]
            return Vector(self.values)
            
def __radd__(self, op):
    # add & radd : only vectors of the same shape.

def __sub__(self, op):
    if (self.shape == op.shape):
        if (self.shape[0] == 1):
            for i in range(len(self.values[0])):
                self.values[0][i] -= op.values[0][i]
            return Vector(self.values)
        else:
            for i in range(len(self.values)):
                self.values[i][0] -= op.values[i][0]
            return Vector(self.values)
        
def __rsub__(self, op):
    # sub & rsub: only vectors of the same shape.

def __truediv__(self, op):
    # truediv : only with scalars (to perform division of a Vector by a scalar).
    if isinstance(op, float):
        if (self.shape[0] == 1):
            for i in range(len(self.values[0])):
                self.values[0][i] /= op
            return Vector(self.values)
        else:
            for i in range(len(self.values)):
                self.values[i][0] /= op
            return Vector(self.values)
    return NotImplemented

def __rtruediv__(self, op):
    # rtruediv : raises an NotImplementedError with the message "Division of a scalar by a Vector is not defined here."
    raise NotImplemented("Division of a scalar by a Vector is not defined here.")

def __mul__(self, op):
    if isinstance(op, float):
        if (self.shape[0] == 1):
            for i in range(len(self.values[0])):
                self.values[0][i] *= op
            return Vector(self.values)
        else:
            for i in range(len(self.values)):
                self.values[i][0] *= op
            return Vector(self.values)
    return NotImplemented

def __rmul__(self, op):
    # mul & rmul: only scalars (to perform multiplication of a Vector by a scalar).

def __str__(self, op):

def __repr__(self, op):
    # must be identical, i.e we expect that print(vector) and vector within python interpretor to behave the same, see correspo