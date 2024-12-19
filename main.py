import periodictable
element_name = input("Enter the element name: ").capitalize()
clcoding = getattr(periodictable, element_name, None)

if clcoding:
    print(f"Element: {clcoding.name}")
    print(f"Symbol: {clcoding.symbol}")
    print(f"Atomic Number: {clcoding.number}")
    print(f"Atomic Weight: {clcoding.mass}")
    print(f"Density: {clcoding.density}")

else:
    print(f"Element '{element_name}' not found.")