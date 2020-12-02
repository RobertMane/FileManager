from utilities.node import Node

class DirectoriesTree:

    def __init__(self, roots=None):
        self._roots = list()

    @property
    def roots(self):
        return self._roots

    @roots.setter
    def roots(self, value):
        self._roots = value