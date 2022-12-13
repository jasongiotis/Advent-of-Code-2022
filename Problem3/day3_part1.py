# list of all alphabet letters
import string

def common_letter(str1,str2):
    for i in str1:
        if i in str2:
            return i



if __name__ == '__main__':
    alphabet_lower = list(string.ascii_lowercase)
    alphabet_upper = list(string.ascii_uppercase)
    keys = alphabet_lower + alphabet_upper
    letter_dict = dict(zip(keys, range(1, 53)))
    with open('input.txt') as f:
        data = f.read().splitlines()
        total_score=0
        for element in data:
            str1=element[0:len(element)/2]
            str2=element[-len(element)/2:]
            total_score+=letter_dict[common_letter(str1,str2)]
        print("Total score is ",total_score)   

