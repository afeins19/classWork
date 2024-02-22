#lang plait

(define-type Value
  (numV [n : Number])
  (boolV [b : Boolean]) 
  (closV [arg : Symbol]
         [body : Exp]
         [env : Env])
  
  (thunkV [body : Exp]
          [env : Env]))

(define-type Exp
  (numE [n : Number])
  
  (trueE) ;; a true boolean exp
  (falseE) ;; a false boolean exp
  
  (idE [s : Symbol])
  (plusE [l : Exp] 
         [r : Exp])
  (multE [l : Exp]
         [r : Exp])

  ;; equality expression 
  (eqE  [l : Exp]
        [r : Exp])

  ;; if expression
  (ifE [cnd : Exp] ;; condition 
       [thn : Exp] ;; then (do this if true)
       [els : Exp]) ;; else 

  (letE [n : Symbol] ;; variable
        [rhs : Exp] ;; binding 
        [body : Exp]) ;; expression to execute 

  ;; defining unlet
  (unletE [s : Symbol] ;; unlet this symbol 
          [body : Exp]) ;; expression to evaluate with local env 

  
  (lamE [n : Symbol]
        [body : Exp])
  (appE [fun : Exp]
        [arg : Exp])

  ;; delay only takes the function code 
  (delayE [body : Exp])
  (forceE [body : Exp])
  )

(define-type Binding
  (bind [name : Symbol]
        [val : Value]))

(define-type-alias Env (Listof Binding))

(define mt-env empty)
(define extend-env cons)

(module+ test
  (print-only-errors #t))

#|
    ;; Equality Operator
    [(s-exp-match? `{= ANY ANY})
     ;; checking for comparison of numbers only 
     (cond
       [(and (s-exp-match? `NUMBER (parse (second s))) (s-exp-match? `NUMBER (parse (third s)))) ;; case - comparing 2 numbers -> return boolean
        (cond
          [(= (second s) (third s)) 'true] ;; if 2 numbers are equal -> return true
          [else 'false])] ;; otherwise -> return false 
       [else (error 'parse "not a boolean")])]
|#

;; parse ----------------------------------------

#|

letE
  
  (letE [n : Symbol] 
        [rhs : Exp]
        [body : Exp])

|#
(define (parse [s : S-Exp]) : Exp
  (cond
    [(s-exp-match? `NUMBER s) (numE (s-exp->number s))]

    ;; returns a default true or false evaluation of the expression 
    [(s-exp-match? `true s) (trueE)]
    [(s-exp-match? `false s) (falseE)]

    ;; boolE
    ;;[(s-exp-match? `true s) (boolV #t)]
    ;;[(s-exp-match? `false s) (boolV #f)] 

    ;; equality parsing 
    [(s-exp-match? `{= ANY ANY} s)
     (eqE (parse (second (s-exp->list s))) (parse (third (s-exp->list s)))) ;; recurses into expressions 
     ]

    ;; if statement parsing 
    [(s-exp-match? `{if ANY ANY ANY} s)
     (ifE (parse (second (s-exp->list s))) (parse (third (s-exp->list s))) (parse (fourth (s-exp->list s))))
    ]
    
    [(s-exp-match? `SYMBOL s) (idE (s-exp->symbol s))]
    [(s-exp-match? `{+ ANY ANY} s)
     (plusE (parse (second (s-exp->list s)))
            (parse (third (s-exp->list s))))]
    [(s-exp-match? `{* ANY ANY} s)
     (multE (parse (second (s-exp->list s)))
            (parse (third (s-exp->list s))))]
    
    ;; parsing letE
    [(s-exp-match? `{let {[SYMBOL ANY]} ANY} s)

    ;; extracting the symbol and giving it a generic name -> bs 
     (let ([bs (s-exp->list (first 
                             (s-exp->list (second
                                           (s-exp->list s)))))])

       ;; linking the symbol to a new letE with the body given by whats passed in 
       (letE (s-exp->symbol (first bs))
             (parse (second bs))
             (parse (third (s-exp->list s)))))]

    ;; parsing unlet
    ;; 1. unbind last occurance of symbol from the env (unlet function?) 
    ;; 2. parse expression
    ;; want to return the                              
    [(s-exp-match? `{unlet SYMBOL ANY} s)
     ;; make the var being unbound into an id
     ;; parse the expression in the scope of the given unletE 
     (unletE (s-exp->symbol (second (s-exp->list s))) (parse (third (s-exp->list s))))]

    
    [(s-exp-match? `{lambda {SYMBOL} ANY} s)
     (lamE (s-exp->symbol (first (s-exp->list 
                                  (second (s-exp->list s)))))
           (parse (third (s-exp->list s))))]
    
    [(s-exp-match? `{delay ANY} s) (delayE (parse (second (s-exp->list s))))]
    [(s-exp-match? `{force ANY} s) (forceE (parse (second (s-exp->list s))))]

    
    [(s-exp-match? `{ANY ANY} s)
     (appE (parse (first (s-exp->list s)))
           (parse (second (s-exp->list s))))]
    [else (error 'parse "invalid input")]))

;; removes the unletted var from a given environment 
(define (unbind [var : Symbol] [env : (Listof Binding)])
  (type-case (Listof Binding) env
    [(cons b rst-env) (if (symbol=? (bind-name b) var)
                          rst-env
                          (cons b (unbind var rst-env)))]
    [empty empty]  
    ))

  #|
  (if (equal? (first (first (s-exp->list env)) var)) ;; if we found the binding 
      (extend-env (mt-env) (rest env)) ;; return the env with that binding removed 
      (unbind var (rest env)))) ;; otherwise recurse with the rest of the list and keep looking
  |#
;; creating sample env's
(define sampenv (list (bind 'f (numV 1)) (bind 'g (numV 2))))
(define sampenv2 (list (bind 'f (numV 1)) (bind 'g (numV 2)) (bind 'f (numV 3))))

;; testing unbind function
(module+ test
  ;; testing unbinding missing value (empty case) 
  (test (unbind 'x sampenv) sampenv)

  ;; testing some valid unbinds
  (test (unbind 'f sampenv2) (list (bind 'g (numV 2)) (bind 'f (numV 3)))))



(module+ test 
  (test (parse `2)
        (numE 2))
  (test (parse `x)
        (idE 'x))
  (test (parse `{+ 2 1})
        (plusE (numE 2) (numE 1)))
  (test (parse `{* 3 4})
        (multE (numE 3) (numE 4)))
  (test (parse `{+ {* 3 4} 8})
        (plusE (multE (numE 3) (numE 4))
               (numE 8)))
  (test (parse `{let {[x {+ 1 2}]}
                  y})
        (letE 'x (plusE (numE 1) (numE 2))
              (idE 'y)))
  (test (parse `{lambda {x} 9})
        (lamE 'x (numE 9)))
  (test (parse `{double 9})
        (appE (idE 'double) (numE 9)))
  (test/exn (parse `{{+ 1 2}})
            "invalid input"))


;; testing unlet 
(module+ test
  (test/exn (interp (parse `{let {[x 1]}
                              {unlet x
                                     x}})
                    mt-env)
            "free variable")
  (test (interp (parse `{let {[x 1]}
                          {+ x {unlet x 1}}})
                mt-env)
        (interp (parse `2) mt-env))
  (test (interp (parse `{let {[x 1]}
                          {let {[x 2]}
                            {+ x {unlet x x}}}})
                mt-env)
        (interp (parse `3) mt-env))
  (test (interp (parse `{let {[x 1]}
                          {let {[x 2]}
                            {let {[z 3]}
                              {+ x {unlet x {+ x z}}}}}})
                mt-env)
        (interp (parse `6) mt-env))
  (test (interp (parse `{let {[f {lambda {z}
                                   {let {[z 8]}
                                     {unlet z
                                            z}}}]}
                          {f 2}})
                mt-env)
(interp (parse `2) mt-env)) 

  )

;; interp ----------------------------------------
#|
    
    num+ & num*
interp only ingests expressions and the env and does not actually apply any operator to the values
so interp calls num+ and num* to actually perform the evaluation. These then return a numV of representing
the sum.  
 
|#
(define (interp [a : Exp] [env : Env]) : Value
  (type-case Exp a     
    [(numE n) (numV n)] 

    ;; evaluating booleans to represent actual bool vals  
    [(trueE) (boolV #t)] 
    [(falseE) (boolV #f)] 

    ;; eqE expressions  
    [(eqE l r) (num= (interp l env) (interp r env))]

    ;; ifE expressions 
    [(ifE cnd thn els)
     (if (cnd-check (interp cnd env)) ;; if condition is a boolV
         (interp thn env) ;; interp the task
         (interp els env)) ;; otherwise, interp the else 
     ]
     
    [(idE s) (lookup s env)]
    [(plusE l r) (num+ (interp l env) (interp r env))]
    [(multE l r) (num* (interp l env) (interp r env))]

    
    [(letE n rhs body) (interp body
                               (extend-env
                                (bind n (interp rhs env)) ;; bind rhs to the symbol and use that eval whats in the body 
                                env))]

    ;; unletE expressions
    ;; interp on the body of the unletE
    ;; use the env thats just the scope of the unletE...
    [(unletE s body) 
     (interp body (unbind s env))] 

    
    [(lamE n body) (closV n body env)]
    [(appE fun arg) (type-case Value (interp fun env)
                      [(closV n body c-env)
                       (interp body
                               (extend-env
                                (bind n 
                                      (interp arg env))
                                c-env))]
                      [else (error 'interp "not a function")])]

    [(delayE body) (thunkV body env)] ;; create a thunk (function with env but no parameters) 

    [(forceE body)
     (type-case Value (interp body env) ;; compare value against all possible values 
       [(thunkV body env) (interp body env)] ;; if its a thunk, actually run the function 
       [else (error 'interp "not a thunk")])]))

#|(define-type Value
  (numV [n : Number])
  (boolV [b : Boolean]) 
  (closV [arg : Symbol]
         [body : Exp]
         [env : Env])
  
  (thunkV [body : Exp]
          [env : Env])
  )|#


;; checks if the condition for our if statement is a boolV expression 
(define (cnd-check [cnd : Value])
  (type-case Value cnd
    [(boolV cnd) cnd]
    [else (error 'interp "not a boolean")] 
  )
)

(module+ test
  (test/exn (interp (parse `{force 1})
                    mt-env)
            "not a thunk")
  (test (interp (parse `{force {if {= 8 8} {delay 7} {delay 9}}})
                mt-env)
        (interp (parse `7)
                mt-env))
  (test (interp (parse `{let {[d {let {[y 8]}
                                   {delay {+ y 7}}}]}
                          {let {[y 9]}
                            {force d}}})
                mt-env)
        (interp (parse `15)
                mt-env))
)
 
(module+ test
  (test (interp (parse `2) mt-env)
        (numV 2))
  (test/exn (interp (parse `x) mt-env)
            "free variable")
  (test (interp (parse `x) 
                (extend-env (bind 'x (numV 9)) mt-env))
        (numV 9))
  (test (interp (parse `{+ 2 1}) mt-env)
        (numV 3))
  (test (interp (parse `{* 2 1}) mt-env)
        (numV 2))
  (test (interp (parse `{+ {* 2 3} {+ 5 8}})
                mt-env)
        (numV 19))

  (test (interp (parse `{lambda {x} {+ x x}})
                mt-env)
        (closV 'x (plusE (idE 'x) (idE 'x)) mt-env))
  (test (interp (parse `{let {[x 5]}
                          {+ x x}})
                mt-env)
        (numV 10))
  (test (interp (parse `{let {[x 5]}
                          {let {[x {+ 1 x}]}
                            {+ x x}}})
                mt-env)
        (numV 12))
  (test (interp (parse `{let {[x 5]}
                          {let {[y 6]}
                            x}})
                mt-env)
        (numV 5))
  (test (interp (parse `{{lambda {x} {+ x x}} 8})
                mt-env) 
        (numV 16))

  (test/exn (interp (parse `{1 2}) mt-env)
            "not a function")
  (test/exn (interp (parse `{+ 1 {lambda {x} x}}) mt-env)
            "not a number")
  (test/exn (interp (parse `{let {[bad {lambda {x} {+ x y}}]}
                              {let {[y 5]}
                                {bad 2}}})
                    mt-env)
            "free variable")

  #;
  (time (interp (parse '{let {[x2 {lambda {n} {+ n n}}]}
                          {let {[x4 {lambda {n} {x2 {x2 n}}}]}
                            {let {[x16 {lambda {n} {x4 {x4 n}}}]}
                              {let {[x256 {lambda {n} {x16 {x16 n}}}]}
                                {let {[x65536 {lambda {n} {x256 {x256 n}}}]}
                                  {x65536 1}}}}}})
                mt-env)))


 ;; testing booleans

(module+ test
  (test (interp (parse `{if {= 2 {+ 1 1}} 7 8})
                mt-env)
        (interp (parse `7)
                mt-env))
  (test (interp (parse `{if false {+ 1 {lambda {x} x}} 9})
                mt-env)
        (interp (parse `9)
                mt-env))
  (test (interp (parse `{if true 10 {+ 1 {lambda {x} x}}})
                mt-env)
        (interp (parse `10)
                mt-env))
  (test/exn (interp (parse `{if 1 2 3})
                    mt-env)
            "not a boolean")
  )

;; num+ and num* ----------------------------------------
;; '_a -> unknown type
;; checks to make sure operations are being done on numbers only 
(define (num-op [op : (Number Number -> '_a)] [l : Value] [r : Value]) : '_a
  (cond
   [(and (numV? l) (numV? r))
    (op (numV-n l) (numV-n r))]
   [else
    (error 'interp "not a number")]))


(define (num+ [l : Value] [r : Value]) : Value
  (numV (num-op + l r)))
(define (num* [l : Value] [r : Value]) : Value
  (numV (num-op * l r)))

;;num= operator for comparing numbers
(define (num= [l : Value] [r : Value]) : Value 
   (boolV (num-op = l r))) ;; replaces op in the cond with the equals sign 

(module+ test
  (test (num+ (numV 1) (numV 2))
        (numV 3))
  (test (num* (numV 2) (numV 3))
        (numV 6)))

;; lookup ----------------------------------------
(define (lookup [n : Symbol] [env : Env]) : Value
  (type-case (Listof Binding) env
   [empty (error 'lookup "free variable")]
   [(cons b rst-env) (cond
                       [(symbol=? n (bind-name b))
                        (bind-val b)]
                       [else (lookup n rst-env)])]))

(module+ test
  (test/exn (lookup 'x mt-env)
            "free variable")
  (test (lookup 'x (extend-env (bind 'x (numV 8)) mt-env))
        (numV 8))
  (test (lookup 'x (extend-env
                    (bind 'x (numV 9))
                    (extend-env (bind 'x (numV 8)) mt-env)))
        (numV 9))
  (test (lookup 'y (extend-env
                    (bind 'x (numV 9))
                    (extend-env (bind 'y (numV 8)) mt-env)))
        (numV 8))) 
