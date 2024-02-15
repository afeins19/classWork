#lang plait

(test (interp (parse `{let ([x 1])}
                     {let {[x 2]}
                     {let {[z 3]}
                     {+ x
                        {unlet x
                               {+x z}}}}}

                     ) met-env) (interp (parse `6) mt-env))


