package main

import (
	"fmt"
	"lab1/service"
)

func main() {
	inputService := service.NewInputService()
	coefficients, err := inputService.Get()
	if err != nil {
		fmt.Println(err)
		return
	}

	solverService := service.NewSolverService()
	roots, err := solverService.Solve(coefficients)
	if err != nil {
		fmt.Println(err)
		return
	}

	fmt.Printf("Корни: %+v\n", roots)
}
