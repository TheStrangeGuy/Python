# Prime or not prime. Input: L= [3,4,6,9,11] Output: L= [P, NP, NP, NP, P] using map function .

def p_or_np(number):

    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                print("NP")
                break
        else:
            print("P")

    else:
        print(number, "is not a prime number")

pnp = [3, 4, 6, 9, 11]

list(map(p_or_np, pnp))
