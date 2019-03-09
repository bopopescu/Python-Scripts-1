

def anagram(s1,s2):

    # Confirming that length of strings is same
    if len(s1) != len(s2):
        return False

    s1=s1.replace(" ","").lower()
    s2=s2.replace(" ","").lower()
    print(s1,s2)

    # Track the count of letters in string
    count={}

    for letter in s1:
        if letter in count:
            count[letter] += 1
        else:
            count[letter]=1

    # Reduce the count of letter if it is also found in second string
    for letter in s2:
        if letter in count:
            count[letter] -=1
        else:
            count[letter]=1

    for letter in count:
        if count[letter] != 0:
            return False
    return True




print(anagram("Clint Eastwoodw", "Eastw oodclinte"))
