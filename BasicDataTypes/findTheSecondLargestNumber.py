if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    curr_max = max(arr)
    arr = [val for val in arr if val!=curr_max]
    second_max = max(arr)
    print second_max