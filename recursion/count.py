# For this challenge, we'd like you to convert the following while loop that counts to a recursive method that counts. Your method is successful if it prints numbers 0-9. Remember: it must call itself!

    # count = 0

    # while count < 10:
    #   print(count)
    #   count += 1

#Solution 1 - O(n)
def recursive_count(n):
    print(n)
    if n <= 8:
        recursive_count(n+1)

recursive_count(0)

# Solution 2 - O(n) 
def recursive_count_2(count=0):
    if count < 10:
        print(count)
        recursive_count(count + 1)

recursive_count_2()