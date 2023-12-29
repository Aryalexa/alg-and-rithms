from abc import ABC, abstractmethod 
from collections import deque



def switch(signal):
	return {'L':'H', 'H':'L'}[signal]

class Module(ABC):
	
	def __init__(self, name, dests) -> None:
		super().__init__()
		self.name = name
		self.dests = dests
	def __str__(self) -> str:
		return f"Module({self.dests})"
	def __repr__(self) -> str:
		return f"Module({self.dests})"
	@abstractmethod
	def receive_and_send(self, signal_type, src) -> list:
		pass
	def signals_to_send(self, signal_type):
		to_send = []
		for dst in self.dests:
			to_send.append((self.name, signal_type, dst))
		return to_send

class Earth(Module):
	def receive_and_send(self, signal_type, src) -> list:
		return []

class FlipFlop(Module):
	def __init__(self, name, dests) -> None:
		super().__init__(name, dests)
		self.state_on = False
	def receive_and_send(self, signal_type, src) -> list:
		"""
		if a flip-flop module receives a low pulse, it flips between on and off.
		If it was off, it turns on and sends a high pulse.
		If it was on, it turns off and sends a low pulse.
		"""
		if signal_type == 'L':
			if not self.state_on:
				self.state_on = True
				return self.signals_to_send('H')
			else:
				self.state_on = False
				return self.signals_to_send('L')
		else:
			return []

class Conjunction(Module):
	def __init__(self,name,  dests) -> None:
		super().__init__(name, dests)
		self.dests_last_signal = {}
	def receive_and_send(self, signal_type, src) -> list:
		"""
		remember the type of the most recent pulse received from each of their connected input modules;
		they initially default to remembering a low pulse for each input.
		
		When a pulse is received, the conjunction module first updates its
		memory for that input.
		Then, if it remembers high pulses for all inputs, 
		it sends a low pulse; otherwise, it sends a high pulse.
		"""
		# print(self.dests_last_signal, end=', then ')
		self.dests_last_signal[src] = signal_type
		# print(self.dests_last_signal)
		if all(s == 'H' for s in self.dests_last_signal.values()):
			return self.signals_to_send('L')
		else:
			return self.signals_to_send('H')
		
class Broascast(Module):
	def __init__(self, name, dests) -> None:
		super().__init__(name, dests)
	def receive_and_send(self, signal_type, src) -> list:
		to_send = self.signals_to_send(signal_type)
		return to_send
	
class Button(Module):
	"""
	When you push the button, a single low pulse is sent directly to the broadcaster module
	"""
	def __init__(self, name, broascast) -> None:
		super().__init__(name, [broascast])
	def receive_and_send(self, signal_type, src) -> list:
		assert False, "button doesnt recieve!!"

def check_all_ff_off():
	all_ff_off = True
	for name, mod in modules.items():
		if isinstance(mod, FlipFlop):
			all_ff_off = all_ff_off and not mod.state_on
	return all_ff_off



def push_button():
	count_L = 0
	count_H = 0
	press_button_s = ('button', 'L', 'broadcaster')

	signals.append(press_button_s)
	while signals:
		cur_s = signals.popleft()
		src, stype, dst = cur_s
		#print(f"{src} -{stype}-> {dst}")
		if stype == 'L':
			count_L += 1
		else:
			count_H += 1
		new_ss = modules[dst].receive_and_send(stype, src)
		for new_s in new_ss:
			signals.append(new_s)
	return count_L, count_H


def manage_signals():
	# press button
	count_L = 0
	count_H = 0

	assert check_all_ff_off(), 'bad start'
	
	PUSH_BUTTON_TIMES = 1000
	for i in range(PUSH_BUTTON_TIMES):
		print(f'*** {i}')
		cL,cH = push_button()
		count_L += cL
		count_H += cH
	return count_L, count_H


def update_conjuction_inputs_and_earths():
	earths:list[Earth] = []
	conjs:list[Conjunction] = []
	for s_name, mod in modules.items():
		for d_name in mod.dests:
			if d_name not in modules:
				earths.append(Earth(d_name, []))
			else:
				d = modules[d_name]
				if isinstance(d, Conjunction):
					d.dests_last_signal[s_name] = 'L'
					conjs.append(d)
	for e in earths:
		modules[e.name] = e
	for c in conjs:
		modules[c.name] = c

def read_modules():
	with open("in") as f:
		for line in f.read().splitlines():
			name, dsts = line.split(' -> ')
			dsts = dsts.split(', ')
			if name == 'broadcaster':
				b = Broascast(name, dsts)
				modules[name] = b
			elif name.startswith('%'):
				ff = FlipFlop(name[1:], dsts)
				modules[name[1:]] = ff
			elif name.startswith('&'):
				c = Conjunction(name[1:],dsts)
				modules[name[1:]] = c
			else:
				raise Exception('bad input')
		button = Button('button', 'broadcaster')
		modules['button'] = button
		update_conjuction_inputs_and_earths()

signals = deque()
modules:dict[str, Module] = {}

read_modules()
print(modules)
cL, cH = manage_signals()
print(cL, cH, '. res:', cL*cH)