label avg29043(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc001_01 5', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with trans
play sfx2 "common_select.ogg"
get_char('c13') '[convertstrid(1100030)]' (**arg(1, 1100030))
return "avg29043"