class StringUtility:
    def __init__(self, string):
        self.string = string

    def __str__(self):
        return self.string

    def vowels(self):
        vowel_count = sum(1 for char in self.string if char.lower() in 'aeiou')
        return 'many' if vowel_count >= 5 else str(vowel_count)

    def bothEnds(self):
        if len(self.string) <= 2:
            return ''
        return self.string[:2] + self.string[-2:]

    def fixStart(self):
        if len(self.string) <= 2:
            return ''
        else:
         return self.string[0] + self.string[1:].replace(self.string[0], '*')

    def asciiSum(self):
        return sum(ord(char) for char in self.string)

    def cipher(self):
        shift = len(self.string)
        result = ''
        for char in self.string:
            if char.isalpha():
                shifted_char = chr((ord(char.lower()) - ord('a') + shift) % 26 + ord('a'))
                result += shifted_char.upper() if char.isupper() else shifted_char
            else:
                result += char
        return result