def repeats_till_end(substr: str, orig_str: str):
    for i in range(0, len(orig_str), len(substr)):
        if substr != orig_str[i:i + len(substr)]:
            return False
    return True

def find(s: str):
    s_len = len(s)
    for i in range(1, s_len + 1):
        if s_len % i == 0:
            if repeats_till_end(s[0:i], s):
                return i


if __name__ == "__main__":
    print(find("aaa")) # 1
    print(find("abcd")) # 4
    print(find("abcabcabcabc")) # 3
    print(find("aybabtuaybabtu")) # 7
    print(find("abcabca")) # 7