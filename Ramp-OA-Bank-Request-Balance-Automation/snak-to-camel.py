import re

def solution(src: str) -> str:
    def to_camel(match):
        prefix, core, suffix = match.groups()
        camel_case = core.split('_')
        camel_case = camel_case[0] + ''.join(word.capitalize() for word in camel_case[1:])
        return f"{prefix}{camel_case}{suffix}"
    
    pattern = r"(\_*)([a-z]+(?:_[a-z]+)*)(\_*)"
    return re.sub(pattern, to_camel, src)

# Example usage
src = "_this_is_a_test _another_example_ example_with__multiple_underscores_"
print(solution(src))
