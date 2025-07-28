try:
    sentence = input("Enter a sentence: ")
    words = sentence.split()
    count = len(words)
    print("Number of words:", count)

except Exception as e:
    print("Something went wrong:", e)
