'''
Linked List implementation.
'''

class Node:
    def __init__(self, data_param, message_param):
        self.data = data_param # Commit hash
        self.message = message_param # Commit message
        self.next = None

    def __repr__(self):

        if self.next is None:
            next_data = "None"
        else:
            next_data = self.next.data

        return "NODE = data: " + self.data + ", next: " + next_data


class LinkedList:
    def __init__(self):
        self.head = None


    def __repr__(self):
        nodes = ["Head"]
        for node in self:
            nodes.append(node.data)
        nodes.append("None")
        return " --> ".join(nodes)


    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next


    def traverse(self):
        for node in self:
            print(node)


    def insert_first(self, node):
        node.next = self.head
        self.head = node

    
    def insert_last(self, node):
        if self.head is None:
            self.head = node
        else:
            for current_node in self:
                pass
            current_node.next = node


    def remove(self, node_data):
        if self.head is None:
            raise Exception("La lista está vacía")
            
        if self.head.data == node_data:
            self.head = self.head.next
            return
        
        previous_node = self.head
        for node in self:
            if node.data == node_data:
                previous_node.next = node.next
                return

            previous_node = node

        raise Exception("El nodo no existe en la lista linkeada")


    def insert_before(self, node_data, new_node):
        if self.head is None:
            raise Exception("La lista está vacía")

        if self.head.data == node_data:
            return self.insert_first(new_node)

        previous_node = self.head
        for node in self:
            if node.data == node_data:
                previous_node.next = new_node
                new_node.next = node
                return
            
            previous_node = node

        raise Exception("El nodo no existe en la lista linkeada")


    def insert_after(self, node_data, new_node):
        if self.head is None:
            raise Exception("La lista está vacía")

        for node in self:
            if node.data == node_data:
                new_node.next = node.next
                node.next = new_node
                return

        raise Exception("El nodo no existe en la lista linkeada")
        

    def reverse(self):
        if self.head is None:
            raise Exception("La lista está vacia")

        previous_node = None
        node = self.head

        while node is not None:
            next = node.next
            node.next = previous_node
            previous_node = node
            node = next

        self.head = previous_node
