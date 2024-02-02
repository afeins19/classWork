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

#| Problem 3

Implement the function
contains?, which takes a tree and a number and returns #t if
the number is in the tree, #f otherwise.
Example: (contains? (node 5 (leaf 6) (leaf 7)) 6) should produce #t.
The second argument to the contains? function is “along for the ride.”

|#


(define (contains? [tr : Tree] [findVal : Number])
  (if (leaf? tr)
      (= (leaf-val tr) findVal) ;; base-case - return if the leaf is equal to the users number 
      (or  (contains? (node-left tr) findVal) (contains? (node-right tr) findVal) (= (node-val tr) findVal))));; we have a node, recurse 

 
;; write test cases
(test (contains? (node 5 (leaf 6) (leaf 7)) 6)
      #t) 

#| Problem 4: Big Leaves

Implement the function big-leaves?, which takes a tree and returns #t if every leaf
is bigger than the sum of numbers in the path of nodes from the root that reaches
the leaf.
Examples: (big-leaves? (node 5 (leaf 6) (leaf 7))) should produce #t, while (big-
leaves? (node 5 (node 2 (leaf 8) (leaf 6)) (leaf 7))) should produce #f (since 6 is
smaller than 5 plus 2).
The big-leaves? function should be a thin wrapper on another function,
perhaps bigger-leaves?, that accumulates a sum of node values.

big-leaves? wrapper function
bigger-leaves? accumulator 

|#


(define (bigger-leaves? [tr : Tree] [sum : Number]) 
  (type-case Tree tr 
    [(leaf v) (> v sum)]  ; Check if leaf value is greater than the accumulated sum
    [(node v l r) (and (bigger-leaves? l (+ sum v))  ; Check left subtree
                       (bigger-leaves? r (+ sum v)))]))  ; Check right subtree

(define (big-leaves? [tr : Tree]) : Boolean ;; do we need this? 
        (bigger-leaves? tr 0)
 )

 (test (big-leaves? (node 5 (leaf 6) (leaf 7))) #t)
 (test (big-leaves? (node 5 (node 2 (leaf 8) (leaf 6)) (leaf 7))) #f)


#| Problem 5 - positive-trees?


Implement the function
positive-trees?, which takes a list of trees and
returns #t if every member of the list is a positive tree, where a positive tree is
one whose numbers sum to a positive value.
Hint 1: This function takes a list, not a tree, so don’t try to use the template for
a tree function.
Hint 2: Use your sum function as a helper.
Hint 3: (positive-trees? empty) should produce #t, because there’s no tree in the
empty list whose numbers sum to 0 or less.

|#

(define (sumTree [tr : Tree] [sum : Number]) : Number 
  (type-case Tree tr 
    [(leaf v) (+ v sum)]  ; Check if leaf value is greater than the accumulated sum
    [(node v l r) (+ v (+ (sumTree l (+ sum v)) (sumTree r (+ sum v))))]))   ; Check right subtree


(define (positive-trees? [treeList : (Listof Tree)] )
  (cond
    [(empty? treeList) #t]   ;; base-case - empty list -> return true (well get to this case if list inputed is empty or we check every tree in the list) 
    [(> 0 (sumTree (first treeList) 0)) #f] ;; if we find a negative tree, return false
    [(= 0 (sumTree (first treeList) 0)) #f] ;; for some reason (> 0 0) is not caught 
    [else (positive-trees? (rest treeList))]
  )
) 

(test (positive-trees? (list)) #t) ;; base case, no tree
(test (positive-trees? (list (node 1 (leaf -1) (leaf 27)))) #t) ;; testing positive tree
(test (positive-trees? (list (node 0 (leaf 0) (leaf -1)))) #f) ;; testing negative tree
(test (positive-trees? (list (node 0 (leaf 0) (leaf 0)))) #f) ;; testing zero tree 

 
#| Part 6 -Transmutation

Implement a
positive-thinking function, which takes a Tree as argument and produces
a new tree which removes all negative leaves from the original tree. If the
resulting tree would have no nodes, return false.
Hint: the total number of nodes (leaf and interior) in the resulting tree will be
less than or equal to the total number of nodes in the original, minus the number of
negative leaves in the original.

- we are constructing a new tree

- base-case: reaching a leaf node
   check if positive and cons it
   if negative dont cons it

- recursive case: node found
    if node is positve cons it
    if node is negative, recurse with left and right sub trees 
|#

(define (makeTreePositive [tr : Tree])
  (type-case Tree tr
    ...
    )
    
)

