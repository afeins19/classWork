#lang plait

#| Local Scope |#
;; Let - defines a local binding for some variable 
(let ([x 5]) x) ;; define x as 5 

;; first the inner x is bound to the value 2.
;; Then we move to the outer let and note that the x in this scope is defined as 1.
;; we then sum the nested x=1 with the outer x=2 to get x=3
(let ([x 1]) 
  (+ (let ([x 2]) x)
       x)) 

|# function composition #|