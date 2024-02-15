#lang plait


;; --- unlet function ---
(define (unlet n alst)
  (type-case (Listof Number) alst
    [(cons frst rst) (if (= frst n) 
                    (unlet n rst) ;; recurse if we match to without cons-ing removing the item from the list 
                    (cons frst (unlet n rst)))] ;; recurse
    [else empty])) 

(test (unlet 4 '(1 2 3 4 5 4 1 2))
      '(1 2 3 5 1 2)) 