def is_palindrome(word):

    # 슬라이싱을 이용하여 문자열 전체를 뒤집기
    reversed_word = word[::-1]

    # 원래 글자와 뒤집은 글자가 같으면 True
    if word == reversed_word:
        message = f"입력한 {word}를 뒤집으면, {reversed_word} 동일합니다."
        print(True, message, sep=', ')

    # 다르면
    else:
        message = f"입력한 {word}를 뒤집으면, {reversed_word} 동일하지 않습니다."
        print(False, message, sep=', ')


is_palindrome("a")
is_palindrome("123")
is_palindrome("121")
is_palindrome("eye")
