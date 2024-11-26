import random

def user_turn(stones):
    while True:
        try:
            user_pick = int(input("Ваш ход. Сколько камней вы возьмете? "))
            if user_pick in [1, 2, 3] and user_pick <= stones:
                return user_pick
            else:
                print("Некорректный выбор.")
        except ValueError:
            print("Введите число от 1 до 3.")

def computer_turn(stones):
    if stones % 4 == 0:
        pick = 3
    elif stones % 4 == 3:
        pick = 2
    elif stones % 4 == 2:
        pick = 1
    else:
        pick = random.randint(1, min(3, stones))
    print(f"Компьютер взял {pick} камней.")
    return pick

def play_game():
    stones = random.randint(4, 30)
    print(f"На столе {stones} камней.")

    while stones > 0:
        user_pick = user_turn(stones)
        stones -= user_pick
        print(f"Осталось камней: {stones}")
        if stones == 0:
            print("Компьютер победил.")
            break

        pick = computer_turn(stones)
        stones -= pick
        print(f"Осталось камней: {stones}")
        if stones == 0:
            print("Вы победили.")
            break
            
if __name__ == "__main__":
    play_game()