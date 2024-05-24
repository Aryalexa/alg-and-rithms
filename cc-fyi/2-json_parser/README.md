# Challenge: Build Your Own JSON Parser

This challenge is to build your own JSON parser.

Building a JSON parser is an easy way to learn about parsing techniques which are useful for everything from parsing simple data formats through to building a fully featured compiler for a programming language.

Parsing is often broken up into two stages: lexical analysis and syntactic analysis. 
- Lexical analysis is the process of dividing a sequence of characters into meaningful chunks, called tokens.
- Syntactic analysis (which is also sometimes referred to as parsing) is the process of analysing the list of tokens to match it to a formal grammar.

So the steps would be: defining the grammar, tokenizing the input, and parsing the tokens.

### The grammar
```
"{" OBJECTS "}"
OBJECTS: OBJECT [ "," OBJECTS ]
OBJECT: [KEY ":" VALUE]
KEY: str
VALUE: [str | num | bool | null | "[" VALUES "]" | "{" OBJECTS "}" ]
VALUES: VALUE [ "," VALUES ]
```
The final tokens are: str, num, bool, null, [], {}, ',', ':'

### The lexer
It will divide the input into tokens (tokenization).
We could return a list of the ordered tokens or (leveraging python) generate token by token.

The tokens being: str, num, bool, null, [], {}, ',', ':'

### The parser
It should go token by token in order and verify if the grammar is being respected, at the same time it should be building some data structure containing the interpretation of the input, ready to be used later for whaterver purpose you parse your input.

In our json case, we'll build a python dictionary and this way we'll be able to use the json information easily in python.
