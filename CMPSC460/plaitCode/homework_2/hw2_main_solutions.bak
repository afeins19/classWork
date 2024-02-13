#lang plait

(define-type Exp
  (numE [n : Number])
  (idE [s : Symbol])
  (plusE [l : Exp] 
         [r : Exp])
  (multE [l : Exp]
         [r : Exp])
  (appE [s : Symbol]
        [args : (Listof Exp)]) ;; appE can now take a list of expresssions

  ;; defining max expression [takes 2 expressions] 
  (maxE [l : Exp]
        [r : Exp])) 

(define-type Func-Defn
  (fd [name : Symbol] 
      [args : (Listof Symbol)] ;; funcs can accept 0 to n args 
      [body : Exp]))
 
(module+ test
  (print-only-errors #t))

;; An EXP is either
;; - `NUMBER
;; - `SYMBOL
;; - `{+ EXP EXP}
;; - `{* EXP EXP}
;; - `{SYMBOL EXP)

;; A FUNC-DEFN is
;; - `{define {SYMBOL SYMBOL} EXP}

;; parse ----------------------------------------
(define (parse [s : S-Exp]) : Exp
  (cond
    [(s-exp-match? `NUMBER s) (numE (s-exp->number s))]
    [(s-exp-match? `SYMBOL s) (idE (s-exp->symbol s))]
    [(s-exp-match? `{+ ANY ANY} s)
     (plusE (parse (second (s-exp->list s)))
            (parse (third (s-exp->list s))))]
    [(s-exp-match? `{* ANY ANY} s)
     (multE (parse (second (s-exp->list s)))
            (parse (third (s-exp->list s))))]

        ;; max keyword now makes a maxE expression
    [(s-exp-match? `{max ANY ANY} s)
     (maxE (parse (second (s-exp->list s)))
           (parse (third (s-exp->list s))))]
    
    [(s-exp-match? `{SYMBOL ANY ...} s)
     (appE (s-exp->symbol (first (s-exp->list s)))
           ;; now maps function arguments to any of the expressions 
           (map parse (rest (s-exp->list s))))]


    ;; if an argument or symbol doesnt match any of these...
    [else (error 'parse "invalid input")]))

(define (parse-fundef [s : S-Exp]) : Func-Defn
  (cond
    [(s-exp-match? `{define {SYMBOL SYMBOL ...} ANY} s)
     (fd (s-exp->symbol (first (s-exp->list (second (s-exp->list s))))) ;; function name 
         ;; now converts each of the arguments in the list into a symbol 
         (map  s-exp->symbol (rest (s-exp->list (second (s-exp->list s)))))
         (parse (third (s-exp->list s))))] ;; function body
    [else (error 'parse-fundef "invalid input")]))

#|
(define (dupcheck arg accum)

  )
|#

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
        (plusE (multE (numE 3) (numE 4)) (numE 8)))
  

     
      ;; testing appE
  
  ;; accepting multiple expressions 
  (test (parse `{double 9})
        (appE 'double (list (numE 9))))
  
  ;; accepting a function call with zero arguments - should return empty list 
  (test (parse `{double}) 
        (appE 'double '()))
  
  (test/exn (parse `{{+ 1 2}})
            "invalid input") ;; invalid since we need some args 

  (test (parse-fundef `{define {double x} {+ x x}})
        (fd 'double '(x) (plusE (idE 'x) (idE 'x))))
  (test/exn (parse-fundef `{def {f x} x})
            "invalid input") 

  (define double-def
    (parse-fundef `{define {double x} {+ x x}}))
  (define quadruple-def
    (parse-fundef `{define {quadruple x} {double {double x}}}))) 


;; interp ----------------------------------------
(define (interp [a : Exp] [defs : (Listof Func-Defn)]) : Number
  (type-case Exp a
    [(numE n) n]
    [(idE s) (error 'interp "free variable")]
    [(plusE l r) (+ (interp l defs) (interp r defs))]
    [(multE l r) (* (interp l defs) (interp r defs))]
    
        ;; max interpreting
    [(maxE l r) (cond
                  [(> (interp l defs) (interp r defs)) ;; if l evaluates to greater than r return l
                      (interp l defs)]
                  [else (interp r defs)])] ;; otherwise return r 

    ;; handles interping on nested functions
    [(appE s args) (local [(define fd (get-fundef s defs))]
                    (interp (subst-multi (map (λ(arg) (numE (interp arg defs))) args) ;; now subbst-multi handles interactions with substs
                                   (fd-args fd) 
                                   (fd-body fd))
                            defs))]))

(module+ test
  (test (interp (parse `2) empty)
        2)
  (test/exn (interp (parse `x) empty)
            "free variable")
  (test (interp (parse `{+ 2 1}) empty)
        3)
  (test (interp (parse `{* 2 1}) empty)
        2)
  (test (interp (parse `{+ {* 2 3}
                           {+ 5 8}})
                empty)
        19)
  (test (interp (parse `{double 8})
                (list double-def))
        16)
  (test (interp (parse `{quadruple 8})
                (list double-def quadruple-def))
        32)

      ;; testing max
  (test (interp (parse `{max 1 3}) empty) ;; comparing 2 unequal numbers  
        3)
  (test (interp (parse `{max 3 1}) empty) ;; comparing 2 unequal numbers  
        3)
  (test (interp (parse `{max 3 3}) empty) ;; comparing 2 equal numbers 
        3)
  ) 
  

;; get-fundef ---------------------------------------- 
(define (get-fundef [s : Symbol] [defs : (Listof Func-Defn)]) : Func-Defn
  (type-case (Listof Func-Defn) defs
    [empty (error 'get-fundef "undefined function")]
    [(cons def rst-defs) (if (eq? s (fd-name def))
                             def
                             (get-fundef s rst-defs))]))

(module+ test
  (test (get-fundef 'double (list double-def))
        double-def)
  (test (get-fundef 'double (list double-def quadruple-def))
        double-def)
  (test (get-fundef 'double (list quadruple-def double-def))
        double-def)
  (test (get-fundef 'quadruple (list quadruple-def double-def))
        quadruple-def)
  (test/exn (get-fundef 'double empty)
            "undefined function"))

;; subst ----------------------------------------
(define (subst [what : Exp] [for : Symbol] [in : Exp])
  (type-case Exp in
    [(numE n) in]
    [(idE s) (if (eq? for s)
                 what
                 in)]
    [(plusE l r) (plusE (subst what for l)
                        (subst what for r))]
    [(multE l r) (multE (subst what for l)
                        (subst what for r))]
    
    ;; handling multiple substitutions for a function with 0 or more args
    [(appE s args) (appE s (map (λ(arg) (subst what for arg)) args))]
    
    [(maxE l r) (maxE (subst what for l)
                      (subst what for r))] 
    )) 

;; doing multiple arguments 
(define (subst-multi [whats : (Listof Exp)] [fors : (Listof Symbol)] [fd-body : Exp])
  (cond
    [(and (empty? whats) (empty? fors)) fd-body] ;; base case - empty list of args so just return body 
    [(not (= (length whats) (length fors))) (error 'subst "wrong arity")] ;; error - number of args doesnt match number of vals passed in 

        ;; recursive case - not empty or wrong num vals so perform subst 
    ;; allows subst to handle expression calls as substs in other expressions?
    [else (subst-multi (rest whats) (rest fors) (subst (first whats) (first fors) fd-body))]) 
)


;;  testing subst itself
(module+ test
  (test (subst (parse `8) 'x (parse `9))
        (numE 9))
  (test (subst (parse `8) 'x (parse `x))
        (numE 8))
  (test (subst (parse `8) 'x (parse `y))
        (idE 'y))
  (test (subst (parse `8) 'x (parse `{+ x y}))
        (parse `{+ 8 y}))
  (test (subst (parse `8) 'x (parse `{* y x}))
        (parse `{* y 8}))
  (test (subst (parse `8) 'x (parse `{double x}))
        (parse `{double 8}))
  )
 
;; testing subst-multi

(module+ test
  (test/exn (subst-multi (list (numE 1) (numE 2)) (list 'x) (parse `{double x}))
        "wrong arity")     
)


;;  -- nate tests --
(module+ test
  (test (parse `2)
        (numE 2))
  (test (parse `x)
        (idE 'x))
  (test (parse `{+ 2 1})
        (plusE (numE 2) (numE 1)))
  (test (parse `{* 3 4})
        (multE (numE 3) (numE 4)))
  (test (parse `{max 3 4})
        (maxE (numE 3) (numE 4)))
  (test (parse `{+ {* 3 4} 8})
        (plusE (multE (numE 3) (numE 4))
               (numE 8)))
  (test (parse `{double 9})
        (appE 'double (list (numE 9))))
  (test (parse `{area 3 4})
        (appE 'area (list (numE 3) (numE 4))))
  (test (parse `{five})
        (appE 'five (list)))
  (test/exn (parse `{{+ 1 2}})
            "invalid input"))

(module+ test 
  (test (parse-fundef `{define {double x} {+ x x}})
        (fd 'double (list 'x) (plusE (idE 'x) (idE 'x))))
  (test (parse-fundef `{define {area w h} {* w h}})
        (fd 'area (list 'w 'h) (multE (idE 'w) (idE 'h))))
  (test (parse-fundef `{define {five} 5})
        (fd 'five (list) (numE 5)))

  ;;--- bonus test ---
  ;;(test/exn (parse-fundef `{define {f x x} x})
            ;;"bad syntax")

  
  (test/exn (parse-fundef `{def {f x} x})
            "invalid input")
  )
(module+ test
  (test (interp (parse `2) empty)
        2)
  (test/exn (interp (parse `x) empty)
            "free variable")
  (test (interp (parse `{+ 2 1}) empty)
        3)
  (test (interp (parse `{* 2 1}) empty)
        2)
  (test (interp (parse `{max 1 2}) empty)
        2)
  (test (interp (parse `{+ {* 2 3}
                           {+ 5 8}})
                empty)
        19)
  (test (interp (parse `{max {+ 4 5} {+ 2 3}})
                empty)
        9)
  (test (interp (parse `{double 8})
                (list double-def))
        16)
  (test (interp (parse `{quadruple 8})
                (list double-def quadruple-def))
        32)

  (test/exn (interp (parse `{double})
                    (list double-def))
            "wrong arity"))


(module+ test
  (test (get-fundef 'double (list double-def))
        double-def)
  (test (get-fundef 'double (list double-def quadruple-def))
        double-def)
  (test (get-fundef 'double (list quadruple-def double-def))
        double-def)
  (test (get-fundef 'quadruple (list quadruple-def double-def))
        quadruple-def)
  (test/exn (get-fundef 'double empty)
            "undefined function"))


(module+ test
  (test (subst (parse `8) 'x (parse `9))
        (numE 9))
  (test (subst (parse `8) 'x (parse `x))
        (numE 8))
  (test (subst (parse `8) 'x (parse `y))
        (idE 'y))
  (test (subst (parse `8) 'x (parse `{+ x y}))
        (parse `{+ 8 y}))
  (test (subst (parse `8) 'x (parse `{* y x}))
        (parse `{* y 8}))
  (test (subst (parse `8) 'x (parse `{max y x}))
        (parse `{max y 8}))
  (test (subst (parse `8) 'x (parse `{double x}))
        (parse `{double 8}))
  (test (subst (parse `8) 'x (parse `{area x y}))
        (parse `{area 8 y})))

    