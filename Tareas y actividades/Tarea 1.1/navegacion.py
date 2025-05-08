import sys

class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop() if self.items else None
    
    def peek(self):
        return self.items[-1] if self.items else None
    
    def is_empty(self):
        return len(self.items) == 0
    
    def __repr__(self):
        return str(self.items)

class BrowserNavigation:
    def __init__(self):
        self.back_stack = Stack()  # Pila para el historial hacia atrás
        self.forward_stack = Stack()  # Pila para el historial hacia adelante
        self.current_page = None  # Página actual

    def visit(self, url):
        if self.current_page:
            self.back_stack.push(self.current_page)
        self.current_page = url
        self.forward_stack = Stack()  # Reiniciar pila adelante
        self.show_status()

    def back(self):
        if not self.back_stack.is_empty():
            self.forward_stack.push(self.current_page)
            self.current_page = self.back_stack.pop()
        self.show_status()

    def forward(self):
        if not self.forward_stack.is_empty():
            self.back_stack.push(self.current_page)
            self.current_page = self.forward_stack.pop()
        self.show_status()

    def show_status(self):
        print(f"\nPágina actual: {self.current_page}")
        print(f"Historial atrás: {self.back_stack}")
        print(f"Historial adelante: {self.forward_stack}\n")

    def interactive_mode(self):
        while True:
            command = input("Ingrese un comando (visit [url] / back / forward / exit): ")
            if command.startswith("visit "):
                self.visit(command.split(" ", 1)[1])
            elif command == "back":
                self.back()
            elif command == "forward":
                self.forward()
            elif command == "exit":
                print("Saliendo del navegador...")
                break
            else:
                print("Comando no reconocido.")

# Ejemplo de uso
if __name__ == "__main__":
    browser = BrowserNavigation()
    browser.interactive_mode()
