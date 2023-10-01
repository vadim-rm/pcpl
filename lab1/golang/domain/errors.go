package domain

import "errors"

var (
	ErrWrongInput  = errors.New("Неверный ввод")
	ErrWrongConsoleInput  = errors.New("Неверный ввод")
	ErrNoSolutions = errors.New("Нет решений")
)
