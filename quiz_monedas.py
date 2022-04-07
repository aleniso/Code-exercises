class Register:
	def __init__(self, new_name = "N/A",new_init_coins = 0,new_number = 0, new_coins = 0):
		self.name = new_name
		self.chest_initial_coins = new_init_coins
		self.register_number = new_number
		self.coins = new_coins
		self.coins_added = 0
	
	def add_coins(self,coins_to_add = 0):
		self.coins_added = self.coins_added + coins_to_add
	
	def report(self):
		print(self.name," ", self.register_number)
		print("Initial coins in chest : ", self.chest_initial_coins)
		print("Coins taken: ", self.coins)
		print("Coins added: ", self.coins_added)
		print("Total coins: ", self.coins_added + self.coins,"\n")
	

def remainder(a,b):
	a = abs(a)
	b = abs(b)
	
	if (a == 0):
		return 0
	
	if (b == 0):
		return -1
	
	if (a < b):
		return 0
	
	q = 1
	r = a - b*q
	while (r >= b):
		q = q + 1
		r = a - b*q
		
	r = abs(r)
	q = abs(q)
	return r, q


def solve_quiz():
	n = 100001 #240 test case
	max_results = 10 #1 test case
	list_of_results = []
	while (len(list_of_results) < max_results):
		sailor_coins = 0
		sailor_count = 1
		current_sailor_list = []
		left_coins = n
		r = remainder(left_coins,3)
		if ( r[0] ==  1):
			sailor_coins = r[1]
			current_sailor_list.append(Register("Marinero",left_coins,sailor_count,sailor_coins))
			left_coins = left_coins - sailor_coins - 1
			sailor_count = sailor_count + 1
			r = remainder(left_coins,3)
			if (r[0] ==  1):
				sailor_coins = r[1]
				current_sailor_list.append(Register("Marinero",left_coins,sailor_count,sailor_coins))
				left_coins = left_coins - sailor_coins - 1
				sailor_count = sailor_count + 1
				r = remainder(left_coins,3)
				if (r[0] ==  1):
					sailor_coins = r[1]
					current_sailor_list.append(Register("Marinero",left_coins,sailor_count,sailor_coins))
					left_coins = left_coins - sailor_coins - 1
					sailor_count = sailor_count + 1
					r = remainder(left_coins,3)
					if (r[0] ==  1):
						coins_to_be_distribuited = r[1]
						sailor_coins = 1
						current_sailor_list.append(Register("Almojarife",left_coins,sailor_count,sailor_coins))
						for count in range(len(current_sailor_list) - 1):
							current_sailor_list[count].add_coins(coins_to_be_distribuited)
						list_of_results.append(current_sailor_list)
		
		n = n+1
	#report
	result_count = 0
	while(result_count < len(list_of_results)):
		sailor_list_count = 0
		sailor_list = list_of_results[result_count]
		print("\n-----------------------------------\n")
		print("List number : ", result_count+1)
		while(sailor_list_count < len(sailor_list)):
			sailor = sailor_list[sailor_list_count]
			sailor.report()			
			sailor_list_count = sailor_list_count + 1
		print("Coins dropped : ", 3)
		result_count = result_count + 1


solve_quiz()
