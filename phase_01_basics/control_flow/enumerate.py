winners = ["Goku","Saitama","Naruto"]

for i in enumerate(winners,start=1):
    print(i)
# Tuple unpacking
for position , name in enumerate(winners,start=1):
    print(f"{position}) {name}")