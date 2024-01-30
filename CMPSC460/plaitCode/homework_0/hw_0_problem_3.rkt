#lang plait

#|Problem 3
return an association list from a list of symbols and a list of numbers
define a type to allow for the output of a list of associations
?_t is to be replaced with your appropriately named type   |#

;;custom type 
(define-type Pair 
  (symnum   [s : Symbol] ;; synum variant 
            [n : Number])
)

(define (make-assoc [names : (Listof Symbol)] [values : (Listof Number)]) : (Listof Pair)
  (cond
     [(and (= (length names) 1) (= (length values) 1)) ;; base case 
      (list (symnum (first names) (first values)))
      ]
     [else
      ;; recursive case 
      (append (make-assoc (list (first names)) (list (first values))) (make-assoc (rest names) (rest values)))
      ]
     )
  )


(test (make-assoc '(a b c d) '(1 2 3 4))
      (list (symnum 'a 1) (symnum 'b 2) (symnum 'c 3) (symnum 'd 4)))
(test (make-assoc '(t a c o tuesday) '(0 1 34 1729 42))
      (list(symnum 't 0) (symnum 'a 1) (symnum 'c 34) (symnum 'o 1729) (symnum 'tuesday 42)))