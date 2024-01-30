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

#|PROBLEM 2
return a sorted list of integers based on operator
less than < ascending
greater than > descending
 |#

#|
(define (merge [op : (Number Number -> Boolean)]
               [int-list1 : (Listof Number)]
               [int-list2 : (Listof Number)]) : (Listof Number)

  ;; base case - both lists have length 1 
  (if [(and (= (length int-list1) 1) (= (length int-list2) 1))] ;; if both lists have length 1
      (cond
        [(op (first int-list1) (first int-list2)) (list (first int-list1) (first int-list2))] 
        [(list (first int-list2) (first int-list1))] ;; otherwise, reverse the order 
    ))
  (else
   [(append ((merge op (first int-list1) (first int-list2))) (merge op (rest int-list1) (rest int-list2)))]))

(test (merge < '(1 4 6) '(2 5 8))
      '(1 2 4 5 6 8))
(test (merge > '(6 4 1) '(8 5 2))
      '(8 6 5 4 2 1))
|#



;; trying with if statements
(define (merge [op : (Number Number -> Boolean)]
               [l1 : (Listof Number)]
               [l2 : (Listof Number)]) : (Listof Number)

  (if (and (= (length l1) 1) (= (length l2) 1))
      (if (op (first l1) (first l2)) ;; base case 
          (list (first l1) (first l2)) ;; operator check passed... keep order l1[0], l2[0]
          (list (first l2) (first l1)) ;; swap order
      )
      ;; recursive case 
      (append (merge op (list (first l1)) (list (first l2))) (merge op (rest l1) (rest l2)))
 )
  )

(test (merge < '(1 4 6) '(2 5 8))
      '(1 2 4 5 6 8))
(test (merge > '(6 4 1) '(8 5 2))
      '(8 6 5 4 2 1))
 

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