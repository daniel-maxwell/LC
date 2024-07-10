func timeRequiredToBuy(tickets []int, k int) int {
    continuous := true
    i := 0
    time := 0

    for continuous {
        if i == len(tickets) {
            i = 0
            continue
        }
        if tickets[i] == 0 {
            i++
            continue
        } else {
            tickets[i]--
            time++
        }
        if i == k && tickets[i] == 0 {
            break
        }
        i++
    }
    return time
}