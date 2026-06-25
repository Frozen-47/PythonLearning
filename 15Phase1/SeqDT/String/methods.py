string = "Sabareesh is a programmer"

print("=" * 50)
print("STRING METHODS")
print("=" * 50)


print("\n[CASE CONVERSION]")
print(f"Original   : {string}")
print(f"Upper      : {string.upper()}")
print(f"Lower      : {string.lower()}")
print(f"Swapcase   : {string.swapcase()}")
print(f"Capitalize : {string.capitalize()}")
print(f"Casefold   : {string.casefold()}")


print("\n[SEARCH OPERATIONS]")
print(f"Find 'a'   : {string.find('a')}")
print(f"RFind 'a'  : {string.rfind('a')}")
print(f"Count 'a'  : {string.count('a')}")

print("\n[INDEX OPERATIONS]")

print(f"index('a')  : {string.index('a')}")
print(f"rindex('a') : {string.rindex('a')}")

print("\n[REPLACE]")
print(f"Replace    : {string.replace('programmer', 'Developer')}")


strip_string = "   Sabareesh is a programmer   "

print("\n[STRIP METHODS]")
print(f"Original   : '{strip_string}'")
print(f"strip()    : '{strip_string.strip()}'")
print(f"lstrip()   : '{strip_string.lstrip()}'")
print(f"rstrip()   : '{strip_string.rstrip()}'")

print("\n[OTHER METHODS]")
print(f"Startswith 'Sab' : {string.startswith('Sab')}")
print(f"Endswith 'mer'   : {string.endswith('mer')}")
print(f"Length           : {len(string)}")

print("\n" + "=" * 50)
print("END OF DEMO")
print("=" * 50)