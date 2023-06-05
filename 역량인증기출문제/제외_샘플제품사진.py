import sys

def main():
	sol = 1e9
	N = int(input())
	info = []
	pid_set = set()
	for _ in range(N):
		x, y = map(int, input().split())
		info.append([x,y])
		pid_set.add(y)
	
	pid = dict()
	numbering = 0
	for i in sorted(pid_set):
		pid[i] = numbering
		numbering += 1
	
	info2 = []
	for x, y in sorted(info):
		info2.append([x, pid[y]])
		
	check = [0 for _ in range(len(pid))]
	
	# 여기서부터 작성
	s = 0
	for e in range(len(info2)):
		check[ info2[e][1] ] += 1
		while 0 not in check:
			sol = min(sol, info2[e][0] - info2[s][0])
			check[ info2[s][1] ] -= 1
			s += 1			
			
	# 출력하는 부분
	print(sol)


if __name__ == '__main__':
	main()
