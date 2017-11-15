class MyMath:
    def myAdd(num1, num2):
        """Add two numbers together (num1, num2)"""
        if isinstance(num1, str):
            try:
                num1 = float(num1)
            except ValueError:
                print('The first value needs to be a number.')
                return
        else:
            num1 = float(num1)

        if isinstance(num2, str):
            try:
                num2 = float(num2)
                return num1 + num2
            except ValueError:
                print('The second value needs to be a number.')
        else:
            num2 = float(num2)
            return num1 + num2

    def mySubtract(num1, num2):
        """Subtract num2 from num2"""
        if isinstance(num1, str):
            try:
                num1 = flaot(num1)
            except ValueError:
                print('The first value needs to be a number.')
                return
        else:
            num1 = float(num1)

        if isinstance(num2, str):
            try:
                num2 = float(num2)
                return num1 - num2
            except ValueError:
                print('The second value needs to be a number.')
        else:
            num2 = float(num2)
            return num1 - num2

    def myMultiply(num1, num2):
        """Multiply num1 by num2"""
        if isinstance(num1, str):
            try:
                num1 = float(num1)
            except ValueError:
                print('The first value needs to be a number.')
                return
        else:
            num1 = float(num1)

        if isinstance(num2, str):
            try:
                num2 = float(num2)
                return num1 * num2
            except ValueError:
                print('The second value needs to be a number,')
        else:
            num2 = float(num2)
            return num1 * num2

    def myDivide(num1, num2):
        """Divide num1 by num2"""
        if isinstance(num1, str):
            try:
                num1 = float(num1)
            except ValueError:
                print('This first value needs to be a number.')
                return
        else:
            num1 = float(num1)

        if isinstance(num2, str):
            try:
                num2 = float(num2)
                return num1 / num2
            except ValueError:
                print('The second value needs to be number.')
        else:
            num2 = float(num2)
            return num1 / num2
