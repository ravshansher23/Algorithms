from memory_profiler import profile


# Код из 2 урока, проблема возникает в том, что профилируется только декоратор. Я решил эту проблему обернув код в функцию.
@profile
def cn():
    def ascii(i=32):
        if i > 121:
            return print(
                f'{i}\t{chr(i)},{i + 1}\t{chr(i + 1)},{i + 2}\t{chr(i + 2)},{i + 3}\t{chr(i + 3)},{i + 4}\t{chr(i + 4)},{i + 5}\t{chr(i + 5)}')
        else:
            print(
                f'{i}\t{chr(i)},{i + 1}\t{chr(i + 1)},{i + 2}\t{chr(i + 2)},{i + 3}\t{chr(i + 3)},{i + 4}\t{chr(i + 4)},{i + 5}\t{chr(i + 5)},{i + 6}\t{chr(i + 6)},{i + 7}\t{chr(i + 7)},{i + 8}\t{chr(i + 8)},{i + 9}\t{chr(i + 9)}')
            i += 10
            ascii(i)
    return ascii()

print(cn())