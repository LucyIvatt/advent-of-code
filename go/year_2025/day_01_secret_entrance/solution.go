package main

import (
	"fmt"
	"strconv"

	"github.com/LucyIvatt/advent-of-code/go/helpers"
)

func rotateDial(currentPosition int, instruction string) int {
	var nextPos int;
	direction := string(instruction[0])
	turnAmount, err := strconv.Atoi(instruction[1:])
	if err != nil {
			panic(err)
	}

	if direction == "L"{
	newPos := (currentPosition - turnAmount)%100

	if newPos < 0 {
		nextPos = 100 + newPos
	} else {
		nextPos = newPos
	}
	
	} else {
		newPos := (currentPosition + turnAmount)
		nextPos = newPos%100;
	}

	return nextPos
}

func p1() {
	input := helpers.InputLines("input.txt")

	currentPos := 50
	password := 0

	for _, element := range input {
		currentPos = rotateDial(currentPos, element)

		if (currentPos == 0) {password++}

		fmt.Println("current pos", currentPos)
	}
	fmt.Println("password", password)
}


func main() {
	p1()
}