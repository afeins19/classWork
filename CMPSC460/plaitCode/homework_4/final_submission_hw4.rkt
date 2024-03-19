#lang plait

(module+ test
  (print-only-errors #t))

(define-type-alias Location Number)

(define-type Value
  (numV [n : Number])
  (closV [arg : Symbol]
         [body : Exp]
         [env : Env])
  (boxV [l : Location]))

(define-type Exp
  (numE [n : Number])
  (idE [s : Symbol])
  (plusE [l : Exp] 
         [r : Exp])
  (multE [l : Exp]
         [r : Exp])
  (letE [n : Symbol] 
        [rhs : Exp]
        [body : Exp])
  (lamE [n : Symbol]
        [body : Exp])
  (appE [fun : Exp]
        [arg : Exp])
  (boxE [arg : Exp])
  (unboxE [arg : Exp])
  (setboxE [bx : Exp]
           [val : Exp])
  (beginE [Es : (Listof Exp)]))

(define-type Binding
  (bind [name : Symbol]
        [val : Value]))

(define-type-alias Env (Listof Binding))

(define mt-env empty)
(define extend-env cons)

(define-type Storage
  (cell [location : Location] 
        [val : Value]))

(define-type-alias Store (Listof Storage))
(define mt-store empty)
(define override-store cons)

(define-type Result
  (v*s [v : Value] [s : Store]))

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
    [(s-exp-match? `{let {[SYMBOL ANY]} ANY} s)
     (let ([bs (s-exp->list (first
                             (s-exp->list (second
                                           (s-exp->list s)))))])
       (letE (s-exp->symbol (first bs))
             (parse (second bs))
             (parse (third (s-exp->list s)))))]
    [(s-exp-match? `{lambda {SYMBOL} ANY} s)
     (lamE (s-exp->symbol (first (s-exp->list 
                                  (second (s-exp->list s)))))
           (parse (third (s-exp->list s))))]
    [(s-exp-match? `{box ANY} s)
     (boxE (parse (second (s-exp->list s))))]
    [(s-exp-match? `{unbox ANY} s)
     (unboxE (parse (second (s-exp->list s))))]
    [(s-exp-match? `{set-box! ANY ANY} s)
     (setboxE (parse (second (s-exp->list s)))
              (parse (third (s-exp->list s))))]
    [(s-exp-match? `{begin ANY ANY ...} s)
     (beginE (map parse (rest (s-exp->list s))))]
    [(s-exp-match? `{ANY ANY} s)
     (appE (parse (first (s-exp->list s)))
           (parse (second (s-exp->list s))))]
    [else (error 'parse "invalid input")]))

;; Parse Tests
(module+ test
  (test (parse `2)
        (numE 2))
  (test (parse `x) ; note: backquote instead of normal quote
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
  (test (parse `{box 0})
        (boxE (numE 0)))
  (test (parse `{unbox b})
        (unboxE (idE 'b)))
  (test (parse `{set-box! b 0})
        (setboxE (idE 'b) (numE 0)))
  (test/exn (parse `{{+ 1 2}})
            "invalid input"))

;; with form ----------------------------------------
(define-syntax-rule
  (with [(v-id sto-id) call]
    body)
  (type-case Result call
    [(v*s v-id sto-id) body]))

;; interp ----------------------------------------
(define (interp [a : Exp] [env : Env] [sto : Store]) : Result
  (type-case Exp a
    [(numE n) (v*s (numV n) sto)]
    [(idE s) (v*s (lookup s env) sto)]
    [(plusE l r)
     (with [(v-l sto-l) (interp l env sto)]
       (with [(v-r sto-r) (interp r env sto-l)]
         (v*s (num+ v-l v-r) sto-r)))]
    [(multE l r)
     (with [(v-l sto-l) (interp l env sto)]
           (with [(v-r sto-r) (interp r env sto-l)]
                 (v*s (num* v-l v-r) sto-r)))]
    [(letE n rhs body)
     (with [(v-rhs sto-rhs) (interp rhs env sto)]
           (interp body
                   (extend-env
                    (bind n v-rhs)
                    env)
                   sto-rhs))]
    [(lamE n body)
     (v*s (closV n body env) sto)]
    [(appE fun arg)
     (with [(v-f sto-f) (interp fun env sto)]
           (with [(v-a sto-a) (interp arg env sto-f)]
                 (type-case Value v-f
                   [(closV n body c-env)
                    (interp body
                            (extend-env
                             (bind n v-a)
                             c-env)
                            sto-a)]
                   [else (error 'interp "not a function")])))]
    [(boxE a)
     (with [(v sto-v) (interp a env sto)]
       (let ([l (new-loc sto-v)])
         (v*s (boxV l) 
              (override-store (cell l v) 
                              sto-v))))]
    [(unboxE a)
     (with [(v sto-v) (interp a env sto)]
           (type-case Value v
             [(boxV l) (v*s (fetch l sto-v) 
                            sto-v)]
             [else (error 'interp "not a box")]))]
    [(setboxE bx val)
     (with [(v-b sto-b) (interp bx env sto)]
           (with [(v-v sto-v) (interp val env sto-b)]
                 (type-case Value v-b
                   [(boxV l)
                    (v*s v-v
                         (update-store (cell l v-v)
                                         sto-v))]
                   [else (error 'interp "not a box")])))]
    [(beginE Es) (eval_single_exp Es env sto)]))

(define (eval_single_exp [exps : (Listof Exp)] [env : Env] [sto : Store])
  (if (empty? (rest exps))
      (interp (first exps) env sto)
      (with [(v-l sto-l) (interp (first exps) env sto)]
            (eval_single_exp (rest exps) env sto-l))))

(module+ test
  (test (interp (parse `2) mt-env mt-store)
        (v*s (numV 2) mt-store))
  (test/exn (interp (parse `x) mt-env mt-store)
            "free variable")
  (test (interp (parse `x) 
                (extend-env (bind 'x (numV 9)) mt-env)
                mt-store)
        (v*s (numV 9)
             mt-store))
  (test (interp (parse `{+ 2 1}) mt-env mt-store)
        (v*s (numV 3)
             mt-store))
  (test (interp (parse `{* 2 1}) mt-env mt-store)
        (v*s (numV 2)
             mt-store))
  (test (interp (parse `{+ {* 2 3} {+ 5 8}})
                mt-env
                mt-store)
        (v*s (numV 19)
             mt-store))
  (test (interp (parse `{lambda {x} {+ x x}})
                mt-env
                mt-store)
        (v*s (closV 'x (plusE (idE 'x) (idE 'x)) mt-env)
             mt-store))
  (test (interp (parse `{let {[x 5]}
                          {+ x x}})
                mt-env
                mt-store)
        (v*s (numV 10)
             mt-store))
  (test (interp (parse `{let {[x 5]}
                          {let {[x {+ 1 x}]}
                            {+ x x}}})
                mt-env
                mt-store)
        (v*s (numV 12)
             mt-store))
  (test (interp (parse `{let {[x 5]}
                          {let {[y 6]}
                            x}})
                mt-env
                mt-store)
        (v*s (numV 5)
             mt-store))
  (test (interp (parse `{{lambda {x} {+ x x}} 8})
                mt-env
                mt-store)
        (v*s (numV 16)
             mt-store))
  (test (interp (parse `{box 5})
                mt-env
                mt-store)
        (v*s (boxV 1)
             (override-store (cell 1 (numV 5))
                             mt-store)))
  (test (interp (parse `{unbox {box 5}})
                mt-env
                mt-store)
        (v*s (numV 5)
             (override-store (cell 1 (numV 5))
                             mt-store)))
  (test (interp (parse `{set-box! {box 5} 6})
                mt-env
                mt-store)
        (v*s (numV 6)
             (override-store (cell 1 (numV 6))
                             mt-store)))
  (test (interp (parse `{let {[b {box 1}]}
                          {begin
                            {set-box! b 2}
                            {unbox b}}})
                mt-env
                mt-store)
        (v*s (numV 2)
             (override-store (cell 1 (numV 2))
                             mt-store)))
  (test (interp (parse `{begin 1 2})
                mt-env
                mt-store)
        (v*s (numV 2)
             mt-store))
  (test (interp (parse `{begin 1 2 3})
                mt-env
                mt-store)
        (v*s (numV 3)
             mt-store))
  (test (interp (parse `{unbox {begin {box 5} {box 6}}})
                mt-env
                mt-store)
        (v*s (numV 6)
             (override-store (cell 2 (numV 6))
                             (override-store (cell 1 (numV 5))
                                             mt-store))))
  (test (interp (parse `{let {[b (box 5)]}
                          {begin
                            {set-box! b 6}
                            {unbox b}}})
                mt-env
                mt-store)
        (v*s (numV 6)
             (override-store (cell 1 (numV 6))
                             mt-store)))
    
  (test (interp (parse `{begin 1 2})
                mt-env
                mt-store)
        (v*s (numV 2)
             mt-store))
  (test (interp (parse `{begin 1 2 3})
                mt-env
                mt-store)
        (v*s (numV 3)
             mt-store))
  (test (interp (parse `{unbox {begin {box 5} {box 6}}})
                mt-env
                mt-store)
        (v*s (numV 6)
             (override-store (cell 2 (numV 6))
                             (override-store (cell 1 (numV 5))
                                             mt-store))))
  (test (interp (parse `{let {[b (box 5)]}
                          {begin
                            {set-box! b 6}
                            {unbox b}}})
                mt-env
                mt-store)
        (v*s (numV 6)
             (override-store (cell 1 (numV 6))
                             mt-store)))
  
  (test/exn (interp (parse `{1 2}) mt-env mt-store)
            "not a function")
  (test/exn (interp (parse `{+ 1 {lambda {x} x}}) mt-env mt-store)
            "not a number")
  (test/exn (interp (parse `{let {[bad {lambda {x} {+ x y}}]}
                              {let {[y 5]}
                                {bad 2}}})
                    mt-env
                    mt-store)
            "free variable")
  (test/exn (interp (parse `{unbox 1}) mt-env mt-store)
            "not a box")
  (test/exn (interp (parse `{set-box! 1 1}) mt-env mt-store)
            "not a box"))
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

;; num+ and num* ----------------------------------------
(define (num-op [op : (Number Number -> Number)] [l : Value] [r : Value]) : Value
  (cond
   [(and (numV? l) (numV? r))
    (numV (op (numV-n l) (numV-n r)))]
   [else
    (error 'interp "not a number")]))
(define (num+ [l : Value] [r : Value]) : Value
  (num-op + l r))
(define (num* [l : Value] [r : Value]) : Value
  (num-op * l r))

(module+ test
  (test (num+ (numV 1) (numV 2))
        (numV 3))
  (test (num* (numV 2) (numV 3))
        (numV 6)))

;; store operations ----------------------------------------

(define (new-loc [sto : Store]) : Location
  (+ 1 (max-address sto)))

(define (max-address [sto : Store]) : Location
  (type-case (Listof Storage) sto
   [empty 0]
   [(cons c rst-sto) (max (cell-location c)
                          (max-address rst-sto))]))

(define (fetch [l : Location] [sto : Store]) : Value
  (type-case (Listof Storage) sto
   [empty (error 'interp "unallocated location")]
   [(cons c rst-sto) (if (equal? l (cell-location c))
                         (cell-val c)
                         (fetch l rst-sto))]))


;; Problem 1:
;; Change the implementation of set-box! so that the old value
;; of the box is dropped (i.e., replaced with the new value) instead of
;; merely hidden by the outside-in search order of fetch

    ;; type store: (Listof Storage)
      ;; type storage: (Listof cell)
        ;; type cell: (location::number, val:val) 

;; interp now returns result(v::val, s::store) 



;; updating store code
      ;; pre-check => run fetch on the store to see if the box exists 
    ;; 1. iterate over the list storing all cells that do not match 
    ;; 2. if we find the target cell, we create a new value and have it be consd to the current list of values that dont equal it
    ;; 3. since we updated the value, just const whats left of the list onto the built-up list
    ;; 4. this is now the updated store. If the next cell is empty, we have traversed the store and could not find the specified box - make a new one and append it    


(define (update-store [incell : Storage] [sto : Store])
  (type-case (Listof Storage) sto
    [empty (override-store incell empty)]
    [(cons f r) (if (= (cell-location incell) (cell-location f))
                    (override-store incell r)
                    (override-store f (update-store incell r)))]))





(module+ test
  (test (max-address mt-store)
        0)
  (test (max-address (override-store (cell 2 (numV 9))
                                     mt-store))
        2)
  
  (test (fetch 2 (override-store (cell 2 (numV 9))
                                 mt-store))
        (numV 9))
  (test (fetch 2 (override-store (cell 2 (numV 10))
                                 (override-store (cell 2 (numV 9))
                                                 mt-store)))
        (numV 10))
  (test (fetch 3 (override-store (cell 2 (numV 10))
                                 (override-store (cell 3 (numV 9))
                                                 mt-store)))
        (numV 9))
  (test/exn (fetch 2 mt-store)
            "unallocated location")

  (test (update-store (cell 1 (numV 2)) mt-store)
        (override-store (cell 1 (numV 2)) mt-store))
  (test (update-store (cell 1 (numV 3))
                      (override-store (cell 1 (numV 2)) 
                                      mt-store))
        (override-store (cell 1 (numV 3)) mt-store))
  (test (update-store (cell 1 (numV 3))
                      (override-store (cell 2 (numV 2)) 
                                      mt-store))
        (override-store (cell 2 (numV 2))
                        (override-store (cell 1 (numV 3)) 
                                        mt-store))))

