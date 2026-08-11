label avg24011(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('st026_01 1', 'p225', [mid(-14), light], 6)
$ update_narrator('c2253')
window show
with trans
get_char('c2253') '[convertstrid(1200039)]' (**arg(1, 1200039))
hide p225
$ update_portrait('oc002_01 6', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1200040)]' (**arg(2, 1200040))
return "avg24011"