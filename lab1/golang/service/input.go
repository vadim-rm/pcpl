package service

import (
	"fmt"
	"lab1/domain"
	"os"
	"strconv"
)

type InputService struct{}

func NewInputService() *InputService {
	return &InputService{}
}

func (_ *InputService) parseFloatFromString(input string) (float64, error) {
	value, err := strconv.ParseFloat(input, 64)

	if err != nil {
		return 0, domain.ErrWrongInput
	}

	return value, nil
}

func (s *InputService) getCoefficients(input domain.Input) (output domain.Coefficients, err error) {
	output.A, err = s.parseFloatFromString(input.A)
	if err != nil {
		return
	}

	if output.A == 0 {
		return
	}

	output.B, err = s.parseFloatFromString(input.B)
	if err != nil {
		return
	}

	output.C, err = s.parseFloatFromString(input.C)
	if err != nil {
		return
	}

	return
}

func (s *InputService) Get() (domain.Coefficients, error) {
	var input domain.Input

	if len(os.Args) > 3 {
		input.A = os.Args[1]
		input.B = os.Args[2]
		input.C = os.Args[3]
	} else {
		fmt.Print("Введите коэффициенты через пробел: ")
		_, err := fmt.Scanf("%s %s %s", &input.A, &input.B, &input.C)
		if err != nil {
			return domain.Coefficients{}, err
		}
	}

	coefficients, err := s.getCoefficients(input)
	if err != nil {
		return domain.Coefficients{}, err
	}
	return coefficients, nil
}
