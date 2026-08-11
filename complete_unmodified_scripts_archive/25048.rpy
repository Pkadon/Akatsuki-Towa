label avg25048(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc001_01 1', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with trans
play sfx2 "common_select.ogg"
get_char('c13') '[convertstrid(1210123)]' (**arg(1, 1210123))
hide p1
$ update_portrait('uc001_02 1', 'p2002', [mid(6), light], 6)
get_char('c20023') '[convertstrid(1210124)]' (**arg(2, 1210124))
return "avg25048"