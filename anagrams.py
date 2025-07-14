Given an array (or list) of strings strs, your task is to group the anagrams together.
An anagram is a word or phrase formed by rearranging the letters of another, typically using all the original letters exactly once. For example, "eat", "tea", and "ate" are anagrams of each other.
The order of the output groups and the order of the strings within each group does not matter.
Input Format:The first line contains an integer N, representing the number of strings in the input array strs.The second line contains N space-separated strings, which are the elements of strs.
Output Format:
Print the groups of anagrams. Each group should be printed on a new line. The strings within each group should be space-separated. The order of the groups and the strings within each group doesn't matterfrom collections import defaultdict

def group_anagrams(strs):
    anagram_groups = defaultdict(list)
    for word in strs:
        key = ''.join(sorted(word))
        anagram_groups[key].append(word)
    for group in anagram_groups.values():
        print(' '.join(group))
n = int(input())
strs = input().split()
group_anagrams(strs)