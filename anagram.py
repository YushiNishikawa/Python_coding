def count_charactors(par_string):
    count_dict = {}
    for char in par_string:
        if char in count_dict:
            count_dict[char] += 1
        else:
            count_dict[char] = 1

    print(count_dict)


def anagram(par_str1: str, par_str2: str):
    par_str1 = par_str1.lower()
    par_str2 = par_str2.lower()
    return sorted(par_str1) == sorted(par_str2)


count_charactors("Dynasty")
print(anagram("iceman", "cinema"))
print(anagram("tree", "leaf"))
