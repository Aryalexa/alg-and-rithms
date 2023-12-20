from collections import OrderedDict
class WF:
	def __init__(self, name:str, conds:list) -> None:
		self.name = name
		self.conds = conds
	def __str__(self) -> str:
		conds_str = ','.join(f'{x}' for x in self.conds)
		return f'WF({self.name}, {conds_str})'

def read_workflows(s:str) -> OrderedDict[str,WF]:
	wfs = OrderedDict()
	for wf in s.splitlines():
		name, conds = wf[:-1].split('{')
		conds = [item.split(':') for item in conds.split(',')]
		x = WF(name, conds)
		wfs[name] = x
	return wfs


def read_parts_ratings(s:str) -> list[dict]:
	def read_part(s:str) -> dict[str, int]:
		part_dict = {}
		ratings = s[1:-1].split(',')
		for r in ratings:
			cat, num = r.split('=')
			part_dict[cat] = int(num)
		return part_dict

	prs = []
	for part_str in s.splitlines():
		prs.append(read_part(part_str))
	return prs

def part_value(part_dict:dict[str,int]):
	return sum(v for v in part_dict.values())

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
	print(rule_name, end=' ')
	if rule_name in "AR":
		return rule_name
	rule = rules[rule_name]
	for cond in rule.conds:
		if len(cond) == 1:
			cond_str, new_rule = "end", cond[0]
		else:
			cond_str, new_rule = cond
		if check_condition(p, cond_str):
			return check_workflow(p, rules, new_rule)
	assert False, rule.conds


def sort_part(p:dict, rules: OrderedDict[str, WF]) -> str:
	res = check_workflow(p, rules, 'in')
	if res in "AR":
		return res
	assert False, res


with open("in") as f:
	wf_str, parts_str = f.read().split('\n\n')
wfs = read_workflows(wf_str)
parts = read_parts_ratings(parts_str)


ret = 0
for p in parts:
	res_p = sort_part(p, wfs)
	print(res_p)
	if res_p == "A":
		ret += part_value(p)

print(ret)






# print(wf_str)
# print(parts_str)