# homework
def compare(l1, l2):
    add = []
    mis = []

    for i in l2:
        if i not in l1:
            add += [i]

    for i in l1:
        if i not in l2:
            mis += [i]

    return add, mis

# challenge
def primes(n):
    sum = 0
    prime = True

    for i in range(2, n):
        for a in range(2, i):
            if i % a == 0:
                prime = False
                break
        if prime:
            sum += i
        prime = True

    return sum
