package main

import (
	"fmt"
	"errors"
	"lab1/service"
	"lab1/domain"
)

func main() {
	inputService := service.NewInputService()

	var coefficients domain.Coefficients
	var err error

	for {
		coefficients, err = inputService.Get()
		if err != nil {
			fmt.Println(err)
			if errors.Is(err, domain.ErrWrongConsoleInput) {
				break
			}
		} else {
			break
		}
	}
	

	solverService := service.NewSolverService()
	roots, err := solverService.Solve(coefficients)
	if err != nil {
		fmt.Println(err)
		return
	}

	fmt.Printf("Корни: %+v\n", roots)
}
