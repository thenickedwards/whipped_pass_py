'''
### Commonly Allowed Characters
These characters are broadly accepted across systems and can help create strong, compatible passwords:
1. **Uppercase Letters**: A-Z
2. **Lowercase Letters**: a-z
3. **Digits**: 0-9
4. **Symbols**: ! @ # $ % ^ & * _ - + = ? , . ; : ( )
---
### Sometimes Allowed Characters
These characters may be allowed in some systems but are frequently restricted in others:
1. **Special Mathematical Symbols**: ~ \\
2. **Extended Symbols**: > < [ ]
Occasionally allowed for added complexity, though they might not work on all keyboards.
3. **Extended Punctuation or Typographic Characters**: — (em dash) – (en dash)
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

allowed_symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "_", "-", "+", "=", "?", ",", ".", ";", ":", "(", ")"]

commonly_prohibited_chars = ["\\", "|", "/", "—", "–", "~", "<", ">", "{", "}", "[", "]", "'", '"', "`"]

alpha_subs_dict = {
    "a": ["A", "4", "@", "^"],
    "b": ["B", "8", "13", "3"],
    "c": ["C", "("],
    "d": ["D", "!)", "*!", ".!"],
    "e": ["E", "3", "&"],
    "f": ["F", "!=", "ph"],
    "g": ["G", "6", "9", "&"],
    "h": ["H", "#", "!-!", ")-("],
    "i": ["I", "1", "!"],
    "j": ["J", ";"],
    "k": ["K", "!(", "!;", "X"],
    "l": ["L", "1", "!", "7", "("],
    "m": ["M", "!v!", ")V(", "^^"],
    "n": ["N", "!V", ")V"],
    "o": ["O", "0", "()", "*"],
    "p": ["P", "!*", "!o", ")*", ")o"],
    "q": ["Q", "9", "0_", "0,", "(,)"],
    "r": ["R", "12", "!2", "I2", ")2"],
    "s": ["S", "5", "$", "z"],
    "t": ["T", "7", "+"],
    "u": ["U", "v", "!_!"],
    "v": ["V", "u", ")("],
    "w": ["W", "vv"],
    "x": ["X", "*", ")("],
    "y": ["Y", "-;", "-(", "4"],
    "z": ["Z", "2", "7_"]
}

numeric_subs_dict = {
    "0": ["O", "o", "()", "*", "@"],
    "1": ["I", "!", ".", "(", ")"],
    "2": ["Z", "z", ":", "&"],
    "3": ["E", "e", ":.", "&"],
    "4": ["A", "a", "y", "::", "^^"],
    "5": ["S", "s", "$"],
    "6": ["G", "b"],
    "7": ["T", "-!", "-(" "?"],
    "8": ["B", "&"],
    "9": ["g", "q"]
}

words_subs_dict = {
    "you": ["u"],
    "your": ["ur"],
    "are": ["r"],
    "why": ["y"],
    "see": ["c"],
    "be": ["b"],
    "okay": ["ok"],
    "for": ["4"],
    "to": ["2"],
    "too": ["2"],
    "ate": ["8"],
    "one": ["1"],
    "and": ["&", "n"],
    "at": ["@"],
    "oh": ["o"],
    "ex": ["x"],
    "thanks": ["thx", "tnx"],
    "please": ["pls", "plz"],
    "because": ["cuz", "bc"],
    "before": ["b4"],
    "people": ["ppl"],
    "later": ["l8r"],
    "with": ["w!"],
    "without": ["w!o"],
    "great": ["gr8"],
    "laugh out loud": ["lol"],
    "by the way": ["btw"],
    "see you": ["cu"],
    "talk to you later": ["ttyl"],
    "got to go": ["gtg"],
    "what's up": ["wazzup", "sup"]
}



def iterate_through(_dict):
    for k, v in _dict.items():
        print(f"key: {k}")
        for i in v:
            print(f"key: {k}, value: {i}")

# iterate_through(alpha_subs_dict)

def check_for_bad_chars(_dict, bad_chars=commonly_prohibited_chars):
    for k, v in _dict.items():
        # print(f"Checking: {k}")
        issue = 0
        for l in v:                 # iterate through list
            for i in l:             # iterate through string
                if i in bad_chars:
                    print(f"❌ key: {k}, may pose an issue with symbol: {i} in {l}")
                    issue += 1
                    continue
        if issue == 0:
            print(f"✅ key: {k} looks good!")
        else:
            issue = 0

# check_for_bad_chars(alpha_subs_dict)
# check_for_bad_chars(numeric_subs_dict)
check_for_bad_chars(words_subs_dict)