package service

import (
	"lab1/domain"
	"math"
)

type SolverService struct{}

func NewSolverService() *SolverService {
	return &SolverService{}
}

func (s *SolverService) Solve(coefficients domain.Coefficients) ([]float64, error) {
	rootSet := map[float64]struct{}{}

	d := math.Pow(coefficients.B, 2) - 4*coefficients.A*coefficients.C
	if d < 0 {
		return []float64{}, domain.ErrNoSolutions
	}

	possibleRoots := []float64{
		(-coefficients.B - math.Sqrt(d)) / (2 * coefficients.A),
		(-coefficients.B + math.Sqrt(d)) / (2 * coefficients.A),
	}

	for _, root := range possibleRoots {
		if root < 0 {
			continue
		}

		rootSet[-math.Sqrt(root)] = struct{}{}
		rootSet[math.Sqrt(root)] = struct{}{}
	}

	roots := make([]float64, 0, len(rootSet))
	for root := range rootSet {
		roots = append(roots, root)
	}

	return roots, nil
}
