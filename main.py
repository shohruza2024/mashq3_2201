# 1
n = 50
match n:
    case _ if n < 0:
        print("Negative")
    case 0:
        print("Zero")
    case _ if 1 <= n <= 10:
        print("1–10")
    case _ if 11 <= n <= 100:
        print("11–100")
    case _:
        print("100+")


# 2
order = {"status": "shipped", "paid": True}
match order:
    case {"status": "shipped", "paid": True}:
        print("Order shipped and paid")
    case {"status": "pending"}:
        print("Order pending")
    case _:
        print("Unknown order status")


# 3
num = 6
match num:
    case 0:
        print("Zero")
    case _ if num % 2 == 0:
        print("Even")
    case _:
        print("Odd")


# 4
command = "ADD 10 20"
cmd, a, b = command.split()
match cmd:
    case "ADD":
        print(int(a) + int(b))
    case "SUB":
        print(int(a) - int(b))
    case _:
        print("Unknown command")


# 5
data = [1, 2, 3]
match data:
    case [a]:
        print(a ** 2)
    case [a, b]:
        print(a + b)
    case [a, b, c]:
        print(a * b * c)
    case _:
        print("Unsupported")
