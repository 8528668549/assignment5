def permutations(remaining, candidate=' '):
    if len(remaining) == 0:
        print(candidate)

    for i in range(len(remaining)):
        newcandidate = candidate + remaining[i]
        newremaining = remaining[0:i] + remaining[i + 1:]

        permutations(newremaining, newcandidate)


if __name__ == '__main__':
    s = 'SRG'
    permutations(s)