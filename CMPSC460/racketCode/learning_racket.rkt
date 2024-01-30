#lang racket

(define (inc value)
  (+ value 1))

(if (= 1 (inc 0))
    #t
    #f)

(define (abs x)
  (cond
    [(> x 0) x]
    [(= x 0) "bruh"]
    [else (- x)]))

(define (fact n)
  (cond
    [(= n 0) 1]
    [(= n 1) 1]
    [else (* n (fact (- n 1)))]))

;; optimized factorial
(define (fact2 n acc)
  (cond
    [(= n 1) acc]
    [else (fact2 (- n 1) (* n acc))]))


(define (p1l lst)
  (cond
    [(empty? lst) empty]
    [else (cons (+ 1 (first lst)) (p1l (rest lst)))]))

