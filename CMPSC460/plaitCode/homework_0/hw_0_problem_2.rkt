#lang plait

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


;; lets try again :)
#|
(define (merge [op : (Number Number -> Boolean)]
               [l1 : (Listof Number)]
               [l2 : (Listof Number)]) : (Listof Number)

  (cond
    [(and (= (length l1) 1) (= (length l2) 1))
     (cond
       [(op (first l1) (first l2))
        (list (first l1) (first l2))]
       [(op (first l2) (first l1))
        (list (first l2) (first l1))]
     )
     ]

    
  )
  )
|#

;; trying with if statements
(define (merge [op : (Number Number -> Boolean)]
               [l1 : (Listof Number)]
               [l2 : (Listof Number)]) : (Listof Number)

  (if (and (= (length l1) 1) (= (length l2) 1))
      (if (op (first l1) (first l2))
          (list (first l1) (first l2)) ;; operator check pass, keep order l1[0], l2[0]
          (list (first l2) (first l1)) ;; swap order
      )
     
      (append (merge op (list (first l1)) (list (first l2))) (merge op (rest l1) (rest l2)))
 )
  )

(test (merge < '(1 4 6) '(2 5 8))
      '(1 2 4 5 6 8))
(test (merge > '(6 4 1) '(8 5 2))
      '(8 6 5 4 2 1))
 
  
 
  