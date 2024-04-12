#lang racket

;; defining objects with private members 

(define (msg ob m . a)
  (apply (ob m) a))

(define (ob-priv init)
  (let ([count init])
    (lambda(m)
      (case m
        [(inc) (lambda() (set! count (+ count 1)))]
        [(dec) (lambda() (set! count (- count 1)))]
        [(get) (lambda() count)]))))


;; self modification  of objects 

(define ob-self!
  (let ([self `dummy])
    (begin
      (set! self
            (lambda(m)
              (case m
                [(inc) (lambda() (set count (+ count 1)))]
                [(dec) (lambda() (set count (- count 1)))]
                [(get) (lambda() count)]))))))


(define ob-self-msg!
  (let ([self `dummy])
    (begin
      (set! self
            (lambda(m)
              (case m
                [(first) (lambda(x) (msg self `second (+ x 1)))]
                [(second) (lambda(x) (+ x 1))]
                [(get) (lambda() count)])))) self))


(define (mt)
  (let ([self `dummy])
    (begin
      (set! self
            (lambda(m)
              (case m
                [(sum) (lambda() 0)])))
      self)))

(define [node v l r]
  (let ([self `dummy])
    (begin
      (set! self
            (lambda(m)
              (case m
                [(sum) (lambda() (+ v (msg 1 `sum) (msg r `sum)))]))))))