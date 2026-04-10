def two_timestamp(hr1, min1, sec1, hr2, min2, sec2):
    # Your code here
    hours = (hr1 * 3600) - (hr2 * 3600)
    mins = (min1 * 60) - (min2 * 60)
    sec = sec1 - sec2
    total = hours + mins + sec

    return abs(total)


# Invoke the function and pass two timestamps(6 intergers) as its arguments
print(two_timestamp(1,2,30,1,3,20))
