package helpers

import (
	"fmt"
	"math"
)

func formatToSignificantFigures(value float64, figures int) string {
	if value == 0 {
		return "0"
	}

	exponent := int(math.Floor(math.Log10(math.Abs(value))))
	decimalPlaces := figures - exponent - 1

	scale := math.Pow10(decimalPlaces)
	rounded := math.Round(value*scale) / scale

	if decimalPlaces < 0 {
		decimalPlaces = 0
	}

	return fmt.Sprintf("%.*f", decimalPlaces, rounded)
}
