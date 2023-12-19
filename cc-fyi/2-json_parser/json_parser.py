import sys
import re


from enum import Enum, auto
class TokenType(Enum):
    STRING = auto()
    NUMBER = auto()
    BOOLEAN = auto()
    NULL = auto()
    LBRACE = auto()
    RBRACE = auto()
    LBRACKET = auto()
    RBRACKET = auto()
    COMMA = auto()
    COLON = auto()


class Token:

	def __init__(self, type:TokenType, value) -> None:
		self.type = type
		self.value = value
	def __str__(self) -> str:
		return f"Token({self.type} = {self.value})"

class Lexer:
	"""
	Its main responsibility is to break down the input source code into a sequence of tokens.
	Tokens: str, num, bool, null, (), {}, ',', ':'
	"""
	def __init__(self, text:str):
		self.text = text
		self.pos = -1
		self.current_char = None
		self.advance()

	def advance(self):
		self.pos += 1
		if self.pos < len(self.text):
			self.current_char = self.text[self.pos]
		else:
			self.current_char = None
	
	def get_next_token(self):
		while self.current_char:
			if self.current_char =='{':
				self.advance()
				yield Token(TokenType.LBRACE, '{')
			elif self.current_char =='}':
				self.advance()
				yield Token(TokenType.RBRACE, '}')
			else: 
				raise Exception('')
		yield None
			
class Parser:
	def __init__(self, lexer:Lexer) -> None:
		self.lexer = lexer
		self.current_token = next(self.lexer.get_next_token())

	def eat(self, token_type:TokenType):
		if self.current_token and self.current_token.type == token_type:
			self.current_token = next(self.lexer.get_next_token())
		else:
			raise Exception('unexpected token') # current_token vs expected_token



	def json_dict(self):
		d:dict = {}
		print(self.current_token)
		if self.current_token and self.current_token.type == TokenType.LBRACE:
			self.eat(TokenType.LBRACE)
		else:
			raise Exception("bad start")
		
		if self.current_token and self.current_token.type == TokenType.RBRACE:
			self.eat(TokenType.RBRACE)
		else:
			raise Exception("bad end")
		return d
		

def json_parser(json_str:str):
	lexer = Lexer(json_str)
	parser = Parser(lexer)
	
	x = parser.json_dict()
	print(x)
	return x
	#sys.exit(-1)
	#sys.exit(0)


if __name__ == '__main__':
	file = 'x'
	with open(f"test_files/{file}.txt") as f:
		json_str = f.read() 
	json_parser(json_str)