'''
Author: Sarv Parteek Singh (sarvparteek@gmail.com)
Source: https://towardsdatascience.com/10-algorithms-to-solve-before-your-python-coding-interview-feb74fb9bc27
Date: Jan 31, 2021
Brief: Provides the average word length for a given sentence
'''

def findAvgWordLength(string):
    word_lengths = []
    length = 0
    for i, v in enumerate(string):
        if isPunctuation(v) or v == " ": # Do not consider punctuations
            word_lengths.append(length)
            length = 0
        else:
            length += 1

    word_lengths = [item for item in word_lengths if item > 0]
    print(word_lengths)
    return round(sum(word_lengths)/len(word_lengths), 2)

def isPunctuation(v):
    return True if v in [",", "'", "?", "!", "(", ")", ";", "-", ":", "."] else False

if __name__ == "__main__":
    string = "Hello! I've been waiting for so long, right?"
    print("For [", string, "], the average word length is ", findAvgWordLength(string), "\n")

    string = "Hi all, my name is Tom...I am originally from Australia."
    print("For [", string, "], the average word length is ", findAvgWordLength(string), "\n")

    string = "I need to work very hard to learn more about algorithms in Python!"
    print("For [", string, "], the average word length is ", findAvgWordLength(string), "\n")
