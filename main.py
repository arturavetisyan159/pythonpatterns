class String:
    def concatenate(self, string1: str, string2: str) -> str:
        return string1 + string2

    def make_uppercase(self, string: str) -> str:
        return string.upper()

    def make_lowercase(self, string: str) -> str:
        return string.lower()

    def capitalize(self, string: str) -> str:
        res = ""
        for l in range(len(string)):
            if l == 0 and 97 <= ord(string[1]) <= 122:
                res += chr(ord(string[l]) - 32)
            elif l != 0 and 65 <= ord(string[l]) <= 90:
                res += chr(ord(string[l]) + 32)
            else:
                res += string[l]
        return res

    def replace(self, string: str, pattern: str, replacement: str) -> str:
        length_pattern = len(pattern)
        res = ''
        for i in range(len(string)):
            if string[i:i + length_pattern] == pattern:
                res = string[:i] + replacement + string[i + length_pattern:]
        return res


def main():
    string = String()
    print(string.concatenate("pyt", "hon"))
    print(string.make_lowercase("PYTHON"))
    print(string.make_uppercase("python"))
    print(string.replace("mama myla ramu", "mama", "rama"))
    print(string.capitalize("artur"))


if __name__ == '__main__':
    main()