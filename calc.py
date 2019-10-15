# EBNF GRAMMAR
# plus_expr :- minus_expr + plus_expr
# minus_expr :- div_expr - minus_expr
# div_expr :- mul_expr / div_expr
# term :- number | (plus_expr)

def skip_paren(start_pos,expr):
    """ skip a term with parens """
    current_pos = start_pos
    if expr[current_pos] == "(":
        while current_pos < len(expr):
            if expr[current_pos] == ")":
                return current_pos + 1
            
            current_pos += 1
        
        raise SyntaxError("Opening paren at char " + str(start_pos) + " but no closing")
    
    else:
        raise SyntaxError("Not a paren block")


def split_according_to_operator(operator,expr):
    """ split to two terms, at operator, ignoring parens"""
    i = 0
    while i < len(expr):
        if expr[i] == "(":
            i = skip_paren(i,expr)
        elif expr[i] == operator:
            break
        else:
            i += 1

    if i < len(expr) and expr[i] == operator:
        return [expr[0:i], expr[i+1:]]
    else:
        return [expr]


            



def term_expr(expr):
    """ A term expression is either a number or a parenthesized expression"""
    if expr == "":
        raise ValueError("Expected digit but got empty instead")

    if len(expr) > 2 and expr[0] == "(" and expr[-1] == ")":
        return plus_expr(expr[1:-1])
    
    num = int(expr)
    return num

    

def mul_expr(expr):
    """A multiplication expression is defined by the operator *"""
    if expr == "":
        return 0
    
    tokens = split_according_to_operator("*",expr)
    
    if len(tokens) == 1:
        return term_expr(tokens[0])
    elif len(tokens) == 2:
        return term_expr(tokens[0]) * mul_expr(tokens[1])


def div_expr(expr):
    """A multiplication expression is defined by the operator /"""
    if expr == "":
        return 0
    tokens = split_according_to_operator("/",expr)
    
    if len(tokens) == 1:
        return mul_expr(tokens[0])
    elif len(tokens) == 2:
        return mul_expr(tokens[0]) / div_expr(tokens[1])

def minus_expr(expr):
    """A multiplication expression is defined by the operator - """
    if expr == "":
    if expr == "":
        return 0
    
    tokens = split_according_to_operator("-",expr)
    
    if len(tokens) == 1:
        return div_expr(tokens[0])
    elif len(tokens) == 2:
        return div_expr(tokens[0]) - minus_expr(tokens[1])



def plus_expr(expr):
    """A multiplication expression is defined by the operator +"""
    if expr == "":
    if expr == "":
        return 0


    tokens = split_according_to_operator("+",expr)
    
    if len(tokens) == 1:
        return minus_expr(tokens[0])
    elif len(tokens) == 2:
        return minus_expr(tokens[0]) + plus_expr(tokens[1])



def eval_expr(expr):
    print(plus_expr(expr))


eval_expr("(1+1*35)/2")

