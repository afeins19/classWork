#lang plait

(define (f x)
  (+ x 1))

;; same as first one but we are doing a lambda function 
(define ff
  (λ(x)(+ x 1)))
(f 2)
(ff 2)

(define (g z)
  (f (+ z 7)))
(g 5)


(g (g (g 5)))


;; order of operations example 
(* 3 (+ 4 2))
(+ 4 (* 2 3))