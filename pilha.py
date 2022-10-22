# Pilha

# Q1
class Pilha:

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


# Q2 pushWithClassLinkedList(e)


    def push(self, newData=None):
        if newData is None:
            return

        p1 = Pilha(self.data, self.next)

        self.data = newData
        if p1.data == None and p1.next == None:
            self.next = None
        else:
            self.next = p1

# Q3 popWithClassLinkedLis(e)
    def pop(self):
        if not self:
            return None

        poped = self.data

        if self.next is None:
            self.data = None
            self.next = None
        else:
            self.data = self.next.data

            self.next = self.next.next
        return poped
# Q4 peek elementar

    def peekLinkedList(self):
        peek = self.pop()
        self.push(peek)
        return peek


# Q5 isEmpty diverso


    def isEmpty(self):
        if self.data is None:
            return None

        n = self
        len = 0
        while n.next is not None:
            n = n.next
            len += 1
        if len == 0:
            return True
        else:
            return False

# Q5 isEmpty elementar
    def isEmptyElementar(self):
        n = self.pop()
        if n == None:
            return True
        else:
            self.push(n)
            return False


# Q6 lengh diverso


    def len(self):
        if self.data is None:
            return None

        n = self
        len = 0
        while n.next is not None:
            n = n.next
            len += 1
        return len

   # Q6 lengh elementar
    def lenElementar(self):
        aux = Pilha()
        len = 0
        n = self.pop()

        while n is not None:
            aux.push(n)
            n = self.pop(n)
            len += 1

        if len == 0:
            return 0
        else:
            e = aux.pop()
            while e is not None:
                self.push(e)
                return len


# Q7 retornar o último elemento diverso


    def last(self):
        if self.data is None:
            return None
        elif self.next.data is None:
            last = self.data
            return last
        else:
            n = self
            while n.next.next.data is not None:
                n = n.next
            last = n.next.data
            return last

# Q7 retornar o último elemento Elementar
    def lastElementar(self):
        aux = Pilha()

        n = self.pop()
        if n == None:
            return

        while n is not None:
            aux.push(n)
            last = n
            n = self.pop()

        e = aux.pop()

        while e is not None:
            self.push(e)

        return last


# Q8 getValueByIndex(i) diverso

    def getValueByIndex(self, i):
        if self.data is None:
            return
        n = self
        aux = 0
        while n.next is not None:
            if (aux == i):
                return n.data
            aux += 1
            n = n.next

   # Q8 getValueByIndex(i) elementar
    def getValueByIndexElementar(self, i):
        aux = Pilha()
        n = self.pop()
        index = 0

        while n is not None:
            if (index == i):
                value = n
            index += 1

            aux.push(n)
            n = self.pop()

        e = aux.pop()
        while e is not None:
            self.push(e)

        return value

# Q9 getIndexByValue diversa
    def getIndexByValue_D(self, NewData):

        if self.data is None:
            return
        n = self
        aux = 0
        while n.next is not None:
            if (aux == NewData):
                value = aux
            aux += 1
            n = n.next

        return value

# Q9 getIndexByValue Elementar
    def getIndexByValue_E(self, NewData):
        aux = Pilha()
        valores = []
        n = self.pop()
        index = 0
        variavel = true

        while n is not None and variavel is not False:
            if (index == NewData):
                value = n
                variavel = False

            index += 1
            aux.push(n)
            n = self.pop()

        e = aux.pop()
        while e is not None:
            self.push(e)

        return value


# Q10 getAllIndexByValue(e)  diversa

    def getAllIndexByValue_D(self, NewData):
        value = []
        if self.data is None:
            return
        n = self
        aux = 0
        while n.next is not None:
            if (aux == NewData):
                value.append(aux)
            aux += 1
            n = n.next

        return value


# Q10 getAllIndexByValue(e) Elementar

    def getAllIndexByValue_E(self, NewData):
        aux = Pilha()
        valores = []
        n = self.pop()
        index = 0

        while n is not None:
            if (n == NewData):
                valores.append(index)

            index += 1
            aux.push(n)
            n = self.pop()

        e = aux.pop()
        while e is not None:
            self.push(e)

        return valores

   # Q11 getValuesByIndexs diverso
    def getValuesByIndexs_D(self, array=[]):

        if self.data is None:
            return
        n = self
        aux = 0
        a = array.pop()

        while a is not None:
            while n.next is not None:
                if (aux == NewData):
                    value = aux
                aux += 1
                n = n.next
            aux2.append(a)

        f = aux2.pop()
        while f is not None:
            aux.append(f)

        return value
# Q11 (getValuesByIndexs elementar

    def getValuesByIndexs_E(self, array=[]):
        aux = []
        aux2 = []
        aux_Pilha = Pilha()
        n = self.pop()
        a = array.pop()

        while a is not None:
            while n is not None:
                if (a == n):
                    aux.append(a)

                aux2.append(a)
                aux_Pilha.push(n)
                n = self.pop()

        a = array.pop()

        aux2.append(a)

        e = aux_Pilha.pop()
        while e is not None:
            self.push(e)

        f = aux2.pop()
        while f is not None:
            aux.append(f)

        return aux

# Q12 getValuesBySlice diverso
    def getValueBySlice_D(self, i):
        if self.data is None:
            return
        n = self
        slice = 0
        while n is not None:
            while slice != NewData:
                valores.append(n)
                slice += 1

        n = n.next

# Q12 getValuesBySlice Elementar
    def getValueBySlice_E(self, NewData):
        valores = []
        n = self.pop()
        slice = 0

        while n is not None:
            while slice != NewData:
                valores.append(n)
                slice += 1

        e = aux.pop()
        while e is not None:
            self.push(e)

        return valores

# Q13 removeAll diversa
    def removeAll_D(self):
        self.data = None
        self.next = None

# Q13 removeAll elementar
    def removeAll_E(self):
        while self.pop() is not None:
            self.pop()

# Q14 removeByIndex(i) diversa
    def removeByIndex_D(self, NewData):
        if self.data is None:
            return
        n = self
        aux = 0
        while n is not None:
            if (aux == i):
                value = n
                aux2 = n
                value = None

            aux += 1
            n = n.next
        return aux2


# Q14 removeByIndex(i) elementar

    def removeByIndex_E(self, NewData):
        aux = Pilha()
        n = self.pop()
        index = 0

        while n is not None:
            aux.push(n)
            if (index == NewData):
                value = aux.pop()
            index += 1

        e = aux.pop()
        while e is not None:
            self.push(e)

        return value

# Q15 removeByValue(e)
    def removeByValue_D(self, NewData):
        if self.data is None:
            return
        n = self
        aux = 0
        var = true
        while n.next is not None & var is True:
            if (n == NewData):
                value = n
                aux2 = n
                value = None
                var = false
            aux += 1
            n = n.next

        while n.next.next is not None:
            n = n.next

        return aux2

# Q15 removeByValue(e)
    def removeByValue_E(self, NewData):
        aux = Pilha()
        n = self.pop()
        var = true

        while n is not None & var is True:
            aux.push(n)
            if (n == NewData):
                aux.pop()
                var = false

        e = aux.pop()
        while e is not None:
            self.push(e)

        return value

# Q16 remove AllByValue(e)
    def removeAllByValue_D(self, NewData):

        if self.data is None:
            return
        n = self
        aux = 0
        aux2 = []
        var = True

        while n.next is not None:
            if (n == NewData):
                value = n
                aux2.append(n)
                value = None
                var = False

            aux += 1
            n = n.next

        e = self.next
        while e.next is not None:
            if var == False:
                n = n.next

        return aux2

# Q16 remove AllByValue(e)

    def removeAllByValue_E(self, NewData):
        aux = Pilha()
        values = []
        n = self.pop()

        while n is not None:
            aux.push(n)
            if (n == NewData):
                value = aux.pop()
                values.append(value)

        e = aux.pop()
        while e is not None:
            self.push(e)

        return values

   # Questão 17

    def removeAllByIndexes_A(self, indexes):
        i = indexes.pop(0)
        while len(indexes) > 0:
            self.removeByIndex_A(i)
            i = indexes.pop(0)
        self.removeByIndex_A(i)

    def removeAllByIndexes_B(self, indexes):
        i = indexes.pop(0)
        while len(indexes) > 0:
            self.removeByIndex_B(i)
            i = indexes.pop(0)
        self.removeByIndex_B(i)

     # Questão 18

    def removeAllBySlice_A(self, inicial, final):
        i = inicial
        while i < final:
            self.removeByIndex_A(i)
            i += 1
        self.removeByIndex_A(i)

    def removeAllBySlice_B(self, inicial, final):
        i = inicial
        while i < final:
            self.removeByIndex_B(i)
            i += 1
        self.removeByIndex_B(i)

        # Questão 19

    def setValueInIndex_A(self, index, new):
        if index == 0:
            self.pop()
            self.push(new)
            return
        i = 0
        aux = Pilha()
        e = self.pop()
        aux.push(e)
        while i != index and e is not None:
            i += 1
            e = self.pop()
            if i != index:
                aux.push(e)
            else:
                aux.push(new)
        a = aux.pop()
        while a is not None:
            self.push(a)
            a = aux.pop()

    def setValueInIndex_B(self, index, new):
        if index == 0:
            self.data = new
            return
        i = 0
        aux = self.next
        while i != index:
            i += 1
            if i == index:
                aux.data = new
            else:
                aux = aux.next

    # Questão 20

    def setValuesInIndexes_C(self, indexes, elements):
        i = indexes.pop(0)
        e = elements.pop(0)
        while len(indexes) > 0:
            self.setValueInIndex_C(i, e)
            i = indexes.pop(0)
            e = elements.pop(0)
        self.setValueInIndex_C(i, e)

    def setValuesInIndexes_D(self, indexes, elements):
        i = indexes.pop(0)
        e = elements.pop(0)
        while len(indexes) > 0:
            self.setValueInIndex_D(i, e)
            i = indexes.pop(0)
            e = elements.pop(0)
        self.setValueInIndex_D(i, e)


# Q2 pushWithArray(e)
class Stack:  # considero que o final do array é o topo da pilha

    def __init__(self):
        self.stack = []

    def pushWithArray(self, value):
        self.stack.append(value)

# Q3 popWithArray(e)
    def popWithArray(self):
        if len(self.stack) == 0:
            return None

        else:
            poped = self.stack[-1]
            self.stack.remove(self.stack[-1])
            return poped


# Q4 peek diverso


    def peek(self):
        peek = self.stack[-1]
        return peek

   # Q4 peek elementar
    def peekElementar(self):
        return self.data

# Q5 isEmpty elementar
    def isEmptyElementar(self):
        arrayAux = []

        len = 0

        n = self.popWithArray()

        while n is not None:
            arrayAux.append(n)
            len += 1
            n = self.popWithArray()

        while arrayAux:
            aux = arrayAux.pop()
            arrayAux.append(aux)

        if len == 0:
            return True
        else:
            return False


# Q6 lengh elementar

    def lenghElementar(self):
        arrayAux = []
        arrayAux2 = []
        len = 0

        while self.data:
            aux = self.pop()
            arrayAux.append(aux)
            len += 1

        while arrayAux.data:
            aux2 = arrayAux.pop()
            arrayAux2.append(aux2)

        return len

# Q6 len diverso
    def len(self):
        return len(self.stack)

# Q7 retornar o último elemento elementar
    def last(self, value):
        arrayAux = []
        arrayAux2 = []

        while self.data:
            aux = self.remove()
            arrayAux.append(aux)

        last = arrayAux.remove()

        while arrayAux.data:
            aux2 = arrayAux.remove()
            arrayAux2.append(aux2)

        return last


# Q7 retornar o último elemento diverso

    def last(self):
        return self.stack[0]

# Q8 getValueByIndex(i) elementar

    def getValueByIndexElementar(self, i):
        arrayAux = []
        arrayAux2 = []
        auxi = 0

        while self.data:
            aux = self.remove()
            arrayAux.append(aux)

            if (aux == i):
                return n.data
            aux += 1

        while arrayAux.data:
            aux2 = arrayAux.remove()
            arrayAux2.append(aux2)

            if (aux == i):
                return n.data
            aux += 1

    # Q8 getValueByIndex(i) diverso

    def getValueByIndex(self, i):
        value = self.stack[-(i+1)]
        return value

    def toArray(self, array=[]):
        if self is None:
            return

        array.append(self.data)

        if self.next is not None and self.next.data is not None:
            self.next.toArray(array)

        return array
