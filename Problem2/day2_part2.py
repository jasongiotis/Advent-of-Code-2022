

def decode(result1,result2):
    win_dict={"A":"C","B":"A","C":"B"}
    lose_dict={"A":"B","B":"C","C":"A"}
    score_dict={"A":1,"B":2,"C":3}
    score=0
    if result2=="X":
        score+=score_dict[win_dict[result1]]
        return score
    elif result2=="Y":
        score+=score_dict[result1]+3
        return score
    else:
        score+=score_dict[lose_dict[result1]]+6
        return score

    
if __name__ == "__main__":
    with open('input.txt') as f:
        data = f.read().splitlines()
        total_score=0
        for element in data:
            element=element.split(" ")
            total_score+=decode(element[0],element[1])
        print("Total score is ",total_score)