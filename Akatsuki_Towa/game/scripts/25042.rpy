label avg25042(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc002_01 2', 'p2', [mid(-3), light], 6)
$ update_narrator('c23')
window show
with trans
play sfx2 "fight_6025.ogg"
play sfxvoice "avg_vocal_ch12.ogg"
get_char('c23') '[convertstrid(1210107)]' (**arg(1, 1210107))
hide p2
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1210108)]' (**arg(2, 1210108))
return "avg25042"