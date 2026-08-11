label avg25134(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with trans
play sfx2 "fight_6022.ogg"
play sfxvoice "avg_vocal_na18.ogg"
get_char('c13') '[convertstrid(1210405)]' (**arg(1, 1210405))
hide p1
$ update_portrait('oc002_01 6', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch08.ogg"
get_char('c23') '[convertstrid(1210406)]' (**arg(2, 1210406))
hide p2
$ update_portrait('oc001_01 11', 'p1', [mid(-2), light], 6)
play sfx2 "other_7088.ogg"
get_char('c13') '[convertstrid(1210407)]' (**arg(3, 1210407))
hide p1
$ update_portrait('oc002_01 8', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch06.ogg"
get_char('c23') '[convertstrid(1210408)]' (**arg(4, 1210408))
return "avg25134"