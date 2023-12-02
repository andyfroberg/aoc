# --- Day 1: Trebuchet?! ---
# Something is wrong with global snow production, and you've been selected to take a look. The Elves have even given you a map; on it, they've used stars to mark the top fifty locations that are likely to be having problems.

# You've been doing this long enough to know that to restore snow operations, you need to check all fifty stars by December 25th.

# Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

# You try to ask why they can't just use a weather machine ("not powerful enough") and where they're even sending you ("the sky") and why your map looks mostly blank ("you sure ask a lot of questions") and hang on did you just say the sky ("of course, where do you think snow comes from") when you realize that the Elves are already loading you into a trebuchet ("please hold still, we need to strap you in").

# As they're making the final adjustments, they discover that their calibration document (your puzzle input) has been amended by a very young Elf who was apparently just excited to show off her art skills. Consequently, the Elves are having trouble reading the values on the document.

# The newly-improved calibration document consists of lines of text; each line originally contained a specific calibration value that the Elves now need to recover. On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.

# For example:

# 1abc2
# pqr3stu8vwx
# a1b2c3d4e5f
# treb7uchet
# In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.

# Consider your entire calibration document. What is the sum of all of the calibration values?

def part_1():
    full_text = ""
    sum = 0
    with open("1a_input.txt", "r") as f:
        full_text = f.readlines()

    for line in full_text:
        is_first = True
        first_last = [0, 0]
        for i in range(len(line)):
            if line[i].isnumeric() and is_first:
                first_last = [int(line[i]), int(line[i])]
                is_first = False
            elif line[i].isnumeric() and not is_first:  # Keep searching for last num
                first_last[1] = int(line[i])
            else:
                continue
        
        combined = str(first_last[0]) + str(first_last[1])
        sum += int(combined)

    print(sum)

# Your puzzle answer was 53386.

# The first half of this puzzle is complete! It provides one gold star: *

# --- Part Two ---
# Your calculation isn't quite right. It looks like some of the digits are actually spelled out with letters: one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".

# Equipped with this new information, you now need to find the real first and last digit on each line. For example:

# two1nine
# eightwothree
# abcone2threexyz
# xtwone3four
# 4nineeightseven2
# zoneight234
# 7pqrstsixteen
# In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these together produces 281.

# What is the sum of all of the calibration values?

nums_dict = {
        "one": 1, 
        "two": 2, 
        "three": 3, 
        "four": 4, 
        "five": 5, 
        "six": 6, 
        "seven": 7, 
        "eight": 8, 
        "nine": 9
    }

def find_first_letter_or_number(string):
    curr = ""
    for letter in string:
        if letter.isnumeric():
            return letter
        else:
            curr += letter
            for key in nums_dict.keys():
                if key in curr:
                    return str(nums_dict[key])


def find_last_letter_or_number(string):
    curr = ""
    for letter in string[::-1]:
        if letter.isnumeric():
            return letter
        else:
            curr += letter
            for key in nums_dict.keys():
                if key in curr[::-1]:
                    return str(nums_dict[key])

def part_2():
    full_text = ""
    sum = 0

    with open("1a_input.txt", "r") as f:
        full_text = f.readlines()

    for line in full_text:
        fdig = find_first_letter_or_number(line)
        ldig = find_last_letter_or_number(line)
        combined = str(fdig) + str(ldig)
        sum += int(combined)

    print(sum)


if __name__ == "__main__":
    part_1()
    part_2()