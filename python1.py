start=10
end=30

for num in range(start, end + 1):
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)

print("-------------------------------------------------------------")

sen = str(input("sentence:"))
s=sen.split()
print(s)

max_len = -1
for ele in s:
    if len(ele) > max_len:
        max_len = len(ele)
        res = ele
print(res)

print("-------------------------------------------------------------")

def eval_bool(exp):
    res= eval(exp)
    if isinstance(res,bool):
        return res
print(eval_bool('True and False or True'))

print("-------------------------------------------------------------")

def func(list):
    list.sort(reverse=True)
    print(list[1])
func([10,20,3,45,99])

print("-------------------------------------------------------------")

def func1(tuple1,tuple2):
    print(tuple(sorted(tuple(tuple1+tuple2))))

func1((1,3,5),(2,4,6))

print("-------------------------------------------------------------")

def dic(inv_dict):
    dict = {v: k for k, v in inv_dict.items()}
    print("inverse mapped dictionary : ", str(dict))
dic({'a':1,'b':2,'c':3})

print("-------------------------------------------------------------")

import collections
ini_dict = [ {'a': 1, 'b': 2}, 
			 {'b': 3, 'c': 4}
			]
counter = collections.Counter()
for d in ini_dict: 
	counter.update(d)
result = dict(counter)
print(result)

print("-------------------------------------------------------------")

def diff(set1,set2):
    print(set1.symmetric_difference(set2))
diff({1,2,3},{3,4,5})

print("-------------------------------------------------------------")

def subsets(numbers):
	if numbers == []:
		return [[]]
	x = subsets(numbers[1:])
	return x + [[numbers[0]] + y for y in x]

# wrapper function
def subsets_of_given_size(numbers):
	return [x for x in subsets(numbers)]

if __name__ == '__main__':
	numbers = [1, 2, 3]
	print(subsets_of_given_size(numbers))

print("-------------------------------------------------------------")

def leap(year):
    if year%2==0 & year%4==0:
        print('leap year')
    else:
        print('not')
leap(2020)

print("-------------------------------------------------------------")

import cmath
def solve(a,b,c):
    d = (b**2) - (4*a*c)

    sol1 = (-b-cmath.sqrt(d))/(2*a)
    sol2 = (-b+cmath.sqrt(d))/(2*a)

    print('The solution are {0} and {1}'.format(sol1,sol2))
solve(1,-3,2)

print("-------------------------------------------------------------")

nterms = int(input("terms="))

n1, n2 = 0, 1
count = 0
if nterms <= 0:
   print("invalid")
elif nterms == 1:
   print()
   print(n1)
else:
   print()
   while count < nterms:
       print(n1)
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1

print("-------------------------------------------------------------")


def subsets(numbers):
	if numbers == []:
		return [[]]
	x = subsets(numbers[1:])
	return x + [[numbers[0]] + y for y in x]

# wrapper function
def subsets_of_given_size(numbers):
	return [x for x in subsets(numbers)]

if __name__ == '__main__':
	numbers = [10, 22, 9, 33, 21, 50, 41, 60, 80]
	subsets= subsets_of_given_size(numbers)
	res=max(subsets, key=len)
	print(res)

print("-------------------------------------------------------------")

def gcd(x, y):

	if x > y:
		small = y
	else:
		small = x
	for i in range(1, small + 1):
		if((x % i == 0) and (y % i == 0)):
			gcd = i
			
	return gcd

print (gcd(48,18))

print("-------------------------------------------------------------")

def collatz(n):
    while n > 1:
        print(n, end=' ')
        if (n % 2):
            n = 3*n + 1
        else:
            n = n//2
    print(1, end='')
 
 
n = int(input())
collatz(n)

print("-----------------------END-------------------------------------")
