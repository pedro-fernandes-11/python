from collections import Counter

main_list = [1, 2, 3, 4, 1, 4, 5, 8, 8, 8, 7, 4, 1, 6, 2, 7, 0, 0, 1]
res = Counter(main_list)

print(res)
print(type(res))

string = 'Pedro Pouzada Fernandes'
res_string = Counter(string)

print(res_string)

text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque quis scelerisque velit. " \
        "Mauris ultrices nisi ipsum, sit amet ultrices ante faucibus convallis. Ut facilisis nisl orci, at " \
        "mattis leo tincidunt vitae. Phasellus accumsan quis augue eget condimentum. In sed quam et neque interdum " \
        "fermentum vitae a elit. Phasellus sed dictum dui, eu laoreet nisl. Quisque ligula felis, pellentesque " \
        "scelerisque tortor eu, tincidunt rhoncus lacus. Curabitur sit amet vestibulum eros. Ut ut velit fringilla, " \
        "porttitor odio pretium, vulputate nunc. Etiam rutrum erat tellus, convallis ornare mi fringilla ac."

res = Counter(text.split())
list_each = []
for key in res.keys():
    print(res[key], end=' ')
    if res[key] > 1:
        list_each.append(key)

print(f'\n\nRepetitive words: {list_each}')
print(res.most_common(1))  # Most common word
