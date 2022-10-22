#  Fila
# Q1
class Fila:

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

# Q2 insertWithClassLinkedList
    def insertWithClassLinkedList(self, newData):
        if newData is None:
            return
        f = Fila(newData, None)

        if self.data == None and self.next == None:
            self.data = newData
        else:
            n = self
            while n.next is not None:
                n = n.next
            n.next = f
# Q3 removeWithClassLinkedLis(e)

    def removeWithClassLinkedList(self, newData):
        poped = self.data

        if self.next == None:
            self.data == None
            self.next == None

        else:
            n = self
            while n.next is not None:
                n = n.next
                if n.data == newData:
                    poped = n.data
                    n.data == None
                    n.next == None
                    return poped


# Q 4 first Elementar
    # def firstElementar(self)
            #aux = Pilha()

            #n = self.pop()
            # if n == None:
        # return

            # while n is not None:
               # aux.push(n)
               #first = n
               #n = self.pop()

            #e = aux.pop()

            # while e is not None:
        # self.push(e)

            # return first


# Q6 lengh diverso

    def len(self):
        if self.data is None:
            return None
        n = self
        len = 1
        while n.next is not None:
            n = n.next
            len += 1
        return len

# Q6 lengh Elementar
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

# Q5 isEmpty diverso
    def isEmpty(self):
        if self.data is None:
            return None
        n = self
        len = 1
        while n.next is not None:
            n = n.next
            len += 1

        if len == 1:
            return True
        else:
            return False

    # Q5 isEmpty Elementar

    # Q7 retornar o último elemento - diverso
    def ultimo(self):
        if self.data is None:
            return None
        elif self.next.data is None:
            first = self.data
            return first
        else:
            n = self
            while n.next is not None:
                n = n.next
                first = n.next
                return first.data

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
        aux = Fila()
        valores = []
        n = self.removeWithClassLinkedList()
        index = 0
        variavel = true

        while n is not None and variavel is not False:
            if (index == NewData):
                value = n
                variavel = False

            index += 1
            aux.insertWithClassLinkedList(n)
            n = self.removeWithClassLinkedList()

        e = aux.removeWithClassLinkedList()
        while e is not None:
            self.insertWithClassLinkedList(e)

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
        aux = Fila()
        valores = []
        n = self.removeWithClassLinkedList()
        index = 0

        while n is not None:
            if (n == NewData):
                valores.append(index)

            index += 1
            aux.insertWithClassLinkedList(n)
            n = self.removeWithClassLinkedList()

        e = aux.removeWithClassLinkedList()
        while e is not None:
            self.insertWithClassLinkedList(e)

        return valores

   # Q11 getValuesByIndexs diverso
    def getValuesByIndexs_D(self, array=[]):

        if self.data is None:
            return
        n = self
        aux = 0
        a = array.pop()

        # while a is not None:
        # while n.next is not None:
        # if(aux == NewData):
        #value = aux
        #aux += 1
        #n = n.next
        # aux2.append(a)

        f = aux2.pop()
        while f is not None:
            aux.append(f)

        return value


# Q11 (getValuesByIndexs elementar

    def getValuesByIndexs_E(self, array=[]):
        aux = []
        aux2 = []
        aux_Pilha = Fila()
        n = self.removeWithClassLinkedList()
        a = array.removeWithClassLinkedList()

        while a is not None:
            while n is not None:
                if (a == n):
                    aux.append(a)

                aux2.append(a)
                aux_Pilha.insertWithClassLinkedList(n)
                n = self.removeWithClassLinkedList()

            a = array.removeWithClassLinkedList()

            aux2.append(a)

        e = aux_Pilha.removeWithClassLinkedList()
        while e is not None:
            self.insertWithClassLinkedList(e)

        f = aux2.removeWithClassLinkedList()
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
        n = self.removeWithClassLinkedList()
        slice = 0

        while n is not None:
            while slice != NewData:
                valores.append(n)
                slice += 1

        e = aux.removeWithClassLinkedList()
        while e is not None:
            self.insertWithClassLinkedList(e)

        return valores

# Q13 removeAll diversa
    def removeAll_D(self):
        self.data = None
        self.next = None

# Q13 removeAll elementar
    def removeAll_E(self):
        while self.removeWithClassLinkedList() is not None:
            self.removeWithClassLinkedList()

# Q14 removeByIndex(i) diversa

    def removeByIndex_A(self, NewData):
        if self.data is None:
            return
        n = self
        aux = 0
        while n is not None:
            if (aux == i):
                value = n
                aux2 = n
                value = None

        while n is not None:
            if (aux == i):
                value = n
                aux2 = n
                value = None

            aux += 1
            n = n.next
       # remove tem que apontar o index p outro
        while n is not None:
            if (aux == i-1):
                n = n.next

            aux += 1
            n = n.next

        return aux2
# Q14 removeByIndex(i) elementar

    def removeByIndex_B(self, NewData):
        aux = Fila()
        n = self.removeWithClassLinkedList()
        index = 0

        while n is not None:
            aux.insertWithClassLinkedList(n)
            if (index == NewData):
                value = aux.removeWithClassLinkedList()
            index += 1

        e = aux.removeWithClassLinkedList()
        while e is not None:
            self.insertWithClassLinkedList(e)

        while n is not None:
            if (aux == i-1):
                n = n.next

            aux += 1
            n = n.next

        return value

# Q15 removeByValue(e)
    def removeByValue_A(self, NewData):
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

        while n is not None:
            if (aux == i-1):
                n = n.next

            aux += 1
            n = n.next

        return aux2

# Q15 removeByValue(e)
    def removeByValue_B(self, NewData):
        aux = Fila()
        n = self.removeWithClassLinkedList()
        var = true

        while n is not None & var is True:
            aux.insertWithClassLinkedList(n)
            if (n == NewData):
                aux.removeWithClassLinkedList()
                var = false

        e = aux.removeWithClassLinkedList()
        while e is not None:
            self.insertWithClassLinkedList(e)

        while n is not None:
            if (aux == i-1):
                n = n.next

            aux += 1
            n = n.next

        return value

# Q16 remove AllByValue(e)
    def removeAllByValue_A(self, NewData):

        if self.data is None:
            return
        n = self
        aux = 0
        aux2 = []

        while n.next is not None:
            if (n == NewData):
                value = n
                aux2.append(n)
                value = None
                var = false

            aux += 1
            n = n.next

        while n is not None:
            if (aux == i-1):
                n = n.next

            aux += 1
            n = n.next

        return aux2

    # Questão 17

    def removeAllByIndexes_C(self, indexes):
        i = indexes.pop(0)
        while len(indexes) > 0:
            self.removeByIndex_C(i)
            i = indexes.pop(0)
        self.removeByIndex_C(i)

    def removeAllByIndexes_D(self, indexes):
        i = indexes.pop(0)
        while len(indexes) > 0:
            self.removeByIndex_D(i)
            i = indexes.pop(0)
        self.removeByIndex_D(i)

     # Questão 18

    def removeAllBySlice_C(self, inicial, final):
        i = inicial
        while i < final:
            self.removeByIndex_C(i)
            i += 1
        self.removeByIndex_C(i)

    def removeAllBySlice_D(self, inicial, final):
        i = inicial
        while i < final:
            self.removeByIndex_D(i)
            i += 1
        self.removeByIndex_D(i)

      # Questão 19

    def setValueInIndex_C(self, index, new):
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

    def setValueInIndex_D(self, index, new):
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


# Q2 insertWithArray(e)
class Fila2:
    def __init__(self):
        self.fila = []

    def insertWithArray(self, value):
        self.fila.append(value)

# Q3 removeWithArray(e)
    def removeWithArray(self, value):
        arrayAux = []
        arrayAux2 = []

        while self.data:
            aux = self.remove()
            arrayAux.append(aux)

        removed = arrayAux.remove()

        while arrayAux.data:
            aux2 = arrayAux.remove()
            arrayAux2.append(aux2)

        return removed

# Q4 first implementação diversa
    def first(self):
        if self.data is None:
            return
        first = self.fila[0]
        return first

# Q4 first implementação elementar
    def firstElementar(self, value):
        arrayAux = []
        arrayAux2 = []

        while self.data:
            aux = self.remove()
            arrayAux.append(aux)

        first = arrayAux.remove()

        while arrayAux.data:
            aux2 = arrayAux.remove()
            arrayAux2.append(aux2)

        return first


# Q5 isEmpty diverso


    def isEmpty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False

# Q5 isEmpty Elementar
    def isEmptyElementar(self):
        arrayAux = []
        arrayAux2 = []
        len = 0

        while self.data:
            aux = self.remove()
            arrayAux.append(aux)
            len += 1

        while arrayAux.data:
            aux2 = arrayAux.remove()
            arrayAux2.append(aux2)

        if len == 0:
            return True
        else:
            return False


# Q6 lengh diverso


    def len(self):
        return len(self.fila)

# Q6 lengh elementar
    def lenghElementar(self):
        arrayAux = []
        arrayAux2 = []
        len = 0

        while self.data:
            aux = self.remove()
            arrayAux.append(aux)
            len += 1

        while arrayAux.data:
            aux2 = arrayAux.remove()
            arrayAux2.append(aux2)

        return len

# Q7 retornar o último elemento diverso
    def last(self):
        return self.stack[-1]

# Q7  retornar o último elemento elementar
    def lastElementar(self):
        return self.data

# Q8 getValueByIndex(i) diverso
    def getValueByIndex(self, i):
        value = self.stack[i]
        return value

# Q8 getValueByIndex(i) elementar
    def getValueByIndex(self, i):
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
