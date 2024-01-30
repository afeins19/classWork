#lang plait

#|
              Advanced Plait

|#

;; types and variants
(define-type Exp
  [num (n : Number)]
  [plus (left : Exp)
        (right : Exp)]
  [mult (left : Exp)
         (right : Exp)])


;; s-expression 
(define prog `(+ (* 4 2) 7)) 

;; parsing s-exp into a list 
(s-exp->list prog)
(first (s-exp->list prog)) ;; extracting plus sign
(second (s-exp->list prog))

;;parsing s-expression
(define (parse s)
  (cond
    [(s-exp-number? s) (num (s-exp->number s))]
    [(s-exp-list?) s]))
