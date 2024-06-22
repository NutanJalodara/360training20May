def generate_stone_piles(n):
    piles = []
    if n % 2 == 0:
        step = 2
    else:
        step = 1
    current_stones = step
    while current_stones <= n:
        piles.append(current_stones)
        current_stones += 2
    return piles

n = int(input("Enter the number of stones in the first pile: "))
stone_piles = generate_stone_piles(n)
print(f"Stones in each pile: {stone_piles}")
