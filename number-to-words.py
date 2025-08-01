units = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
         "sixteen", "seventeen", "eighteen", "nineteen"]
tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

num = int(input("Enter a number (0–99): "))

if 0 <= num < 10:
    print(units[num])
elif 10 <= num < 20:
    print(teens[num - 10])
elif 20 <= num < 100:
    t = tens[num // 10]
    u = "" if num % 10 == 0 else "-" + units[num % 10]
    print(t + u)
else:
    print("Number out of range.")
