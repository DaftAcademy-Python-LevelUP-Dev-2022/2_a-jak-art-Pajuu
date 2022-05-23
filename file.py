def greeter(func):
	def inner(*args):
		greeting = "Aloha " + func(*args)
		return greeting.title()
	return inner


def sums_of_str_elements_are_equal(func):
	def sum_of_numbers(n):
		sum_of_n = 0
		negative = False
		for number in n:
			if number == "-":
				negative = True
			else:
				sum_of_n += int(number)
		if negative:
			sum_of_n *= -1
		return sum_of_n

	def inner(*args):
		value = func(*args)
		sliced_string = value.split()
		num1 = sum_of_numbers(sliced_string[0])
		num2 = sum_of_numbers(sliced_string[1])
		if num1 == num2:
			return f"{num1} == {num2}"
		else:
			return f"{num1} != {num2}"
	return inner


def format_output(*keys):
	def real_decorator(func):
		def inner(*args):
			dict_of_func = func(*args)
			dict_of_decorator = {}
			for key in keys:
				if "__" in key:
					dict_of_decorator[key] = ""
					sliced_keys = key.split("__")
					for sliced_key in sliced_keys:
						if sliced_key in dict_of_func:
							if dict_of_func[sliced_key] == "":
								dict_of_decorator[key] = "Empty value"
								break
							else:
								dict_of_decorator[key] += dict_of_func[sliced_key] + " "
						else:
							raise ValueError
					if dict_of_decorator[key] != "Empty value":
						dict_of_decorator[key] = dict_of_decorator[key][:-1]
				else:
					if key not in dict_of_func:
						raise ValueError
					if dict_of_func[key] == "":
						dict_of_decorator[key] = "Empty value"
					else:
						dict_of_decorator[key] = dict_of_func[key]
			return dict_of_decorator
		return inner
	return real_decorator


def add_method_to_instance(class_name):
	def inner(func):
		def inner2(*args):
			return func()
		setattr(class_name, func.__name__, inner2)
		return inner2
	return inner
