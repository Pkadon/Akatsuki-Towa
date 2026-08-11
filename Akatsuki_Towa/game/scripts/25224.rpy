label avg25224(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with trans
get_char('c13') '[convertstrid(1210787)]' (**arg(1, 1210787))
hide p1
$ update_portrait('oc002_01 4', 'p2', [mid(-3), light], 6)
play sfx2 "other_7088.ogg"
get_char('c23') '[convertstrid(1210788)]' (**arg(2, 1210788))
hide p2
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 6)
play sfxvoice "avg_vocal_na10.ogg"
get_char('c13') '[convertstrid(1210789)]' (**arg(3, 1210789))
return "avg25224"