package helpers

import (
	"fmt"
	"time"
)

func (file InputFile) Filename() string {
	return string(file) + ".txt"
}

const divider = "--------------------------------------"

func TimeFunction[T any](fn func() T) (T, time.Duration) {
	start := time.Now()
	result := fn()

	return result, time.Since(start)
}

func RunDay[Answer1 any, Answer2 any](
	title string,
	partOne func(InputFile) Answer1,
	partTwo func(InputFile) Answer2,
) {
	fmt.Println(divider)
	fmt.Println(title)
	fmt.Println(divider)

	inputFiles := []InputFile{Example, Input}

	for i, inputFile := range inputFiles {
		p1, p1Time := TimeFunction(func() Answer1 {
			return partOne(inputFile)
		})

		p2, p2Time := TimeFunction(func() Answer2 {
			return partTwo(inputFile)
		})

		sectionSeparator := ""

		if i < len(inputFiles)-1 {
			sectionSeparator = "\n"
		}

		fmt.Printf("[%s]\n", inputFile)
		fmt.Printf(
			"Part One Answer: %v - [%v seconds]\n",
			p1,
			formatToSignificantFigures(p1Time.Seconds(), 3),
		)
		fmt.Printf(
			"Part Two Answer: %v - [%v seconds]%s\n",
			p2,
			formatToSignificantFigures(p2Time.Seconds(), 3),
			sectionSeparator,
		)
	}

	fmt.Println(divider)
}
