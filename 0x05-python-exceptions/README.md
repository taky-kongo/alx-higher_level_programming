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
