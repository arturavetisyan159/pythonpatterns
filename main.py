class String:
    def concatenate(self, string1: str, string2: str) -> str:
        pass

    def make_uppercase(self, string: str) -> str:
        pass

    def make_lowercase(self, string: str) -> str:
        pass

    def capitalize(self, string: str) -> str:
        pass

    def replace(self, string: str, pattern: str, replacement: str) -> str:
        length_pattern = len(pattern)
        res = ''
        for i in range(len(string)):
            if string[i:i + length_pattern] == pattern:
                res = string[:i] + replacement + string[i + length_pattern:]
        return res


def main():
    string = String()
    print(string.replace("mama myla ramu", "mama", "rama"))


if __name__ == '__main__':
    main()