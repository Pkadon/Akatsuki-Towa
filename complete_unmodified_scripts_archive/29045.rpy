label avg29045(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc001_01 12', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with trans
play sfx2 "other_7036.ogg"
get_char('c13') '[convertstrid(1100032)]' (**arg(1, 1100032))
return "avg29045"