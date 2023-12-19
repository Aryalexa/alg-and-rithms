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

	def skip_whitespace(self):
		while self.current_char and self.current_char.isspace():
			self.advance()
	def string(self):
		s = ''
		self.advance()
		while self.current_char and self.current_char != '"':
			s += self.current_char
			self.advance()
		self.advance()
		return s

	
	def tokens(self):
		while self.current_char:
			if self.current_char.isspace():
				self.skip_whitespace()
				continue
			if self.current_char == '{':
				self.advance()
				yield Token(TokenType.LBRACE, '{')
			elif self.current_char == '}':
				self.advance()
				yield Token(TokenType.RBRACE, '}')
			elif self.current_char == ':':
				self.advance()
				yield Token(TokenType.COLON, ':')
			elif self.current_char == ',':
				self.advance()
				yield Token(TokenType.COMMA, ',')
			elif self.current_char == '"':
				yield Token(TokenType.STRING, self.string())
			else: 
				raise Exception(f'bad char {self.current_char}')
		yield None
			
class Parser:
	def __init__(self, lexer:Lexer) -> None:
		self.lexer = lexer
		self.current_token = next(self.lexer.tokens())

	def eat(self, token_type:TokenType):
		if self.current_token and self.current_token.type == token_type:
			self.current_token = next(self.lexer.tokens())
		else:
			raise Exception('unexpected token') # current_token vs expected_token

	def parse_key(self):
		if self.current_token and self.current_token.type == TokenType.STRING:
			key = self.current_token.value
			self.eat(TokenType.STRING)
			return key
		else:
			raise Exception("bad key")

	def parse_value(self):
		if self.current_token and self.current_token.type == TokenType.STRING:
			key = self.current_token.value
			self.eat(TokenType.STRING)
			return key
		else:
			raise Exception("bad value")

	def parse_object(self) -> dict:
		obj:dict = {}
		self.eat(TokenType.LBRACE)
		trailing_coma = False
		# ---- key:value LOOP
		while self.current_token and self.current_token.type != TokenType.RBRACE:
			trailing_coma = False
			key = self.parse_key()
			self.eat(TokenType.COLON)
			value = self.parse_value()
			obj[key] = value
			if self.current_token and self.current_token.type == TokenType.COMMA:
				self.eat(TokenType.COMMA)
				trailing_coma = True
		# ----
		if trailing_coma:
			raise Exception("trailing comma")
		self.eat(TokenType.RBRACE)
		return obj
		

def json_parser(json_str:str):
	lexer = Lexer(json_str)
	parser = Parser(lexer)
	
	x = parser.parse_object()
	print(x)
	return x
	#sys.exit(-1)
	#sys.exit(0)


if __name__ == '__main__':
	file = 'x'
	with open(f"test_files/{file}.txt") as f:
		json_str = f.read() 
	json_parser(json_str)