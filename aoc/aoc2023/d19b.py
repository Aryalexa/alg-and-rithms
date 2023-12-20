from collections import OrderedDict
from tqdm import tqdm
from copy import deepcopy

class WF:
	def __init__(self, name:str, rules:list) -> None:
		self.name = name
		self.rules = rules
	def __str__(self) -> str:
		conds_str = ','.join(f'{x}' for x in self.rules)
		return f'WF({self.name}, {conds_str})'

def read_workflows(s:str) -> OrderedDict[str,WF]:
	wfs = OrderedDict()
	for wf in s.splitlines():
		name, rules = wf[:-1].split('{')
		rules = [item.split(':') for item in rules.split(',')]
		x = WF(name, rules)
		wfs[name] = x
	return wfs



def check_condition(p:dict, cond_str) -> bool:
	if cond_str == "end":
		return True
	cat, comp = cond_str[:2]
	thr = int(cond_str[2:])
	if comp =='>':
		return p[cat] > thr
	if comp =='<':
		return p[cat] < thr
	raise Exception(f"new symbol {comp}")
	

def check_workflow(p:dict, rules: OrderedDict[str, WF], rule_name:str) -> str:
	#print(rule_name, end=' ')
	if rule_name in "AR":
		return rule_name
	rule = rules[rule_name]
	for cond in rule.rules:
		if len(cond) == 1:
			cond_str, new_rule = "end", cond[0]
		else:
			cond_str, new_rule = cond
		if check_condition(p, cond_str):
			return check_workflow(p, rules, new_rule)
	assert False, rule.rules


def sort_part(p:dict, rules: OrderedDict[str, WF]) -> str:
	res = check_workflow(p, rules, 'in')
	if res in "AR":
		return res
	assert False, res

def get_comb(space) -> int:
	p = 1
	for a,b in space.values():
		p *= b-a+1
	return p

def divide_space(space, cond_str):
	cat, comp = cond_str[:2]
	thr = int(cond_str[2:])
	space_1 = {**space}
	space_2 = {**space}
	if comp == '>':
		v1 = ([0,-1] if thr > space_1[cat][1] 
			else [max(space_1[cat][0], thr+1), space_1[cat][1]])
		space_1[cat] = v1
		v2 = ([0,-1] if thr < space_2[cat][0]
		 	else [space_2[cat][0], min(space_2[cat][1], thr)])
		space_2[cat] = v2
	if comp =='<':
		v1 = ([0,-1] if thr < space_1[cat][0] 
			else [space_1[cat][0], min(space_1[cat][1], thr-1)])
		space_1[cat] = v1
		v2 = ([0,-1] if thr > space_2[cat][1]
		 	else [max(space_2[cat][0], thr), space_2[cat][1]])
		space_2[cat] = v2
	return space_1, space_2


def combs_for_wf(space, wf_name) -> int:
	#print('*', wf_name, space)
	if wf_name == 'A':
		return get_comb(space)
	elif wf_name == 'R':
		return 0
	combs = 0
	rules = wfs[wf_name].rules
	for rule in rules:
		#print(rule)
		if len(rule)==1:
			new_wf = rule[0]
			return combs + combs_for_wf(space, new_wf)
		else:
			cond, new_wf = rule
			space_1, space_2 = divide_space(space, cond)
			combs += combs_for_wf(space_1, new_wf)
			space = space_2
	assert False, 'jaja'






# -----------------

with open("in") as f:
	wf_str, _ = f.read().split('\n\n')
wfs = read_workflows(wf_str)
# for k, wf in wfs.items():
# 	print(wf)

print('processin 4K^4')
space_ini = {'x':[1,4000],'m':[1,4000],
		 'a':[1,4000],'s':[1,4000]}

wf_ini = 'in'
ret = combs_for_wf(space_ini, wf_ini)
print(ret)

# for x in tqdm(range(1, 4000+1)):
# 	for m in range(1, 4000+1):
# 		for a in range(1, 4000+1):
# 			for s in range(1, 4000+1):
# 				p = {'x':x, 'm':m, 'a':a, 's':s}
# 				res_p = sort_part(p, wfs)
# 				if res_p == "A":
# 					ret += 1

# print(ret)

""" T=10
a>3:A, b<5:A, R
		a	b
a>3 -> T-3 x T : 7x10  OR
b<5 -> T x 5-1 : 10x4
       -------- c1 or c2
		T x T

not (c1 or c2) = not c1 and not c2
			a	b
not c1 -> 	3 x T : 3x10	AND
not c2 -> 	T x 6 : 10x6
			------------
			3 x 6 : 18 ----R
A: TxT - R = 10x10 - 3x6 = 82



"""

"""
WF(lhv, ['a>2928', 'R'],['a>2900', 'gd'],['R'])
a < 2928 
and
'a>2900' and gd
rest: R


gd{x<1717:A,m<3837:A,R}
            	x		m	a	s
c1:x<1717 ->  1717-1	xT 	xT	xT	OR
c2:m<3837 ->  T	  x 3837-1	xT	xT
			---------------------- c1 or c2
c3 (R): 	not (c1 or c2) = not c1 and not c2
R 			T-1717 x T-3837 x T x T
-> TxTxTxT - R

WF(qg, ['x>3174', 'R'],['s<2028', 'A'],['R'])
            	x		m	a	s
c1:(R)x>3174 -> T-3174 x T x T x T
not c1 		->	3174 x 	T x T x T 		AND
c2:(A)s<2028 -> T	x	T x T x 2028-1
			--------------------------- not c1 and c2
		A	3174 x T x T x 2028-1
-> A


how many are accepted?
[R, R, R] -> 0
[R, R, A] -> 
c1 :R, not c1 :A
c1 or c2 :R
not c1 and not c2: A

[R, A, A]
[A, A, A]
[A, A, R]
[A, R, R]



"""


# print(wf_str)
# print(parts_str)


"""
1-4K, 1-4K, 1-4K, 1-4K
in: s<1351
	n1: s<1351 -> px
	n2: cc -> qqz
px: {a<2006:qkq,m>2090:A,rfg}
	n1: a<2006 -> qkq
	n2: cc -> next
		n1: m>2090 -> A
		n2: cc -> next
			rfg
rfg: {s<537:gd,x>2440:R,A}



"""