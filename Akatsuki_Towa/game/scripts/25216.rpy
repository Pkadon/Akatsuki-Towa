label avg25216(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc001_01 8', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with trans
play sfx2 "other_7076.ogg"
play sfxvoice "avg_vocal_na05.ogg"
get_char('c13') '[convertstrid(1210746)]' (**arg(1, 1210746))
hide p1
$ update_portrait('oc002_01 4', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1210747)]' (**arg(2, 1210747))
hide p2
$ update_portrait('oc001_01 18', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1210748)]' (**arg(3, 1210748))
return "avg25216"