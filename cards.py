import random

cards = ['Ace', 'Jack', 'King', 'Queen', 'Spade', 'Hearts', 'Cloves', 'Diamonds']
score = 0
for x in range(10):
    random.shuffle(cards)
    print(cards[0])
    random.shuffle(cards)

    answer = input('Guess the first card : ')
    if answer == cards[0]:
        score += 2
        print('You guessed right.The answer is ', cards[0])

    else:
        print('Ooops,you are wrong.The aswer is', cards[0])

if score > 14:
    print('Nice work!,Your score is', score)
elif score > 7:
    print('Fair play. You scored', score)
else:
    print('Better Luck Next time.', score)