label avg101701(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc001_01 17', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with trans
get_char('c13') '[convertstrid(1221864)]' (**arg(1, 1221864))
hide p1
$ update_portrait('sc009_01 1', 'p17', [mid(-13), light], 6)
get_char('c173') '[convertstrid(1221865)]' (**arg(2, 1221865))
hide p17
$ update_portrait('oc001_01 12', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1221866)]' (**arg(3, 1221866))
hide p1
$ update_portrait('sc009_01 5', 'p17', [mid(-13), light], 6)
get_char('c173') '[convertstrid(1221867)]' (**arg(4, 1221867))
hide p17
$ update_portrait('oc001_01 10', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1221868)]' (**arg(5, 1221868))
return "avg101701"