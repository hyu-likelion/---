word = input('단어를 입력해주세요 : ')

a_palindrome = True
for i in rage(len(word) // 2):
    if word[i] != word[-1 - i]:
        a_palindrome = False
        break

print(a_palindrome)