class noda:
    def __init__(self, value):
        self.value = value
        self.link = None


class str_list:
    def __init__(self):
        self.head = None

    def push(self, storka):
        new_noda = noda(storka)
        if self.head == None:
            self.head = new_noda
        else:
            current = self.head
            while current.link != None:
                current = current.link
            current.link = new_noda

    def pop(self):
        if self.head == None:
            pass
        else:
            current = self.head
            prev = None
            while current.link != None:
                prev = current
                current = current.link
            prev.link = None

    def print(self):
        if self.head == None:
            print('список пуст')
        else:
            index = 0
            current = self.head
            while current.link != None:
                print(index, current.value)
                current = current.link
                index = index + 1
            print(index, current.value)

    def find(self, element_name):
        if self.head == None:
            return False
        else:
            current = self.head
            while current.link != None:
                if current.value == element_name:
                    return True
                current = current.link
            if current.value == element_name:
                return True
            else:
                return False
                
            




products = str_list()
products.push('хлеб')
products.push('хлеб')
products.push('масло')
products.push('сметана')

products.print()
print(products.find('сметана'))

products.pop()

products.print()
print(products.find('сметана'))

