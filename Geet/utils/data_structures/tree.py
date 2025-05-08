'''
A simple tree structure for storing a directory snapshot.
'''


class Node():
    def __init__(self, name: str, content: list):
        self.name = name
        self.content = content


class Tree(): 
    def __init__(self, name: str):
        self.name = name
        self.message = None
        self.children = []

    def insert_child(self, object: any):
        self.children.append(object)

    def get_children(self):
        return self.children
