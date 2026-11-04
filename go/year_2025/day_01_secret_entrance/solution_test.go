package main

import (
	"testing"
)

func TestRotateDial(t *testing.T) {
    tests := []struct {
        name     string
        currentPos int
        instruction string
        expected int
    }{
        {"basic left turn", 50, "L5", 45},
        {"basic right turn", 50, "R5", 55},
        {"left turn over boundary", 50, "L51", 99 },
        {"right turn over boundary", 50, "R50", 0 },
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