# In this kata your task is to differentiate a mathematical expression given as a string in prefix notation. The result should be the derivative of the expression returned in prefix notation.

# To simplify things we will use a simple list format made up of parentesis and spaces.

# The expression format is (func arg1) or (op arg1 arg2) where op means operator, func means function and arg1, arg2 are aguments to the operator or function. For example (+ x 1) or (cos x)

# The expressions will always have balanced parentesis and with spaces between list items.

# Expression operators, functions and arguments will all be lowercase.

# Expressions are single variable expressions using x as the variable.

# Expressions can have nested arguments at any depth for example (+ (* 1 x) (* 2 (+ x 1)))

# Examples of prefix notation in this format:

# (+ x 2)        // prefix notation version of x+2

# (* (+ x 3) 5)  // same as 5 * (x + 3)

# (cos (+ x 1))  // same as cos(x+1)

# (^ x 2)        // same as x^2 meaning x raised to power of 2
# The operators and functions you are required to implement are + - * / ^ cos sin tan exp ln where ^ means raised to power of. exp is the exponential function (same as e^x) and ln is the natural logarithm (base e).

# Example of input values and their derivatives:

# (* 1 x) => 1

# (^ x 3) => (* 3 (^ x 2))

# (cos x) => (* -1 (sin x))
# In addition to returning the derivative your solution must also do some simplifications of the result but only what is specified below.

# The returned expression should not have unecessary 0 or 1 factors. For example it should not return (* 1 (+ x 1)) but simply the term (+ x 1) similarly it should not return (* 0 (+ x 1)) instead it should return just 0

# Results with two constant values such as for example (+ 2 2) should be evaluated and returned as a single value 4

# Any argument raised to the zero power should return 1 and if raised to 1 should return the same value or variable. For example (^ x 0) should return 1 and (^ x 1) should return x

# No simplifications are expected for functions like cos, sin, exp, ln... (but their arguments might require a simplification).

# Think recursively and build your answer according to the rules of derivation and sample test cases.

# If you need to diff any test expressions you can use Wolfram Alpha however remember we use prefix format in this kata.

# Best of luck !

def _tokenize(expr):
	return expr.replace("(", " ( ").replace(")", " ) ").split()


def _is_number(token):
	if token.startswith("-"):
		return token[1:].isdigit()
	return token.isdigit()


def _const(value):
	return ("const", value)


def _var():
	return ("var",)


def _is_const(node):
	return node[0] == "const"


def _const_value(node):
	return node[1]


def _is_zero(node):
	return _is_const(node) and _const_value(node) == 0


def _is_one(node):
	return _is_const(node) and _const_value(node) == 1


def _num_result(value):
	if isinstance(value, float) and value.is_integer():
		return int(value)
	return value


def _make_op(op, left, right):
	if op == "+":
		if _is_zero(left):
			return right
		if _is_zero(right):
			return left
		if _is_const(left) and _is_const(right):
			return _const(_const_value(left) + _const_value(right))
	elif op == "-":
		if _is_zero(right):
			return left
		if _is_const(left) and _is_const(right):
			return _const(_const_value(left) - _const_value(right))
	elif op == "*":
		if _is_zero(left) or _is_zero(right):
			return _const(0)
		if _is_one(left):
			return right
		if _is_one(right):
			return left
		# Keep products canonical: put constant factor on the left when possible.
		if _is_const(right) and not _is_const(left):
			left, right = right, left
		# Merge nested constant factors, e.g. (* -1 (* -37 f)) -> (* 37 f).
		if _is_const(left) and right[0] == "op" and right[1] == "*" and _is_const(right[2]):
			return _make_op("*", _const(_const_value(left) * _const_value(right[2])), right[3])
		if _is_const(left) and _is_const(right):
			return _const(_const_value(left) * _const_value(right))
	elif op == "/":
		if _is_zero(left):
			return _const(0)
		if _is_one(right):
			return left
		if _is_const(left) and _is_const(right):
			return _const(_num_result(_const_value(left) / _const_value(right)))
	elif op == "^":
		if _is_const(right):
			exponent = _const_value(right)
			if exponent == 0:
				return _const(1)
			if exponent == 1:
				return left
		if _is_const(left) and _is_const(right):
			return _const(_num_result(_const_value(left) ** _const_value(right)))

	return ("op", op, left, right)


def _make_func(name, arg):
	return ("func", name, arg)


def _parse(tokens):
	def parse_at(index):
		token = tokens[index]
		if token == "(":
			head = tokens[index + 1]
			if head in {"+", "-", "*", "/", "^"}:
				left, next_index = parse_at(index + 2)
				right, next_index = parse_at(next_index)
				return _make_op(head, left, right), next_index + 1

			arg, next_index = parse_at(index + 2)
			return _make_func(head, arg), next_index + 1

		if token == "x":
			return _var(), index + 1

		if _is_number(token):
			return _const(int(token)), index + 1

		raise ValueError("Invalid token: " + token)

	tree, _ = parse_at(0)
	return tree


def _derive(node):
	kind = node[0]

	if kind == "const":
		return _const(0)
	if kind == "var":
		return _const(1)
	if kind == "func":
		name, arg = node[1], node[2]
		d_arg = _derive(arg)
		if name == "sin":
			return _make_op("*", _make_func("cos", arg), d_arg)
		if name == "cos":
			return _make_op("*", _const(-1), _make_op("*", _make_func("sin", arg), d_arg))
		if name == "tan":
			return _make_op("*", _make_op("+", _const(1), _make_op("^", _make_func("tan", arg), _const(2))), d_arg)
		if name == "exp":
			return _make_op("*", _make_func("exp", arg), d_arg)
		if name == "ln":
			return _make_op("*", _make_op("/", _const(1), arg), d_arg)
		raise ValueError("Unknown function: " + name)

	op, left, right = node[1], node[2], node[3]
	d_left = _derive(left)
	d_right = _derive(right)

	if op == "+":
		return _make_op("+", d_left, d_right)
	if op == "-":
		return _make_op("-", d_left, d_right)
	if op == "*":
		return _make_op("+", _make_op("*", d_left, right), _make_op("*", left, d_right))
	if op == "/":
		top = _make_op("-", _make_op("*", d_left, right), _make_op("*", left, d_right))
		bottom = _make_op("^", right, _const(2))
		return _make_op("/", top, bottom)
	if op == "^":
		if _is_const(right):
			exponent = _const_value(right)
			reduced = _make_op("^", left, _const(exponent - 1))
			return _make_op("*", _make_op("*", _const(exponent), reduced), d_left)

		if _is_const(left):
			return _make_op("*", _make_op("*", node, _make_func("ln", left)), d_right)

		log_part = _make_op("*", d_right, _make_func("ln", left))
		ratio_part = _make_op("*", right, _make_op("/", d_left, left))
		return _make_op("*", node, _make_op("+", log_part, ratio_part))

	raise ValueError("Unknown operator: " + op)


def _to_prefix(node):
	kind = node[0]
	if kind == "const":
		value = node[1]
		if isinstance(value, float) and value.is_integer():
			value = int(value)
		return str(value)
	if kind == "var":
		return "x"
	if kind == "func":
		return "(" + node[1] + " " + _to_prefix(node[2]) + ")"
	return "(" + node[1] + " " + _to_prefix(node[2]) + " " + _to_prefix(node[3]) + ")"


def diff(expr):
	tree = _parse(_tokenize(expr))
	derivative = _derive(tree)
	return _to_prefix(derivative)


def differentiate(expr):
	return diff(expr)