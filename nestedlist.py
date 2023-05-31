if __name__ == '__main__':
    data = []
    lowest = float('inf')
    runnerUP = float('inf')
    for _ in range(int(input())):
        name = input()
        score = float(input())
        if score<lowest and score != lowest:
            runnerUP = lowest
            lowest = score
        elif (score>lowest and score <runnerUP or runnerUP == lowest):
            runnerUP = score
        data.append([name, score])
    secondLowerStudents  = []
    for _data in data:
        if _data[1] == runnerUP:
            secondLowerStudents.append(_data[0])
    for i in sorted(secondLowerStudents):
        print(i)