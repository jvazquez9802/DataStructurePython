"""
Comentarios en bloque

"""
class LinkedList:
    def __init__(self):
        self.first = None

    def addAtEnd(self, node):
        if self.first == None:
            self.first = node
            return
        
        t = self.first

        while t.sig != None:
            t = t.sig

        t.sig = node
    def printList(self):
        s = ""
        t = self.first
        s+= str(t.value) + ", "
        while t.sig != None:
            t = t.sig
            s+= str(t.value) + ", "
        return s
