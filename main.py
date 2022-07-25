import os

print("Adding even numbers from 1 to 101...")
even_sum = 0
for number in range(1,101):
    if number % 2 == 0:
        print(f"Adding {number} to {even_sum}")
        even_sum += number
        print(f"New sum is {even_sum}")
    else:
        continue
print("\n")
print(f"Total sum = {even_sum}")
os.system('pause')