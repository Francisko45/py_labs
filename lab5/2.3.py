cities = ['Budapest', 'Rome', 'Istanbul', 'Sydney', 'Kiev', 'Hong Kong']
message = ", ".join(cities[:-1]) + " and " + cities[-1]
print("Повідомлення:", message)
longest = max(cities, key=len)
print("Найдовша назва міста:", longest)
