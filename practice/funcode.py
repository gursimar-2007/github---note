import math
import time

print("=" * 60)
print(" MASSIVE COMPUTATION DEMO ")
print("=" * 60)

start = time.time()

result = 0

for outer in range(1, 10001):

    subtotal = 0

    for middle in range(1, 500):

        value = middle

        for inner in range(1, 200):

            value = (
                value * value
                + inner * outer
                + middle
            ) % 1000003

            subtotal += (
                value
                ^ (inner * outer)
            ) % 997

        subtotal %= 10000019

    result ^= subtotal

    if outer % 100 == 0:
        elapsed = time.time() - start
        print(
            f"Completed {outer}/10000 iterations "
            f"| Result={result} "
            f"| Time={elapsed:.2f}s"
        )

print("\nBeginning second computation phase...\n")

total = 0.0

for i in range(1, 500000):

    total += (
        math.sin(i)
        * math.cos(i / 2)
        * math.sqrt(i)
    )

    if i % 50000 == 0:
        print(f"Processed {i:,} values")

print("\nThird computation phase...\n")

checksum = 0

for a in range(2500):
    for b in range(150):
        checksum ^= (
            (a * b)
            + (a << 2)
            - (b << 1)
        ) & 0xFFFFFFFF

end = time.time()

print("=" * 60)
print("Finished!")
print("Checksum:", checksum)
print("Floating Total:", total)
print("Result:", result)
print(f"Execution Time: {end-start:.2f} seconds")
print("=" * 60)