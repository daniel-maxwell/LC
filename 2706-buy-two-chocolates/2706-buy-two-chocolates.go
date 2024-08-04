func buyChoco(prices []int, money int) int {
    slices.Sort(prices)
    if prices[0] + prices[1] > money {
        return money
    } else {
        return money - (prices[0] + prices[1])
    }
}