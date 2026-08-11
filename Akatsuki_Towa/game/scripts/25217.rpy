label avg25217(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc001_01 12', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with trans
play sfx2 "other_7079.ogg"
play sfxvoice "avg_vocal_na21.ogg"
get_char('c13') '[convertstrid(1210749)]' (**arg(1, 1210749))
hide p1
get_char('c20233') '[convertstrid(1210750)]' (**arg(2, 1210750))
$ update_portrait('oc002_01 12', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1210751)]' (**arg(3, 1210751))
hide p2
play sfx2 "other_7076.ogg"
get_char('c20233') '[convertstrid(1210752)]' (**arg(4, 1210752))
$ update_portrait('oc001_01 8', 'p1', [mid(-2), light], 6)
play sfx2 "common_35rewardholy.ogg"
play sfxvoice "avg_vocal_na05.ogg"
get_char('c13') '[convertstrid(1210753)]' (**arg(5, 1210753))
return "avg25217"