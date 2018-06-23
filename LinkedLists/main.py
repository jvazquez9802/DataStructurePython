from Node import Node
from LinkedList import LinkedList

if __name__ == '__main__':
    print("Hola buei")

    ll = LinkedList() #Crea un objeto

    ll.addAtEnd(Node(4))
    ll.addAtEnd(Node(2))
    ll.addAtEnd(Node(6))
    ll.addAtEnd(Node(98))
    ll.addAtEnd(Node(124))
    ll.addAtEnd(Node(666))

    print(ll.printList())