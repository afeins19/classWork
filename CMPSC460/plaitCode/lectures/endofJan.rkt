#lang plait

(define-type Exp
  (numE [n : Number])
  (plusE [l : Exp]
         [r : Exp])
  (multE [l : Exp]
         [r : Exp])
  (condE [tst : Exp]
        [thn : Exp]
        [els : Exp])
  (boolE [b : Boolean])
  ;;letE ;;takes in a binding ([<var> <value>]) <var> 
  )

(define-type Value
  [numV [a-number : Number]]
  (boolV [a-bool : Boolean]))
;; An EXP-S-EXP is either
;; - `NUMBER
;; - `{+ EXP-S-EXP EXP-S-EXP}
;; - `{* EXP-S-EXP EXP-S-EXP}
   
(define (parse [s : S-Exp]) : Exp
  (cond
    [(s-exp-match? `NUMBER s) (numE (s-exp->number s))]
    [(s-exp-match? `#t s) (boolE #t)]
    [(s-exp-match? `#f s) (boolE #f)]
    [(s-exp-match? `{+ ANY ANY} s)
     (plusE (parse (second (s-exp->list s)))
            (parse (third (s-exp->list s))))]
    [(s-exp-match? `{* ANY ANY} s)
     (multE (parse (second (s-exp->list s)))
            (parse (third (s-exp->list s))))]
    [(s-exp-match? `{if ANY ANY ANY} s)
     (condE (parse (second (s-exp->list s))) 
           (parse (third (s-exp->list s)))
           (parse (fourth (s-exp->list s))))]
    [else (error 'parse "invalid input")]))

(test (parse `2)
      (numE 2))
(test (parse `{+ 2 1})
      (plusE (numE 2) (numE 1)))
(test (parse `{* 3 4})
      (multE (numE 3) (numE 4)))
(test (parse `{+ {* 3 4} 8})
      (plusE (multE (numE 3) (numE 4))
             (numE 8)))

(define (interp [a : Exp]) : Number
  (type-case Exp a
    [(numE n) n]
    [(condE p t e) (if (zero?(interp p))
                      (interp t)
                      (interp e))]
    [(plusE l r) (+ (interp l) (interp r))]
    [(boolE b) 1]
    [(multE l r) (* (interp l) (interp r))]))

(define (eval [a : Exp]) : Value
  (type-case Exp a
    [(numE n) (numV n)]
    [(condE p t e) (if (type-case Value (eval p)
                        [(boolV b) b]
                        [(numV n) (error 'eval "true is our only truth")])
                      (eval t)
                      (eval e))]
    [(plusE l r) (add (eval l) (eval r))] 
    [(boolE b) (boolV b)]
    [(multE l r) (numV 3)]))

(define (add v1 v2)
  (type-case Value v1
    [(numV n1)
     (type-case Value v2       
       [(numV n2) (numV (+ n1 n2))]
       [else (error '+ "expects RHS to be a number")])]
    [else (error '+ "expects LHS to be a number")]))                                            

#|Nate stuff|#
(test (eval (parse `{if #t 1 2}))
      (numV 1))  
(test (interp (parse `{if #t 1 2}))
      2)
 
(test (interp (parse `{if 0 1 2})) 1)
(test/exn (eval (parse `{if 0 1 2})) "true is our only truth")
(test (eval (parse `{+ 1 1})) (numV 2))


(test (interp (parse `2))
      2)
(test (interp (parse `{+ 2 1}))
      3)
(test (interp (parse `{* 2 1}))
      2)
(test (interp (parse `{+ {* 2 3}
                         {+ 5 8}}))
      19)