def strcounter(s):
    for sym in set(s):
        counter = 0
        for sub_sym in s:
            if sub_sym == sym:
                counter += 1
        print(sym, " - ", counter)

strcounter(";oisrgel;rng;we")

print("-------------------------\n-------------------------")

def strcounter2(s):
    syms_counter = {}
    for sym in s:
        syms_counter[sym] = syms_counter.get(sym, 0) + 1
    for sym, count in syms_counter.items():
        print(sym, " - ", count)

strcounter2(';oisrgel;rng;we')