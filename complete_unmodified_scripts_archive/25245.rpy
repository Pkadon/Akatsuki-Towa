label avg25245(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with trans
get_char('c13') '[convertstrid(1210887)]' (**arg(1, 1210887))
hide p1
$ update_portrait('oc002_01 6', 'p2', [mid(-3), light], 6)
play sfx2 "fight_6025.ogg"
get_char('c23') '[convertstrid(1210888)]' (**arg(2, 1210888))
hide p2
$ update_portrait('oc001_01 11', 'p1', [mid(-2), light], 6)
play sfxvoice "avg_vocal_na17.ogg"
get_char('c13') '[convertstrid(1210889)]' (**arg(3, 1210889))
return "avg25245"