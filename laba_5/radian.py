import math


def get_angle():
    while True:
        try:
            angle = float(input("Введите угол в градусах: "))
            return angle
        except ValueError:
            exit("Угол должен быть числом. Попробуйте снова.")


def convert(angle_deg):
    return math.radians(angle_deg)


def calculate_rad(angle_rad):
    siny = math.sin(angle_rad)
    cosy = math.cos(angle_rad)
    if angle_rad % (math.pi / 2) == 0 and angle_rad % math.pi != 0:
        tany = float('inf')
    else:
        tany = math.tan(angle_rad)
    return siny, cosy, tany


def res(siny, cosy, tany):
    print(f"Синус: {siny}")
    print(f"Косинус: {cosy}")
    print(f"Тангенс: {tany}")


def main():
    angle_deg = get_angle()
    angle_rad = convert(angle_deg)
    siny, cosy, tany = calculate_rad(angle_rad)
    res(siny, cosy, tany)


if __name__ == "__main__":
    main()