N = int(input("type children: "))
K = int(input("type mandarins: "))

mandarins_per_student = K // N
remainder_in_basket = K % N

print(mandarins_per_student)
print(remainder_in_basket)