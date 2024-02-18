#lang plait

;; --- unlet function ---
(define (unlet n alst)
  (type-case (Listof Number) alst
    [(cons frst rst) (if (= frst n) 
                    (rest alst) ;; we want to drop the first item in the list which mateches our unlet 
                    (cons frst (unlet n rst)))] ;; recurse
    [else empty])) 

(test (unlet 4 '(1 2 3 4 5 4 1 2))
      '(1 2 3 5 4 1 2))

