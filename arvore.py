class Arvore:
    # Questão 21
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    # Questão 22
    def preOrder(self, array=[]):

        if self is None:
            return
        array.append(self.data)

        if self.left is not None:
            self.left.preOrder()

        if self.right is not None:
            self.right.preOrder()

        return array

    # Questão 23
    def inOrder(self, array=[]):
        if self is None:
            return
        if self.left is not None:
            self.left.inOrder()

        array.append(self.data)

        if self.right is not None:
            self.right.inOrder()
            # array.append(self.data)

        return array

    # Questão 24
    def postOrder(self, array=[]):
        if self is None:
            return

        if self.left is not None:
            self.left.postOrder()

        if self.right is not None:
            self.right.postOrder()

        array.append(self.data)

        return array

    # Questão 25
    def levelOrder(self, array=[]):
        q = []
        q.append(self)
        while len(q) != 0:
            self = q.pop(0)
            array.append(self.data)
            if self.left is not None:
                q.append(self.left)
            if self.right is not None:
                q.append(self.right)

        return array

    # Questão 26
    def height(self):
        if self is None:
            return -1
        return max(height(self.left), height(self.right)) + 1

    # Questão 27
    def qtd(self):
        qtd = 0
        if self is None:
            return
        if self.left is not None:
            qtd += 1
            self.left.qtd()

        if self.right is not None:
            qtd += 1
            self.right.qtd()

        return qtd

    # Questão 28
    def sheets(self, array=[]):
        if self is None:
            return

        if self.left is not None:
            self.left.sheets()

        if self.right is not None:
            self.right.sheets()

        if self.left is not None & self.right is not None:
            array.append(self.data)

        return array

    # Questão 29

    def complete(self):

        a = True
        if self is None:
            return False

        if self.left is None & self.right is not None:
            a = False

        if self.left is not None & self.right is None:
            a = False

        if self.left is not None & self.right is not None:
            a = True
            self.left.complete()
            self.right.complete()

        return a

    # Questão 30
    def binary(self):
        a = False
        if self is None:
            return
        if self.left is None & self.right is None:
            a = True

        if self.left is not None & self.right is not None:
            a = True
            self.left.binary()
            self.right.binary()

        return a
