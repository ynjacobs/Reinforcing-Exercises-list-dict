ballots = [{'gold': 'Smudge', 'silver': 'Tigger', 'bronze': 'Simba'},
           {'gold': 'Bella', 'silver': 'Lucky', 'bronze': 'Tigger'},
           {'gold': 'Bella', 'silver': 'Boots', 'bronze': 'Smudge'},
           {'gold':'Boots', 'silver': 'Felix', 'bronze': 'Bella'},
           {'gold': 'Lucky', 'silver': 'Felix', 'bronze': 'Bella'},
           {'gold': 'Smudge', 'silver': 'Simba', 'bronze': 'Felix'}]

names = set()

def calc(total, name, key):
    if key == 'gold':
        total += 3
    elif key == 'silver':
        total += 2
    else:
        total += 1
    return total

# names = list(map(lambda x: names.append(x), ballots.pop().values()))
# print(names)

# zip(ballots)




# names.append([ball.values() for ball in ballots])
# print(names)

for items in ballots:
    for value in items.values():
        names.add(value)



# print(names)
score = []

for name in names:
    counter=0
    for items_dict in ballots:
        for key, value in items_dict.items():
            # print(name, '||', value, '||', key)
            if name == value:
                counter = calc(counter, name, key)
    score.append([name, counter])
 
# score.sort()
print('score:',score)

# score:: [{'Lucky': 5}, {'Boots': 5}, {'Smudge': 7}, {'Simba': 3}, {'Felix': 5}, {'Tigger': 3}, {'Bella': 8}]

score = sorted(score, key=lambda k: k[1], reverse= True)
print('winner is:',score[0])