def check_expression(expression):
    is_correct = check_beginning(expression)
    if is_correct:
        print(evaluate_expression(expression))
    else:
        print('NO')


def is_single_expression(expression):
    closing_brackets = {
        '(': ')',
        '[': ']',
        '{': '}'
    }
    leading_bracket = expression[0]
    opened_brackets = 1
    closed_brackets = 0
    i = 1
    while i < len(expression):
        symbol = expression[i]
        if symbol == leading_bracket:
            opened_brackets = opened_brackets + 1
        elif symbol == closing_brackets[leading_bracket]:
            closed_brackets = closed_brackets + 1
        if closed_brackets == opened_brackets and not i == len(expression) - 1:
            return False
        elif closed_brackets == opened_brackets and i == len(expression) - 1:
            return True
        i = i + 1
    return False


def check_beginning(expression):
    if expression[0] not in ['{', '[', '(']:
        return False
    elif expression[len(expression) - 1] not in ['}', ']', ')']:
        return False
    elif not is_single_expression(expression):
        return False
    elif expression[0] == '{':
        if expression[len(expression) - 1] == '}':
            return check_brackets(expression[1:len(expression) - 1], True)
        else:
            return False
    else:
        return check_brackets(expression, False)


def check_brackets(expression, in_outermost):
    i = 0
    while i < len(expression):
        symbol = expression[i]
        if symbol == '[':
            counter = i + 1
            while counter < len(expression):
                head = expression[counter]
                if head == ']':
                    i = counter + 1
                    break
                elif head == '(':
                    bracket_closed_index = check_inner_brackets(expression, counter)
                    if not bracket_closed_index:
                        return False
                    else:
                        counter = bracket_closed_index
                elif head in ['[', '{', '}', ')']:
                    return False
                counter = counter + 1
            continue
        elif symbol == '(':
            if in_outermost:
                return False
            bracket_closed_index = check_inner_brackets(expression, i)
            if not bracket_closed_index:
                return False
            else:
                i = bracket_closed_index
        elif symbol in ['{', '}']:
            return False
        i = i + 1
    return True


def check_inner_brackets(expression, starting_index):
    i = starting_index + 1
    while i < len(expression):
        symbol = expression[i]
        if symbol == ')':
            return i
        elif symbol in ['{', '[', '(', ']', '}']:
            return False
        i = i + 1
    return False


def evaluate_expression(expression):
    value = 0
    symbol = expression[0]
    if symbol == '{':
        value = outermost_bracket_evaluate(expression)
    elif symbol == '[':
        value = middle_bracket_evaluate(expression, 0)['value']
    elif symbol == '(':
        value = find_next_number(expression, 0)['value']
    return value


def outermost_bracket_evaluate(expression):
    value = 0
    i = 0
    while i < len(expression):
        symbol = expression[i]
        if symbol == '[':
            result = middle_bracket_evaluate(expression, i)
            value = value + 2 * result['value']
            i = result['closing_index']
            continue
        elif symbol == '(':
            result = find_next_number(expression, i)
            value = value + result['value']
            i = result['closing_index']
        else:
            result = find_next_number(expression, i)
            value = value + result['value']
            i = result['next_bracket_index']
            continue
        i = i + 1
    return value


def find_next_number(expression, starting_index):
    number = '0'
    i = starting_index + 1
    while i < len(expression):
        symbol = expression[i]
        if symbol in ['{', '[', '(', ')', ']', '}']:
            break
        else:
            number = number + symbol
            i = i + 1
    return {
        'next_bracket_index': i,
        'value': int(number)
    }


def middle_bracket_evaluate(expression, starting_index):
    value = 0
    closing_index = None
    i = starting_index
    while i < len(expression):
        symbol = expression[i]
        if symbol == '(':
            result = find_next_number(expression, i)
            value = value + 2 * result['value']
            i = result['next_bracket_index']
            continue
        elif symbol == ']':
            closing_index = i
            break
        else:
            find_next_number(expression, i)
            result = find_next_number(expression, i)
            value = value + result['value']
            i = result['next_bracket_index']
            continue
        i = i + 1

    return {
        'value': value,
        'closing_index': closing_index
    }
