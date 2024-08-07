func minEatingSpeed(piles []int, h int) int {

    maxPile := 0
    for _, val := range piles {
        if val > maxPile { maxPile = val }
    }

    lowerBound := (len(piles) + h - 1) / h
    upperBound := maxPile * len(piles)

    checkSpeed := func(speed int) bool {
        hoursRemaining := h
        for i := 0; i < len(piles); i++ {
            if hoursRemaining <= 0 {
                return false
            }
            hoursRemaining -= (piles[i] + speed - 1) / speed
        }
        if hoursRemaining < 0 {
            return false
        } else {
            return true
        }
    }

    for lowerBound <= upperBound {
        mid := lowerBound + ((upperBound - lowerBound) / 2)
        if checkSpeed(mid) {
            upperBound = mid - 1
        } else {
            lowerBound = mid + 1
        }
    }

    return lowerBound
}