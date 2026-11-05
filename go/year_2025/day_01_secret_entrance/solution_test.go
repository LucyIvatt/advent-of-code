package main

import (
	"testing"

	"github.com/LucyIvatt/advent-of-code/go/helpers"
)

func TestDay01Solutions(t *testing.T) {
	tests := []struct {
		part  helpers.Part
		file  helpers.InputFile
		solve func(helpers.InputFile) int
		want  int
	}{
		{
			part:  helpers.P1,
			file:  helpers.Example,
			solve: partOne,
			want:  3,
		},
		{
			part:  helpers.P1,
			file:  helpers.Input,
			solve: partOne,
			want:  1145,
		},
		{
			part:  helpers.P2,
			file:  helpers.Example,
			solve: partTwo,
			want:  0,
		},
		{
			part:  helpers.P2,
			file:  helpers.Input,
			solve: partTwo,
			want:  0,
		},
	}

	for _, tt := range tests {
		testName := string(tt.part) + "_" + string(tt.file)

		t.Run(testName, func(t *testing.T) {
			if got := tt.solve(tt.file); got != tt.want {
				t.Errorf("%s(%s) = %d; want %d",
					tt.part,
					tt.file,
					got,
					tt.want,
				)
			}
		})
	}
}

func TestRotateDialPositions(t *testing.T) {
	tests := []struct {
		name        string
		currentPos  int
		instruction string
		expected    int
	}{
		{"basic left turn", 50, "L5", 45},
		{"basic right turn", 50, "R5", 55},
		{"left turn over boundary", 50, "L51", 99},
		{"right turn over boundary", 50, "R50", 0},
		{"numerous left turn over boundary", 0, "L100", 0},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := rotateDial(tt.currentPos, tt.instruction)

			if result != tt.expected {
				t.Errorf("rotateDial(%d, %s) = %d; want %d",
					tt.currentPos, tt.instruction, result, tt.expected)
			}
		})
	}
}

func TestRotateDialPanicsForInvalidDirection(t *testing.T) {
	defer func() {
		recovered := recover()

		if recovered == nil {
			t.Fatal("expected rotateDial to panic")
		}

		if got, want := recovered, "invalid direction: X"; got != want {
			t.Fatalf("panic value = %v, want %v", got, want)
		}
	}()

	rotateDial(50, "X10")
}
