
def multiply_once(N, M):
    return N * M


def multiply_with_iterations(N, M):
    result = 0
    for _ in range(N):
        result += M
    return result

N = int(input("Enter the value of N: "))
M = int(input("Enter the value of M: "))

print("Multiplication using single iteration:", multiply_once(N, M))
print("Multiplication using N iterations:", multiply_with_iterations(N, M))
