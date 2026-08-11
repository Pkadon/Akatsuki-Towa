label avg25232(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc002_01 12', 'p2', [mid(-3), light], 6)
$ update_narrator('c23')
window show
with trans
play sfx2 "fight_6024.ogg"
get_char('c23') '[convertstrid(1210826)]' (**arg(1, 1210826))
hide p2
$ update_portrait('oc001_01 19', 'p1', [mid(-2), light], 6)
play sfxvoice "bcv_oc001_hurt_02.ogg"
get_char('c13') '[convertstrid(1210827)]' (**arg(2, 1210827))
hide p1
$ update_portrait('oc002_01 4', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1210828)]' (**arg(3, 1210828))
return "avg25232"