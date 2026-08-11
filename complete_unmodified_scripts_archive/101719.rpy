label avg101719(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('sc009_01 5', 'p17', [mid(-13), light], 6)
$ update_narrator('c173')
window show
with trans
get_char('c173') '[convertstrid(1221920)]' (**arg(1, 1221920))
hide p17
$ update_portrait('oc001_01 1', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1221921)]' (**arg(2, 1221921))
hide p1
$ update_portrait('sc009_01 1', 'p17', [mid(-13), light], 6)
get_char('c173') '[convertstrid(1221922)]' (**arg(3, 1221922))
$ update_portrait('sc009_01 4', 'p17', [mid(-13), light], 6)
get_char('c173') '[convertstrid(1221923)]' (**arg(4, 1221923))
hide p17
$ update_portrait('oc001_01 22', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1221924)]' (**arg(5, 1221924))
return "avg101719"