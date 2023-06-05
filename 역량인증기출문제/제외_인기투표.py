import sys
read = sys.stdin.readline


def main():
	
	N = int(read().rstrip())
	A = read().rstrip().split()
	dict_name = {}
	for name in A:
		dict_name[name] = 0
		
	M = int(read().rstrip())
	for _ in range(M):
		name, score = read().rstrip().split()
		score = int(score)
		if name in dict_name:
			dict_name[name] += score
	
	# B = list(sorted(dict_name.items(), key=lambda x:x[1], reverse = True))
	B = []
	for name in A:
		B.append([name, dict_name[name]])
	B = sorted(B, key=lambda x:x[1], reverse = True)

	for i in range(3):
		print(B[i][0], B[i][1])
		
if __name__ == '__main__':
	main()
