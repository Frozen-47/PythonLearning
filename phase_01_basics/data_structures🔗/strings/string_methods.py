text = "Sabareesh is a programmer"

print("=" * 50)
print("STRING METHODS")
print("=" * 50)

print(f"Length           : {len(text)}")

print("\n[CASE CONVERSION]")
print(f"Original   : {text}")
print(f"Upper      : {text.upper()}")
print(f"Lower      : {text.lower()}")
print(f"Swapcase   : {text.swapcase()}")
print(f"Capitalize : {text.capitalize()}")
print(f"Title      : {text.title()}")
print(f"Casefold   : {text.casefold()}")

print("\n[SEARCH OPERATIONS]")
print(f"Find 'a'   : {text.find('a')}")
print(f"RFind 'a'  : {text.rfind('a')}")
print(f"Count 'a'  : {text.count('a')}")
print(f"Startswith : {text.startswith('Sab')}")
print(f"Endswith   : {text.endswith('er')}")

print("\n[INDEX OPERATIONS]")
try:
    print(f"index('a')  : {text.index('a')}")
    print(f"rindex('a') : {text.rindex('a')}")
except ValueError:
    pass

print("\n[REPLACE & PADDING]")
print(f"Replace    : {text.replace('programmer', 'Developer')}")
print(f"RemovePrefix: {text.removeprefix('Sabareesh ')}")
print(f"RemoveSuffix: {text.removesuffix(' programmer')}")
print(f"Center     : {text.center(40, '*')}")
print(f"Ljust      : {text.ljust(40, '-')}")
print(f"Rjust      : {text.rjust(40, '-')}")
print(f"Zfill      : {'42'.zfill(5)}")

spaced_text = "   Sabareesh is a programmer   "

print("\n[STRIP METHODS]")
print(f"Original   : '{spaced_text}'")
print(f"strip()    : '{spaced_text.strip()}'")
print(f"lstrip()   : '{spaced_text.lstrip()}'")
print(f"rstrip()   : '{spaced_text.rstrip()}'")

print("\n[SPLIT & JOIN METHODS]")
words = text.split()
print(f"Split      : {words}")
print(f"Join(-)    : {'-'.join(words)}")
print(f"Partition  : {text.partition('is')}")

print("\n[ISALPHA, ISDIGIT, ISALNUM, ISLOWER, ISUPPER, ISSPACE, ISTITLE METHODS]")
s1 = "sabareesh"
print(f"isalpha {s1}      : {s1.isalpha()}")
s2 = "sabar12"
print(f"isalpha {s2}      : {s2.isalpha()}")
print(f"isalnum {s2}      : {s2.isalnum()}")
s3 = "123"
print(f"isdigit {s3}      : {s3.isdigit()}")
s4 = "   "
print(f"isspace {s4}      : {s4.isspace()}")
s5 = "SABAREESH"
print(f"islower {s1}      : {s1.islower()}")
print(f"isupper {s5}      : {s5.isupper()}")
s6 = "Sabareesh Is"
print(f"istitle {s6}      : {s6.istitle()}")
s7 = "var_name"
print(f"isidentifier {s7} : {s7.isidentifier()}")

print("=" * 50)