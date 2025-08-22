# Day 46: Create a DataFrame  

Create a **DataFrame** using pandas. You are going to create code to put the following into a Data Frame. You will use the information in the table  below. Basically, you are going to recreate this table using pandas. Use the information in the table to recreate the table.  

| year | Title        | genre  |
|------|--------------|--------|
| 2009 | Brothers     | Drama  |
| 2002 | Spider-Man   | Sci-fi |
| 2009 | WatchMen     | Drama  |
| 2010 | Inception    | Sci-fi |
| 2009 | Avatar       | Fantasy |

## Extra Challenge:  Website Data  with Pandas

Create a code that extracts data from a website. You will extract a table from the website. And from that table, you will extract columns about the data types in Python and their mutability. You will extract information from the following website:  
<https://en.wikipedia.org/wiki/Python_(programming_language)>  
The following table (next page) is what you will extract from the website.

| Type | Mutability | Description | Syntax examples |
| ---- | ---------- | ----------- | --------------- |
| bool | immutable  | Boolean value | True, False |
| bytearray | mutable  | Sequence of bytes | bytearray(b'Some ASCII')<br>bytearray(b"Some ASCII")<br> bytearray([119, 105, 107, 105]) |
| bytes | immutable  | Sequence of bytes | b'Some ASCII'<br> b"Some ASCII"<br> bytes([119, 105, 107, 105]) |
| complex | immutable  | Complex number with real and imaginary parts | 3+2.7j <br> 3 + 2.7j |
| dict | mutable  | Associative array (or dictionary) of key and value pairs; can contain mixed types (keys and values); keys must be a hashable type | {'key1': 1.0, 3: False}<br> {} |
| types.EllipsisType | immutable  | An ellipsis placeholder to be used as an index in NumPy arrays | ... <br> Ellipsis |
| float | immutable  | Double-precision floating-point number. The precision is machine-dependent, but in practice it is generally implemented as a 64-bit IEEE 754 number with 53 bits of precision.[103] | 1.33333 |
| frozenset | immutable  | Unordered set, contains no duplicates; can contain mixed types, if hashable | frozenset([4.0, 'string', True]) |
| int | immutable  | Integer of unlimited magnitude[104] | 42 |
| list | mutable  | List, can contain mixed types | [4.0, 'string', True] <br> [] |
| types.NoneType | immutable  | An object representing the absence of a value, often called null in other languages | None |
| types.NotImplementedType | immutable  | A placeholder that can be returned from overloaded operators to indicate unsupported operand types. | NotImplemented |
| range | immutable  | An immutable sequence of numbers, commonly used for iterating a specific number of times in for loops[105] | range(−1, 10) <br> range(10, −5, −2) |
| set | mutable  | Unordered set, contains no duplicates; can contain mixed types, if hashable | {4.0, 'string', True} <br> set() |
| str | immutable  | A character string: sequence of Unicode codepoints | 'Wikipedia' <br> "Wikipedia" <br>"""Spanning <br> multiple <br> lines""" |
| tuple | immutable  | Tuple, can contain mixed types | (4.0, 'string', True) <br> ('single element',) <br> () |

Once  you  extract  this  table,  you  will  write  a  code  that  will
extract  the  data  types  and  their  mutability  (Two  columns).
