<h1>0x06-python-classes</h1>

<h2>0.My first square</h2>
Write an empty class Square that defines a square:
<ul>
	<li>You are not allowed to import any module</li>
</ul>

<h2>1. Square with size</h2>
Write a class Square that defines a square by: (based on 0-square.py)
<ul>
	<li>Private instance attribute: size</li>
	<li>Instantiation with size (no type/value verification)</li>
	<li>You are not allowed to import any module</li>
</ul>

<h2>2. Size validation</h2>
Write a class Square that defines a square by: (based on 1-square.py)
<ul>
	<li>Private instance attribute: size</li>
	<li>Instantiation with optional size: def __init__(self, size=0):</li>
	<ul>
		<li>size must be an integer, otherwise raise a TypeError exception with the message size must be an integer</li>
		<li>if size is less than 0, raise a ValueError exception with the message size must be >= 0</li>
	</ul>
	<li>You are not allowed to import any module</li>
</ul>

<h2>3. Area of a square</h2>
Write a class Square that defines a square by: (based on 2-square.py)
<ul>
        <li>Private instance attribute: size</li>
        <li>Instantiation with optional size: def __init__(self, size=0):</li>
        <ul>
                <li>size must be an integer, otherwise raise a TypeError exception with the message size must be an integer</li>
                <li>if size is less than 0, raise a ValueError exception with the message size must be >= 0</li>
        </ul>
	<li>Public instance method: def area(self): that returns the current square area</li>
        <li>You are not allowed to import any module</li>
</ul>
