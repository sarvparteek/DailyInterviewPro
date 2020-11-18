# Daily Interview Pro problem for Nov 17, 2020
# There are n people lined up, and each have a height represented as an integer. A murder has happened right in front
# of them, and only people who are taller than everyone in front of them are able to see what has happened. How many
# witnesses are there?
#
# Example:
# Input: [3, 6, 3, 4, 1]
# Output: 3
# Explanation: Only [6, 4, 1] were able to see in front of them.
#    #
#    #
#    # #
#   ####
#   ####
#   #####
#   36341                                 x (murder scene)

__author__ = 'sarvps'

'''
Author: Sarv Parteek Singh (sarvparteek@gmail.com)
Daily Interview Pro problem for Nov 17, 2020
Date: Nov 17, 2020
Brief: Finds the number of witnesses arranged in a decreasing order of heights '''


def update_witness_list(w_list, person):
    # If there is no existing witness, or if the new person is shorter than the last witness in the list, then the list
    # is up to date after the inclusion of this new person
    if not w_list or person < w_list[-1]:
        w_list.append(person)
        return True
    else:  # if the new person is taller than the last witness in the list, then remove that witness
        del w_list[-1]
        return False


def witnesses(heights):
    assert len(heights) > 0, "No witness available"
    witness_list = []
    for i in heights:
        while not update_witness_list(witness_list, i):
            continue

    print("Full list: ", heights)
    print("Witness list: ", witness_list)
    print("Number of witnesses: ", len(witness_list), "\n")


witnesses([3, 6, 4, 1])  # Expected: [6, 4, 1] = 3 witnesses
witnesses([4, 3, 5, 2, 6, 1, 4, 3, 1, 2, 1])  # Expected: [6, 4, 3, 2, 1] = 5 witnesses
witnesses([4]) # Expected: [4] = 1 witness
witnesses([3, 3, 3, 3, 2]) # Expected: [3, 2] = 2 witnesses