label avg19018:

stop music
scene avg_bg_023
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
$ update_narrator('c23')
window show
with fade_in
get_char('c23') '[convertstrid(1216173)]' (**arg(1, 1216173, size=(0.9)))
hide p2
$ update_portrait('sc049_01 10', 'p56', [r(-8), light], 6)
get_char('c563') '[convertstrid(1216174)]' (**arg(2, 1216174, size=(0.9)))
return