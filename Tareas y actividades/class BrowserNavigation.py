class BrowserNavigation:
    def __init__(self):
        self.back_stack = []  
        self.forward_stack = []  
        self.current_page = None  

    def visit(self, url):
        if self.current_page:
            self.back_stack.append(self.current_page)
        self.current_page = url
        self.forward_stack.clear()
        self.show_status()

    def back(self):
        if self.back_stack:
            self.forward_stack.append(self.current_page)
            self.current_page = self.back_stack.pop()
        self.show_status()

    def forward(self):
        if self.forward_stack:
            self.back_stack.append(self.current_page)
            self.current_page = self.forward_stack.pop()
        self.show_status()

    def show_status(self):
        print(f"Página actual: {self.current_page}")
        print(f"Historial atrás: {self.back_stack}")
        print(f"Historial adelante: {self.forward_stack}\n")


browser = BrowserNavigation()
browser.visit("google.com")
browser.visit("github.com")
browser.visit("futbollibre.com")
browser.back()
browser.back()
browser.forward()
