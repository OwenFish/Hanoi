import time
from Stack import Stack

# n - number of disks
# s - source stack
# a - auxiliary stack
# d - destination stack

def Hanoi_rec(n, s, a, d):
	print(n, 's', s, 'a', a, 'd', d)
	if n == 1:
		a.push(s.pop())
		print(n, 's', s, 'a', a, 'd', d)
		d.push(s.pop())
		print(n, 's', s, 'a', a, 'd', d)
		d.push(a.pop())
		print(n, 's', s, 'a', a, 'd', d)
	else:
		Hanoi_rec(n - 1, s, d, a) # get the subpyramid above the largest one onto the aux peg.
		print(n, 's', s, 'a', a, 'd', d)
		# d.push(s.pop()) # move the bottom peg onto the destination peg.
		print(n, 's', s, 'a', a, 'd', d)
	print(n, 's', s, 'a', a, 'd', d)
	print()

def Hanoi(n):
	source = Stack()
	dest = Stack()
	aux = Stack()
	i = n - 1
	while i >= 0:
		source.push(i)
		i = i - 1
	Hanoi_rec(n - 1, source, aux, dest)

if __name__ == '__main__':
	start = time.clock()
	n = 5
	Hanoi(n)
	end = time.clock()
	print('computed Hanoi(' + str(n) + ') in ' + str(end - start) + ' seconds.')