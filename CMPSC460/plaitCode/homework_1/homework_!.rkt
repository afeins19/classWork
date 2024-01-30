#lang plait

;;The following Tree datatype implements a binary tree with a number in each node and leaf:

(define-type Tree
  (leaf [val : Number]) 
  (node [val : Number]
        [left : Tree]
        [right : Tree]))

#|
problem 1:

Implement a
sum function that takes a tree and returns the sum of the numbers in the
tree.

|#
(define (sum  [tr : Tree]) : Number
  (type-case Tree tr
    [(leaf v) v] ;; base case - return the leaf itself 
    [(node v l r) (+ (+ v (sum l)) (sum r))] ;; return the current value plus sum left and sum right 
    ) 
  )
 
;; base case test 
(test (sum (leaf 1)) 1)
(test (sum (node 5 (leaf 6) (leaf 7))) 18) ;; 1 leaf tree

#| Problem 2:

Implement the function
negate, which takes a tree and returns a tree that has the
same shape, but with all the numbers negated.

|#

;; negation involves constructing a new tree based on a the tree we wish to negate 
(define (negate [tr : Tree])
  (type-case Tree tr
    [(leaf v) (leaf (- 0 v))]
    [(node v l r) (node (- 0 v) (negate l) (negate r))]
  )
)


#|
;; Problem 2 Test Cases 
(test (negate (node 5 (leaf 6) (leaf 7)))
      (node -5 (leaf -6) (leaf -7)))

(define (contains? [tr : Tree] [target : Number])
  (type-case Tree tr
    [(leaf v) (if (= v target)
                  #t
                  #f)]
   [(node v l r) (if (= (v target) #t)
                     (if (contains? l target) #t) 
                     (else (contains? r target)) #f)]
    )
  )
 |#



