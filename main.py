print("Please, input a few numbers for creating a list: ")
l0 = list(map(int, input().split()))
print(l0)

def ListReverse(List = l0):
    l1 = l0[::-1]
    return l1

if __name__ == "__main__":
    print(ListReverse())