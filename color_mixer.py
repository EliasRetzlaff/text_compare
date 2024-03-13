# text_compare.py
# Written by Elias Retzlaff

import math

import string

stem_list = ["s", "ing", "ed", "ly"]

stop_list = { "the", "a", "to", "and", "of", "in", "it", "that", "for", "so", 

             "am", "is", "are", "was", "be", "were", "been", "being", "from", "by",

             "as", "with", "not", "was", "on", "at", "its", "but", "have", "has",

             "had" }

files = ['docs/BellowAugieMarch.txt', 'docs/wizard_of_oz.txt', 'docs/moby_dick.txt',

         'docs/alice_in_wonderland.txt', 'docs/SinclairJungle.txt',

         'docs/tale_of_two_cities.txt', 'docs/frankenstein.txt', 'docs/dracula.txt',

         'docs/udolpho.txt', 'docs/pride_and_prejudice.txt',

         'docs/WilkersonWarmthofOtherSuns.txt', 'docs/jane_eyre.txt']

def clean_word(word):

    word = word.strip(string.punctuation)

    word = word.lower()

    word = stem(word)

    return word

def stem(word):

    for suffix in stem_list:

        if word.endswith(suffix) and len(word) / len(suffix) > 3:

            return word[0:-len(suffix)]

    return word

def count_word(word_table, item):

    word = clean_word(item)

    if word in word_table:

        word_table[word] = word_table[word] + 1

    else:

        word_table[word] = 1

def similarity(tableA, tableB):

    words = set(tableA.keys()).union(tableB.keys())

    

    ab = 0

    a2 = 0

    b2 = 0

    for w in words:

        ab += tableA.get(w, 0) * tableB.get(w, 0)

        a2 += tableA.get(w, 0) * tableA.get(w, 0)

        b2 += tableB.get(w, 0) * tableB.get(w, 0)

    return ab / (math.sqrt(a2) * math.sqrt(b2))

def display_counts(file_name):

    fd = open(file_name, 'r', encoding="utf8")

    word_list = fd.read().split()

    word_table = dict()

    for word in word_list:

        count_word(word_table, word)

    print(f"The word 'dance' appears {word_table.get('dance', 0)} times!")

    fd.close()

def display_counts2(file_name, search_list):

    fd = open(file_name, 'r', encoding="utf8")

    word_list = fd.read().split()

    word_table = dict()

    for word in word_list:

        count_word(word_table, word)

        

    for w in search_list:

        print(f"The word '{w}' appears {word_table.get(w, 0)} times!")

    fd.close()

def display_counts3(file_name, search_list):

    fd = open(file_name, 'r', encoding="utf8")

    word_list = fd.read().split()

    num_words = len(word_list)

    word_table = dict()

    for word in word_list:

        count_word(word_table, word)

        

    for w in search_list:

        print(f"The word '{w}' appears {word_table.get(w, 0) / num_words *100} % times!")

    fd.close()

def display_counts4(search_word):

    for file_name in files:

        word_table = get_word_table(file_name)

        print(f"Counts for file: {file_name}")

        print(f"The word '{search_word}' appears {word_table.get(search_word, 0)} times!\n")

    

def get_word_table(file_name):

    fd = open(file_name, 'r', encoding="utf8")

    word_list = fd.read().split()

    word_table = dict()

    for word in word_list:

        count_word(word_table, word)

    fd.close()

    return word_table

def compare_text(fname1, fname2):

    sim_score = similarity(get_word_table(fname1), get_word_table(fname2))

    return sim_score

def recommend_text(query_file):

    max_similarity = 0

    recommended_file = ""

    for file in files:

        if file == query_file:

            continue

        similarity_score = compare_text(query_file, file)

        if similarity_score > max_similarity:

            max_similarity = similarity_score

            recommended_file = file

    print(f"The recommended file for '{query_file}' is '{recommended_file}'")

    print()

    return recommended_file

    

def best_pair():

    max_similarity = 0

    best_pair = ()

    for i in range(len(files)):

        for j in range(i + 1, len(files)):

            similarity_score = compare_text(files[i], files[j])

            if similarity_score > max_similarity:

                max_similarity = similarity_score

                best_pair = (files[i], files[j])

    return best_pair

def count_word2(word_table, item):

    word = clean_word(item)

    if word not in stop_list:

        if word in word_table:

            word_table[word] += 1

        else:

            word_table[word] = 1
