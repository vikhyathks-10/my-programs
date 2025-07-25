nth_num = input("Enter the number of Fibonacci terms you want: ")
series = []
fib_sum = 0
for i in range(int(nth_num)):
    if i == 0:
        series.append(0)
    elif i == 1:
        series.append(1)
        fib_sum += 1
    else:
        next_num = series[i - 1] + series[i - 2]
        series.append(next_num)
        fib_sum += next_num
    print(f"Step {i}: Series = {series}, Sum = {fib_sum}")
