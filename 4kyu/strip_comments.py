# Given an input string of:

# apples, pears # and bananas
# grapes
# bananas !apples
# The output expected would be:

# apples, pears
# grapes
# bananas

def strip_comments(text, markers):
    lines = text.split("\n")
    result = []
    
    for line in lines:
        for marker in markers:
            if marker in line:
                line = line.split(marker)[0]  
        result.append(line.rstrip())     
    return "\n".join(result)