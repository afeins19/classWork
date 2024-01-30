#lang racket

(define (inc x)
  (+ x 1))

(define lst '(1 2 3 4 5 6))
 

;;my own maping function
(define (mymap fn lst)
  (cond
    [(empty? lst) empty]
    [else (cons (fn (first lst))
                (mymap fn (rest lst)))]))

;;(mymap inc lst)

;;my own even-number filter
(define (even_filter lst)
  (cond
    [(empty? lst) empty]
    [(even? (first lst)) (cons (first lst) (even_filter (rest lst)))]
    [(even_filter (rest lst))]))


(even_filter lst)

