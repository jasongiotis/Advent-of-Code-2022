# list of all alphabet letters
import string

def common_letter(str1,str2,str3):
    for i in str1:
        if i in str2 and i in str3:
            return i



if __name__ == '__main__':
    alphabet_lower = list(string.ascii_lowercase)
    alphabet_upper = list(string.ascii_uppercase)
    keys = alphabet_lower + alphabet_upper
    letter_dict = dict(zip(keys, range(1, 53)))
    with open('input.txt') as f:
        data = f.read().splitlines()
        total_score=0
        index=0
        for i in range(len(data)/3):
            str1=data[index]
            str2=data[index+1]
            str3=data[index+2]
            index+=3
            total_score+=letter_dict[common_letter(str1,str2,str3)]
        print("Total score is ",total_score)   

