'''
### Commonly Allowed Characters
These characters are broadly accepted across systems and can help create strong, compatible passwords:
1. **Uppercase Letters**: A-Z
2. **Lowercase Letters**: a-z
3. **Digits**: 0-9
4. **Symbols**: ! @ # $ % ^ & * _ - + = ? , . ; : 
---
### Sometimes Allowed Characters
These characters may be allowed in some systems but are frequently restricted in others:
1. **Special Mathematical Symbols**: ~ \
2. **Extended Symbols**: > < [ ]
Occasionally allowed for added complexity, though they might not work on all keyboards.
3. **Extended Punctuation or Typographic Characters**: — – 
Also non-standard characters (such as Unicode or emoji characters)./
---
### Commonly Prohibited Characters
These characters are frequently prohibited due to parsing, encoding, or security concerns:
1. **Whitespace**: (space)
    (Often restricted to avoid accidental leading/trailing spaces and input errors.)
2. **Escape Characters**: \ ' " `
    (These can interfere with encoding and data processing)
3. **Angle Brackets**: < >
    (Often restricted to prevent HTML or XML injection.)
4. **Special Brackets or Braces**: { } [ ]
5. **Path and Command Symbols**: / |

'''


alpha_subs_dict = {
    "a": ["A", "4", "@", "^"],
    "b": ["B", "8", "13", "3"],
    "c": ["C", "(", "<", "{"],
    "d": ["D", "|)", "I>", "[)"],
    "e": ["E", "3", "&"],
    "f": ["F", "|=", "ph"],
    "g": ["G", "6", "9", "&"],
    "h": ["H", "#", "]-[", "|-|", "}{",],
    "i": ["I", "1", "!", "|", "]"],
    "j": ["J", "_|", ";", "]"],
    "k": ["K", "|<", "|{", "X"],
    "l": ["L", "1", "|", "7"],
    "m": ["M", "|v|", "[V]", "^^"],
    "n": ["N", "|||"],
    "o": ["O", "0", "()", "*"],
    "p": ["P", "|*", "|o", "|>"],
    "q": ["Q", "9", "0_", "0,", "(,)"],
    "r": ["R", "12", "|2", "I2"],
    "s": ["S", "5", "$", "z"],
    "t": ["T", "7", "+"],
    "u": ["U", "v", "|_|"],
    "v": ["V", "u", "||"],
    "w": ["W", "vv"],
    "x": ["X", "*", "><", "}{"],
    "y": ["Y", "`/", "'/", "4"],
    "z": ["Z", "2", "7_", ">"]
}




numeric_subs_dict = {
    "0": ["O", "()", "o", "[]"],
    "1": ["I", "|", "!"],
    "2": ["Z", "z", "&"],
    "3": ["E", "e", "]",],
    "4": ["A", "a", "^","|>"],
    "5": ["S", "s", "$"],
    "6": ["G", "b"],
    "7": ["T", "-|", "+", "?"],
    "8": ["B", "&"],
    "9": ["g", "q"]
}


symbols = []