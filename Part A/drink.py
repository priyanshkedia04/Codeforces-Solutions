def soft_drink(n, k, l, c, d, p, nl, np):
	drink = (k*l)//nl
	slices = c*d
	salt = p//np
	glasses = min(drink, slices, salt)
	print(glasses//n)

n, k, l, c, d, p, nl, np = map(int, input().split())
soft_drink(n, k, l, c, d, p, nl, np)