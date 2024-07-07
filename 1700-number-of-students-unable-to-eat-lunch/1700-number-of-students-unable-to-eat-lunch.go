func countStudents(students []int, sandwiches []int) int {
    ptr, refusals := 0, 0
    
    for ptr < len(sandwiches) {
        if sandwiches[ptr] == students[0] {
            ptr++
            refusals = 0
        } else {
            refusals++
            students = append(students, students[0])
        }

        students = students[1:]

        if refusals == len(students) {
            break
        }
    }
    return len(students)
}