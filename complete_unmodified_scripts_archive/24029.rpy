label avg24029(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc001_01 1', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with trans
get_char('c13') '[convertstrid(1200120)]' (**arg(1, 1200120))
hide p1
get_char('c10153') '[convertstrid(1200121)]' (**arg(2, 1200121))
$ update_portrait('oc001_01 1', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1200122)]' (**arg(3, 1200122))
return "avg24029"