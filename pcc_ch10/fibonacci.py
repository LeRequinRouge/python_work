# simple for-fun program unrelated to python crash course
first_num = 0
second_num = 1
sum_num = 0

# first 20 sums of the fibonacci sequence
for sequence in range(0, 20):
    sum_num = first_num + second_num
    print(f"Sequence {sequence}: Sum {sum_num}")
    first_num = second_num
    second_num = sum_num