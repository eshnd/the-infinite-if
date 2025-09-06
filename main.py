with open("infinite_if.py", "w") as f:
    f.write("num = input('What is your number?: ')\nif abs(int(num)) == 0:\n  print('even')")

idx = 1
try:
    while True:
        with open("infinite_if.py", "r") as f:
            data = f.read()
        data += f"\nelif abs(int(num)) == {idx}:\n  print('{'even' if idx % 2 == 0 else 'odd'}')"
        with open("infinite_if.py", "w") as f:
            f.write(data)
        idx += 1
except:
    print(f"max number: {idx - 1}")
