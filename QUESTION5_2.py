def count_pattern_occurrences(text):
    count = 0
    n = len(text)
    for i in range(n):
        if text[i] == "C":
            for j in range(i + 4, n + 1):
                candidate = text[i:j]
                if candidate[-3:] == "jeb":
                    mid = candidate[1:-3]
                    valid = True
                    for ch in mid:
                        if not ((ch >= "A" and ch <= "Z") or (ch >= "a" and ch <= "z")):
                            valid = False
                            break
                    if valid:
                        count += 1
    return count

with open("text.txt") as file:
    text = file.read()

print(count_pattern_occurrences("text.txt"))
