import math


def main() -> None:
    print("To'g'ri burchakli uchburchak: katetlarni kiriting.")
    try:
        a = float(input("a: "))
        b = float(input("b: "))
    except ValueError:
        print("Noto'g'ri son.")
        return
    c = math.hypot(a, b)
    area = a * b / 2
    print(f"Gipotenuza: {c:.3f}")
    print(f"Yuza: {area:.3f}")


if __name__ == "__main__":
    main()


