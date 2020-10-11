print("Please, input a few numbers for creating a list: ")


source_list = list(map(int, input().split()))  # Enter a source list
print(source_list)

def ListReverse(List=source_list) -> list:
    """Function that reverse a list"""
    destination_list = List[::-1]

    return destination_list


if __name__ == "__main__":
    print(ListReverse())
