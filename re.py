import re
'''
Regular expressions are a powerful tool for various kinds of string manipulation.
They are a domain specific language (DSL) that is present as a library in most modern programming languages, not just Python.
They are useful for two main tasks:
- verifying that strings match a pattern (for instance, that a string has the format of an email address),
- performing substitutions in a string 
'''

'''
We use a raw string, which is a normal string with an "r" in front of it. To avoid constantly having to escape literal metacharacters in our string
'''
pattern = r'or'


'''
After you've defined a regular expression, the re.match function can be used to determine whether it matches at the beginning of a string.
'''
if re.match(pattern, "orange"):
    print("Yes")

'''
The function re.search finds a match of a pattern anywhere in the string.
'''

if re.search(pattern, "door"):
    print("Yes")

match = re.search('fun', "defunct")
if match:
    '''
    These methods include group which returns the string matched, 
    start and end which return the start and ending positions of the first match, 
    and span which returns the start and end positions of the first match as a tuple.
    '''
    print(match.group())
    print(match.start())
    print(match.end())
    print(match.span())

'''
The function re.findall returns a list of all substrings that match a pattern.
'''
print(re.findall('pan', "panelistspan"))

'''
The function re.finditer does the same thing as re.findall, except it returns an iterator, rather than a list.
'''
for i in re.finditer('pan', "panelistspan"):
    print(i)


'Metacharacters'

r'gr.y' #any character apart from new line
r'gr..n'  #any two characters apart from new line
r'^gr.y$' #must begin with g, end with y and can have any character in between apart from a new line

'''
A character class is created by putting the characters it matches inside square brackets.
'''

pattern = r'[aeiou]' #contains any of these characters
if re.search(pattern, "grey"): 
   print("Yes")
r'[abc][def]' #will match any letter out of 'abc' then any letter out of 'def'. It is AND not OR

'Character classes can also have ranges'
r'[a-z]' #all lowercase letters
r'[G-P]' #letters between G and P in upper case
r'[0-9]' #numbers
r'[A-Z][A-Z][0-9]' #has LA7 pass the search!

'''
Place a ^ at the start of a character class to invert it. This causes it to match any character other than the ones included.
It basically NOT. So can be used to filter words with numbers or special characters
Other metacharacters such as $ and ., have no meaning within character classes.
'''
r'[^A-Z]' #gives all lower case characters

'''
The metacharacter * means "zero or more repetitions of the previous thing". 
It tries to match as many repetitions as possible. 

'''

pattern = r"cup(soon)*" 
if re.match(pattern, "cupsoonsoontake"): 
    print(True) #this will pass because spam in () can be repeated 0 or more times. 
                #It matches strings that start with "cup" and follow with zero or more "soon"s.

r'[a^]*'  #matches zero or more repetitions of "a" or "^"

'''
The metacharacter + is very similar to *, except it means "one or more repetitions", as opposed to "zero or more repetitions".

The metacharacter ? means "zero or one repetitions".

Another important metacharacter is |.
This means "or". usually has 2 or more chracters in a () sepearted by | in the pattern.

Curly braces can be used to represent the number of repetitions between two numbers.
The regex {x,y} means "between x and y repetitions of something".
Hence {0,1} is the same thing as ?.
If the first number is missing, it is taken to be zero. If the second number is missing, it is taken to be infinity.

For groups, () are used and []
'''
r'([^aeiou][aeiou][^aeiou])+' #matches one or more repetitions of a non-vowel, a vowel and a non-vowel

'''
The content of groups in a match can be accessed using the group function.
A call of group(0) or group() returns the whole match.
A call of group(n), where n is greater than 0, returns the nth group from the left.
The method groups() returns all groups up from 1.

Groups can be nested.

'''
pattern = r"a(bc)(de)(f(g)h)i"

match = re.match(pattern, "abcdefghijklmnop")
if match:
   print(match.group())
   print(match.group(0))
   print(match.group(1))
   print(match.group(2))
   print(match.groups())


'''
Two types of groups are named groups and non-capturing groups.
Named groups have the format (?P<name>...), where name is the name of the group, and ... is the content. They behave exactly the same as normal groups, except they can be accessed by group(name) in addition to its number.
Non-capturing groups have the format (?:...). They are not accessible by the group method, so they can be added to an existing regular expression without breaking the numbering.
'''

pattern = r"(?P<first>abc)(?:def)(ghi)"

match = re.match(pattern, "abcdefghi")
if match:
   print(match.group("first"))
   print(match.groups())

'''
Special sequences
One useful special sequence is a backslash and a number between 1 and 99, e.g., \1 or \17. This matches the expression of the group of that number.

Note, that "(.+) \1" is not the same as "(.+) (.+)", because \1 refers to the first group's subexpression, which is the matched expression itself, and not the regex pattern.
'''

pattern = r"(.+) \1"

match = re.match(pattern, "word word")
if match:
   print ("Match 1")

match = re.match(pattern, "?! ?!")
if match:
   print ("Match 2")    

match = re.match(pattern, "abc cde")
if match:
   print ("Match 3")

'''
More useful special sequences are \d, \s, and \w.
These match digits, whitespace, and word characters respectively.
In ASCII mode they are equivalent to [0-9], [ \t\n\r\f\v], and [a-zA-Z0-9_].
In Unicode mode they match certain other characters, as well. For instance, \w matches letters with accents.
Versions of these special sequences with upper case letters - \D, \S, and \W - mean the opposite to the lower-case versions. For instance, \D matches anything that isn't a digit.

r'(\D+\d)' matches one or more non-digits followed by a digit.

Additional special sequences are \A, \Z, and \b.
The sequences \A and \Z match the beginning and end of a string, respectively.
The sequence \b matches the empty string between \w and \W characters, or \w characters and the beginning or end of the string. 
Informally, it represents the boundary between words.
The sequence \B matches the empty string anywhere else.
'''

pattern = r"\b(cat)\b" #basically matches the word "cat" surrounded by word boundaries.


match = re.search(pattern, "The cat sat!")
if match:
   print ("Match 1")

match = re.search(pattern, "We s>cat<tered?")
if match:
   print ("Match 2")

match = re.search(pattern, "We scattered.")
if match:
   print ("Match 3")

'''
[\w\.-]+ matches one or more word character, dot or dash.
a period (.) in a pattern is preceeded by a \ to treat is a character
'''

pattern = r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+)"
text = "Please contact example@gmail.com for assistance"

match = re.search(pattern, text)
if match:
   print(match.group())


