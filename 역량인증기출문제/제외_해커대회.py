
def main():
	L = list(input())
	C = input()
	R = []	
		
	for cmd in C:
		if cmd == "L":
			if len(L)>0:
				R.append(L.pop())
		elif cmd == "R":
			if len(R)>0:
				L.append(R.pop())
		elif cmd == "B":
			if len(L)>0:
				L.pop()
		else:
			L.append(cmd)

	print("".join(L+R[::-1]))

	
if __name__ == '__main__':
	main()