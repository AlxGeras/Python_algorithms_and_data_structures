# 1. Написать программу, которая будет складывать, вычитать, умножать или делить два числа. Числа и знак операции
# вводятся пользователем. После выполнения вычисления программа не завершается, а запрашивает новые данные для
# вычислений. Завершение программы должно выполняться при вводе символа '0' в качестве знака операции. Если пользователь
# вводит неверный знак (не '0', '+', '-', '', '/'), программа должна сообщать об ошибке и снова запрашивать знак
# операции. Также она должна сообщать пользователю о невозможности деления на ноль, если он ввел его в качестве делителя.
#

step_message = ['первый операнд ', 'операция ', 'второй операнд ']
step = 0
while True:
    user_input = input(step_message[step])
    if user_input == '0' and step == 1:
        break
    if step == 0:
        try:
            first = float(user_input);
            step += 1
        except:
            print('введите вещественное число')

    elif step == 1:
        if user_input not in '/+-*' or user_input == '':
            print('неизвестная арифметическая операция')
        else:
            operator = user_input;
            step += 1
    else:
        if step == 2:
            try:
                second = float(user_input)
                if second == 0:
                    print('недопустимое значение аргумента: деление на ноль невозможно')
                else:
                    if operator == '+':
                        print(f'{first} + {second} = {first + second}')
                    if operator == '-':
                        print(f'{first} - {second} = {first - second}')
                    if operator == '*':
                        print(f'{first} * {second} = {first * second}')
                    if operator == '/':
                        print(f'{first} / {second} = {first / second}')
                    step = 0
            except:
                print('введите вещественное число')
