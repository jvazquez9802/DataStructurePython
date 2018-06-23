"""
Comentarios en bloque

"""
class LikedList:
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
