label avg25178(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc001_01 8', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with trans
play sfx2 "other_7067.ogg"
get_char('c13') '[convertstrid(1210571)]' (**arg(1, 1210571))
hide p1
get_char('c20133') '[convertstrid(1210572)]' (**arg(2, 1210572))
$ update_portrait('oc001_01 23', 'p1', [mid(-2), light], 6)
play sfxvoice "avg_vocal_na20.ogg"
get_char('c13') '[convertstrid(1210573)]' (**arg(3, 1210573))
hide p1
play sfx2 "other_7039.ogg"
get_char('c20133') '[convertstrid(1210574)]' (**arg(4, 1210574))
$ update_portrait('oc002_01 6', 'p2', [mid(-3), light], 6)
play sfx2 "common_35rewardholy.ogg"
play sfxvoice "avg_vocal_ch09.ogg"
get_char('c23') '[convertstrid(1210575)]' (**arg(5, 1210575))
return "avg25178"