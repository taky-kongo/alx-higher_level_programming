<h2>0x05-python-exceptions</h2>

<h3>0. Safe list printing</h3>
Write a function that prints x elements of a list.
<ul>
	<li>Prototype: def safe_print_list(my_list=[], x=0):</li>
	<li>my_list can contain any type (integer, string, etc.)</li>
	<li>All elements must be printed on the same line followed by a new line.</li>
	<li>x represents the number of elements to print</li>
	<li>x can be bigger than the length of my_list</li>
	<li>Returns the real number of elements printed</li>
	<li>You have to use try: / except:</li>
	<li>You are not allowed to import any module</li>
	<li>You are not allowed to use len()</li>
</ul>

<h3>1. Safe printing of an integers list</h3>
Write a function that prints an integer with "{:d}".format().
<ul>
	<li>Prototype: def safe_print_integer(value):</li>
	<li>value can be any type (integer, string, etc.)</li>
	<li>The integer should be printed followed by a new line</li>
	<li>Returns True if value has been correctly printed (it means the value is an integer)</li>
	<li>Otherwise, returns False</li>
	<li>You have to use try: / except:</li>
	<li>You have to use "{:d}".format() to print as integer</li>
	<li>You are not allowed to import any module</li>
	<li>You are not allowed to use type()</li>
</ul>

<h3>2. Print and count integers</h3>
Write a function that prints the first x elements of a list and only integers.
<ul>
	<li>Prototype: def safe_print_list_integers(my_list=[], x=0):</li>
	<li>my_list can contain any type (integer, string, etc.)</li>
	<li>All integers have to be printed on the same line followed by a new line - other type of value in the list must be skipped (in silence).</li>
	<li>x represents the number of elements to access in my_list</li>
	<li>x can be bigger than the length of my_list - if it’s the case, an exception is expected to occur</li>
	<li>Returns the real number of integers printed</li>
	<li>You have to use try: / except:</li>
	<li>You have to use "{:d}".format() to print an integer</li>
	<li>You are not allowed to import any module</li>
	<li>You are not allowed to use len()</li>
</ul>

<h3>3. Integers division with debug</h3>
Write a function that divides 2 integers and prints the result.
<ul>
	<li>Prototype: def safe_print_division(a, b):</li>
	<li>You can assume that a and b are integers</li>
	<li>The result of the division should print on the finally: section preceded by Inside result:</li>
	<li>Returns the value of the division, otherwise: None</li>
	<li>You have to use try: / except: / finally:</li>
	<li>You have to use "{}".format() to print the result</li>
	<li>You are not allowed to import any module</li>
</ul>

<h3>4. Divide a list</h3>
Write a function that divides element by element 2 lists.
<ul>
	<li>Prototype: def list_division(my_list_1, my_list_2, list_length):</li>
	<li>my_list_1 and my_list_2 can contain any type (integer, string, etc.)</li>
	<li>list_length can be bigger than the length of both lists</li>
	<li>Returns a new list (length = list_length) with all divisions</li>
	<li>If 2 elements can’t be divided, the division result should be equal to 0</li>
	<li>If an element is not an integer or float:</li>
	<ul>
		<li>print: wrong type</li>
	</ul>
	<li>If the division can’t be done (/0):</li>
	<ul>
		<li>print: division by 0</li>
	</ul>
	<li>If my_list_1 or my_list_2 is too short</li>
	<ul>
		<li>print: out of range</li>
	</ul>
	<li>You have to use try: / except: / finally:</li>
	<li>You are not allowed to import any module</li>
</ul>

<h3>5. Raise exception</h3>
Write a function that raises a type exception.
<ul>
	<li>Prototype: def raise_exception():</li>
	<li>You are not allowed to import any module</li>
</ul>

<h3>6. Raise a message</h3>
Write a function that raises a name exception with a message.
<ul>
	<li>Prototype: def raise_exception_msg(message=""):</li>
	<li>You are not allowed to import any module</li>
</ul>
