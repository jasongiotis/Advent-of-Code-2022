

with open('input.txt') as f:
    data = f.read().splitlines()
    max = 0
    elf_number=1
    sum=0
    for element in data:
        if element=='':
            if sum>max:
                max=sum
            elf_number+=1
            best_elf=elf_number
            sum=0
        else:
            sum+=int(element)
    print("Winner is elf ",best_elf,"  with a total of ",max ,"  calories")
       
