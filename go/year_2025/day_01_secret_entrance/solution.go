package main

import (
	"fmt"
	"strconv"

	"github.com/LucyIvatt/advent-of-code/go/helpers"
)

const dialSize = 100

func rotateDial(currentPosition int, instruction string) int {
	turnAmount, err := strconv.Atoi(instruction[1:])
	if err != nil {
		panic(err)
	}

	switch instruction[0] {
	case 'L':
		turnAmount = -turnAmount

	case 'R':
	default:
		panic("invalid direction: " + string(instruction[0]))
	}

	return ((currentPosition+turnAmount)%dialSize + dialSize) % dialSize
}

func solveP1() int {
	input := helpers.InputLines("input.txt")

	currentPosition := 50
	password := 0

	for _, instruction := range input {
		currentPosition = rotateDial(currentPosition, instruction)

		if currentPosition == 0 {
			password++
		}
	}

	return password
}

func main() {
	fmt.Println("password:", solveP1())
}
