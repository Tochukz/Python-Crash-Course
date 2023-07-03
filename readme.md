# Python Crash Course (2nd Edition) (2019)
__By Eric Matthes__  

## Part 1: Basics
### Chapter 1: Getting Started  
__Python interactive shell__  
To start an interactive REPL session with python, enter the command `python` in you terminal window.
```
$ python
>>> print("Hello world")
>>> quit()
```

__Python interpreter__  
To run your python code
```
$ python hello_world.py
```

### Chapter 2: Variables and Simple Data Types
__The Zen of Python__  
The Python community’s philosophy is contained in _“The Zen of Python”_ by Tim Peters.  
To read it, enter `import this` into a python terminal
```
$ python
>>> import this
```

### Chapter 3: Introducing Lists

### Chapter 4: Working with Lists
__Tuples__    
Python refers to values that cannot change as immutable, and an _immutable_ list is called a _tuple_.  
Tuples are like list, but you define them using parentheses instead of square brackets.
```
dimension=(200,50)
```
If you want to define a tuple with one element, you need to include a trailing comma:
```
my_tuple = (3,)
```

__Styling your code__  
When someone wants to make a change to the Python language, they write
a _Python Enhancement Proposal_ (PEP). One of the oldest PEPs is PEP 8, which instructs Python programmers on how to style their code.  
See [PEP-8](https://peps.python.org/pep-0008/) to learn more.  

### Chapter 5: If Statements  

### Chapter 6: Dictionaries  
#### Sets
A set is a collection in which each item must be unique. Unlike lists and dictionaries, sets do not retain items in any specific order.  

### Chapter 7: User Input and while Loops

### Chapter 8: Functions
#### Docstring
A _docstring_ is a comment which describes what a function does.  Docstrings are enclosed in triple quotes, which Python looks for when it generates documentation for the functions in your programs.
```
def my_function():
   """This function does something"""
   print("Hello function!")
```

#### Passing Arguments  
You can pass arguments to your functions in a number of ways.  
You can use:
1. _positional arguments_, which need to be in the same order the parameters were written;
2. _keyword arguments_, where each argument consists of a variable name and a value; and lists and dictionaries of values.

#### Styling functions
1. Use descriptive name with lower letters and underscores.
2. Same rule in 1 is applicable to module names as well.
3. Write comment immediately after the function definition and use the _docstring_ format.
4. If you specify a default value for a parameter, no spaces should be used on either side of the equal sign.
5. Same convention in 4 is applicable for keyword arguments in function call.
6. PEP 8 recommends that you limit lines of code to 79 characters so every line is visible in a reasonably sized editor window.
7. If a set of parameters causes a function’s definition to
be longer than 79 characters, press enter after the opening parenthesis on the definition line. On the next line, press tab twice to separate the list of arguments from the body of the function, which will only be indented one level.
8. If your program or module has more than one function, you can separate each by two blank lines.  
9. All import statements should be written at the beginning of a file. The only exception is if you use comments at the beginning of your file to describe the overall program.


### Github Tips  
__To sync a forked repository's master branch with the latest changes from the parent repository__  
1. Add the parent repository as an upstream remote.  
In your local repository (the forked repository), add the parent repository as an upstream remote:
```
$ git remote add upstream https://github.com/Tochukz/Python-Crash-Course.git
```
2. Fetch the latest changes.  
Fetch the latest changes from the upstream remote:
```
$ git fetch upstream
```
3. Merge the upstream changes.  
Switch to your forked repository's master branch and merge the upstream changes into your local master branch:
```
$ git checkout master
$ git merge upstream/master
```
4. Push the changes to your forked repository.  
Push the merged changes to your forked repository on GitHub:
```
$ git push origin master
```
