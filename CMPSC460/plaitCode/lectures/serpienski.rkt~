#lang racket

;; (foldl cons '(34 78) '(1 2 3 4))
;; (foldr cons '(34 78) '(1 2 3 4))

#|
(define (g alst)
  (cond
    [(empty? (rest alst)) empty]
    [else (if (h (length alst))
              (cons (first alst) (g (rest alst)))
              (g (rest alst)))]))
(define (h n)
  (let ([r (remainder n 2)])
    (if (zero? r) #t #f)))
(define lst2 '(11 22 33 44 55))

|#


(require 2htdp/image)

(let sierpinski ([n 8])
  (if (zero? n)
    (triangle 2 'solid 'red)
    (let ([t (sierpinski (- n 1))])
      (freeze (above t (beside t t))))))

