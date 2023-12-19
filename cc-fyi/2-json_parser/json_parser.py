import sys

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
	
	def number(self):
		n = ''
		while self.current_char and (self.current_char.isdigit() or self.current_char == '.'):
			n += self.current_char
			self.advance()
		points_count = n.count('.')
		if points_count == 0:
			return int(n)
		elif points_count == 1:
			return float(n)
		else:
			raise Exception("bad number")
		
	def boolean(self):
		b = ''
		target = "true" if self.current_char == 't' else "false"
		for c in target:
			if self.current_char == c:
				b += c
				self.advance()
			else:
				break
		if b == "true":
			return True
		elif b == "false":
			return False
		else:
			raise Exception("bad boolean")
		
	def null(self):
		n = ''
		for c in "null":
			if self.current_char == c:
				n += c
				self.advance()
			else:
				break
		if n == "null":
			return None
		else:
			raise Exception("bad null")

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
			elif self.current_char == '[':
				self.advance()
				yield Token(TokenType.LBRACKET, '[')
			elif self.current_char == ']':
				self.advance()
				yield Token(TokenType.RBRACKET, ']')
			elif self.current_char == ':':
				self.advance()
				yield Token(TokenType.COLON, ':')
			elif self.current_char == ',':
				self.advance()
				yield Token(TokenType.COMMA, ',')
			elif self.current_char == '"':
				yield Token(TokenType.STRING, self.string())
			elif self.current_char.isdigit():
				yield Token(TokenType.NUMBER, self.number())
			elif self.current_char == 't' or self.current_char == 'f':
				yield Token(TokenType.BOOLEAN, self.boolean())
			elif self.current_char == 'n':
				yield Token(TokenType.NULL, self.null())
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
	
	def parse_array(self) -> list:
		arr:list = []
		self.eat(TokenType.LBRACKET)
		trailing_coma = False
		while self.current_token and self.current_token.type != TokenType.RBRACKET:
			trailing_coma = False
			value = self.parse_value()
			arr.append(value)
			if self.current_token and self.current_token.type == TokenType.COMMA:
				self.eat(TokenType.COMMA)
				trailing_coma = True
		if trailing_coma:
			raise Exception("trailing comma")
		self.eat(TokenType.RBRACKET)
		return arr

	def parse_value(self):
		token = self.current_token
		if token:
			if token.type == TokenType.STRING:
				self.eat(TokenType.STRING)
				return token.value
			elif token.type == TokenType.NUMBER:
				self.eat(TokenType.NUMBER)
				return token.value
			elif token.type == TokenType.BOOLEAN:
				self.eat(TokenType.BOOLEAN)
				return token.value
			elif token.type == TokenType.NULL:
				self.eat(TokenType.NULL)
				return token.value
			elif token.type == TokenType.LBRACKET:
				return self.parse_array()
			elif token.type == TokenType.LBRACE:
				return self.parse_object()
		raise Exception(f"bad value {token}")

	def parse_object(self) -> dict:
		obj:dict = {}
		self.eat(TokenType.LBRACE)
		trailing_coma = False
		while self.current_token and self.current_token.type != TokenType.RBRACE:
			trailing_coma = False
			key = self.parse_key()
			self.eat(TokenType.COLON)
			value = self.parse_value()
			obj[key] = value
			if self.current_token and self.current_token.type == TokenType.COMMA:
				self.eat(TokenType.COMMA)
				trailing_coma = True
		if trailing_coma:
			raise Exception("trailing comma")
		self.eat(TokenType.RBRACE)
		return obj

def json_parser(json_str:str):
	lexer = Lexer(json_str)
	parser = Parser(lexer)

	result = parser.parse_object()
	print(result)
	return result
	# try:
	# 	result = parser.parse_object()
	# 	return result
	# except Exception as e:
	# 	print(f"Error: {e}")
	# 	sys.exit(1)

if __name__ == '__main__':
	...
# 	file = 'x'
# 	with open(f"test_files/{file}.txt") as f:
# 		json_str = f.read() 
# 	json_parser(json_str)