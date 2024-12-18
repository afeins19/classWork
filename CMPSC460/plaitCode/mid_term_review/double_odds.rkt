#lang plait

;; double_odds: returns a list of all odd values doubled 

(define (double_odds lst)
  (type-case (Listof Number) lst
    [empty empty]
    [(cons f r) (cond
                  [(odd? f) (cons {* 2 f} (double_odds r))]
                  [else (cons f (double_odds r))])]))

(double_odds '(1 2 25227))


