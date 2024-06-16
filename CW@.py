class StackInterpreter:
    def __init__(self):
        self.stack = [1]

    def run(self, code):
        i = 0
        while i < len(code):
            if code[i] == '@':
                self.copy_top()
            elif code[i] == '#':
                self.pop_top()
            elif code[i] == '+':
                self.add_one()
            elif code[i] == '-':
                self.subtract_one()
            elif code[i] == '{':
                loop_code, i = self.extract_loop(code, i)
                self.run_loop(loop_code)
            elif code[i] == '!':
                self.output_top()
            elif code[i] == '?':
                self.input_user()
            elif code[i] == ';':
                self.output_as_ascii()
            elif code[i] == '↷':
                self.move_to_bottom()
            i += 1

    def copy_top(self):
        if self.stack:
            self.stack.append(self.stack[-1])

    def pop_top(self):
        if self.stack:
            self.stack.pop()

    def add_one(self):
        if self.stack:
            self.stack[-1] += 1

    def subtract_one(self):
        if self.stack:
            self.stack[-1] -= 1

    def extract_loop(self, code, i):
        loop_code = ""
        bracket_count = 1
        i += 1  # Skip the opening '{'
        while bracket_count > 0 and i < len(code):
            if code[i] == '{':
                bracket_count += 1
            elif code[i] == '}':
                bracket_count -= 1
                if bracket_count == 0:
                    break
            loop_code += code[i]
            i += 1
        return loop_code, i

    def run_loop(self, loop_code):
        while self.stack and self.stack[-1] != 0:
            self.run(loop_code)

    def output_top(self):
        if self.stack:
            print(self.stack[-1])

    def input_user(self):
        user_input = input("Enter a number: ")
        try:
            num = int(user_input)
            self.stack.append(num)
        except ValueError:
            print("Invalid input. Expected an integer.")

    def output_as_ascii(self):
        if self.stack:
            ascii_value = self.stack[-1]
            print(chr(ascii_value))

    def move_to_bottom(self):
        if len(self.stack) > 1:
            top_item = self.stack.pop()
            self.stack.insert(0, top_item)

# Example usage
interpreter = StackInterpreter()
interpreter.run(" ") #code goes here. comment this out if you want the below
#interpreter.run(input(code)) #if you want the code to come from console input