label avg24038:

stop music
scene placeholderbackground
$ update_portrait('oc002_01 1', 'p2', [mid(-3), light], 6)
$ update_narrator('c23')
window show
with fade_in
get_char('c23') '[convertstrid(1200153)]' (**arg(1, 1200153))
hide p2
get_char('c7623') '[convertstrid(1200154)]' (**arg(2, 1200154))
get_char('c7623') '[convertstrid(1200155)]' (**arg(3, 1200155))
$ update_portrait('oc002_01 8', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1200156)]' (**arg(4, 1200156))
return