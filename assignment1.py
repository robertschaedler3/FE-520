##### 1 #####
s1 = str()
print(s1)

s2 = "I'm a student"
print(s2)

s3 = """This course is very interesting.
I hope to learn a lot."""
print(s3)


##### 2 #####

a = 100
b = 9

c = a + b
print(c)

# a divided by b
print(a / b)
# integer part of a divided by b
print(a // b)
# remainder of a divided by b
print(a % b)
# a raised to the power of b
print(a ** b)
# boolean a not equal to b
print(a != b)
# boolean a greater than b
print(a > b)


##### 3 #####
List_A = [1, 2.2, 5.55555, 'i am a string', 'hello world', '1234']
List_B = [100, 987, 543.21, 'string 123', 'hola', 'a1']

List_A.extend(List_B)

List_A[1] = 'FE520'
del List_A[1]

# return and delete the last element of List_A
List_A.pop()

# create list from 3 to end
List_C = List_A[3:]

# double size of list
List_C = 2 * List_C

# reverse list
List_C = List_C.reverse()


##### 4 #####
A = [1, 2, 3, 5, 10, 1, 4, 10, 11, 20, 50, 100]
d = {}
for i in A:
    if i not in d:
        d[i] = 0
    d[i] += 1
print(d)


##### 5 #####

def seq_insert(seq, num):
    if len(seq) == 0:
        seq.append(num)
        return

    asc = None
    if sorted(seq) == seq:
        asc = True
    elif sorted(seq, reverse=True) == seq:
        asc = False
    else:
        raise ValueError('Invalid seqence given.')

    i = 0
    while i < len(seq):
        if (asc and seq[i] < num) or (not asc and seq[i] > num):
            i += 1
        else:
            break

    seq.insert(i, num)
