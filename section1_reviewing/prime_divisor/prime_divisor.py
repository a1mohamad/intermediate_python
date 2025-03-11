from math import sqrt
def is_prime(number):
    prime = True
    for i in range(2, int(sqrt(number))+ 1):
        if (number % i) == 0:
            prime = False
            break
    return prime

def divisor_counting(input_numbers):

    divisor_answer = 0
    number_answer = 0
    for every in input_numbers:
        divisor_count = 0
        for i in range(2, every):
            if is_prime(i):
                if every % i == 0:
                    divisor_count += 1
        if divisor_count > divisor_answer :
            divisor_answer = divisor_count
            number_answer = every
        elif divisor_count == divisor_answer:
            if every > number_answer:
                number_answer = every
                divisor_answer = divisor_count

    
    return print(number_answer, divisor_answer)

input_numbers_list = []
for i in range(10):
    input_numbers_list.append(int(input()))

divisor_counting(input_numbers_list)