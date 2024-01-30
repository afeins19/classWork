#lang plait

#|PROBLEM 1
returns a list containing n copies of x|#
(define (duple n x)
  (cond
    [(equal? n 0) '()]
    [(> n 0) (cons x (duple (- n 1) x))]
  )
)

;; testing problem 1 
(test (duple 2 3)
      '(3 3))
(test (duple 4 '(ha ha))
      '((ha ha) (ha ha) (ha ha) (ha ha)))
(test (duple 0 '(word))
      '())

#|Problem 2...Use Quicksort?|#

