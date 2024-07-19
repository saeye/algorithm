def is_palindrome(word):
    # 하나의 값으로 이루어지면 펠린드롬 성립
    if len(word) == 1:
        print(f"{word}는 하나의 문자열로 이루어져 있으므로 볼 것도 없이 펠린드롬입니다.")
        return True
    # 맨 앞과 맨 뒤가 다르면 무조건 False니까
    if word[0] != word[-1]:
        print(f"입력한 {word}의 맨 앞과 맨 뒤가 다릅니다. 볼 것도 없습니다.")
        return False

    reversed_word = word[::-1]

    if word == reversed_word:
        print(f"입력한 {word}를 뒤집으면, {reversed_word}로 동일합니다.")
        return True

    else:
        print(word, reversed_word)
        print(f"입력한 {word}를 뒤집으면, {reversed_word} 동일하지 않습니다.")
        return False


print(is_palindrome("123"))
print(is_palindrome("121"))
print(is_palindrome("a"))
print(is_palindrome("eye"))
