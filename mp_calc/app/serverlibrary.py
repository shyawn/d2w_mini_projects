

def mergesort(array, byfunc=None):
    if byfunc == None:
        byfunc = lambda item: item
    mergesort_recursive(array, 0, len(array) - 1, byfunc)

def mergesort_recursive(array, p, r, byfunc):
    if p < r:
        middle = (p + r) // 2
        mergesort_recursive(array, p, middle, byfunc)
        mergesort_recursive(array, middle + 1, r, byfunc)

        merge(array, p, middle, r, byfunc)
        
def merge(array, p, q, r, byfunc):
    left_array = array[p : q + 1]
    right_array = array[q + 1 : r + 1]
    left = right = 0
    dest = p
    
    while (left < len(left_array)) and (right < len(right_array)):
        if (byfunc(left_array[left]) <= byfunc(right_array[right])):
            array[dest] = left_array[left]
            left += 1
        else:
            array[dest] = right_array[right]
            right += 1
        dest += 1

    while left < len(left_array):
        array[dest] = left_array[left]
        left += 1
        dest += 1
    while right < len(right_array):
        array[dest] = right_array[right]
        right += 1
        dest += 1

class Stack:
    def __init__(self):
        self.__items = []
        
    def push(self, item):
        self.__items.append(item)

    def pop(self):
        if self.__items != []:
            return self.__items.pop()
        return None

    def peek(self):
        if self.__items != []:
            return self.__items[-1]
        return None

    @property
    def is_empty(self):
        return self.__items == []

    @property
    def size(self):
        return len(self.__items)

class EvaluateExpression:
    valid_char = '0123456789+-*/() '
    def __init__(self, string=""):
        self.string = string

    @property
    def expression(self):
        return self.string

    @expression.setter
    def expression(self, new_expr):
        for i in range(len(new_expr)):
            if new_expr[i] not in self.valid_char or new_expr == '':
                self.string = ''
                break
            else:
                self.string = new_expr
                continue

    def insert_space(self):
        new_string = ''
        for i in range(len(self.string)):
            if self.string[i] in '+-*/()':
                new_string += f' {self.string[i]} '
            else:
                new_string += self.string[i]
        return new_string

    def process_operator(self, operand_stack, operator_stack):
        operator = operator_stack.pop()
        right = operand_stack.pop()
        left = operand_stack.pop()
        if operator == '/':
            result = eval(f'{left} // {right}')
        else:
            result = eval(f'{left}{operator}{right}')
        operand_stack.push(result)

    def evaluate(self):
        operand_stack = Stack()
        operator_stack = Stack()
        expression = self.insert_space()
        tokens = expression.split()

        for i in range(len(tokens)):
            if tokens[i] in '+-':
                while not operator_stack.is_empty and operator_stack.peek() not in '()':
                    self.process_operator(operand_stack, operator_stack)
                operator_stack.push(tokens[i])
            elif tokens[i] in '*/':
                if operator_stack.peek() != None:
                    while operator_stack.peek() == '*' or operator_stack.peek() == '/':
                        self.process_operator(operand_stack, operator_stack)
                operator_stack.push(tokens[i])
            elif tokens[i] == '(':
                operator_stack.push(tokens[i])
            elif tokens[i] == ')':
                while operator_stack.peek() != '(':
                    self.process_operator(operand_stack, operator_stack)
                operator_stack.pop()
            else:
                operand_stack.push(tokens[i])

        while not operator_stack.is_empty:
            self.process_operator(operand_stack, operator_stack)
        return operand_stack.peek()


def get_smallest_three(challenge):
  records = challenge.records
  times = [r for r in records]
  mergesort(times, lambda x: x.elapsed_time)
  return times[:3]





