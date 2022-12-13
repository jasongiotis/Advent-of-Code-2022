
def decode_input(result):
    if result=="X":
        return ("A",1)
    elif result=="Y":
        return ("B",2)
    elif result=="Z":
        return ("C",3)

def grading_func(result1,result2):
    score=0
    res2=decode_input(result2)[0]
    score+=decode_input(result2)[1]
    if result1==res2 :
        score+=3
        return score
    if result1=="A" and res2=="B" :
        score+=6
        return score
    elif result1=="B" and res2=="C" :
        score+=6
        return score
    elif result1=="C" and res2=="A" :
        score+=6
        return score
    else:
        return score


    
if __name__ == "__main__":
    with open('input.txt') as f:
        data = f.read().splitlines()
        total_score=0
        for element in data:
            element=element.split(" ")
            total_score+=grading_func(element[0],element[1])
        print("Total score is ",total_score)

       
    