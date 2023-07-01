""" class is creating for seeing lint issues"""
class A:
    def __init__(self):
        self.name=None

class B:
    pass

class C(B,A):
    pass
