label avg25804(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc002_01 2', 'p2', [mid(-3), light], 6)
$ update_narrator('c23')
window show
with trans
get_char('c23') '[convertstrid(1211259)]' (**arg(1, 1211259))
hide p2
$ update_portrait('oc001_01 11', 'p1', [mid(-2), light], 6)
play sfx2 "fight_6025.ogg"
play sfxvoice "avg_vocal_na03.ogg"
get_char('c13') '[convertstrid(1211260)]' (**arg(2, 1211260))
$ update_portrait('oc001_01 1', 'p1', [mid(-2), light], 6)
play sfx2 "fight_6026.ogg"
get_char('c13') '[convertstrid(1211261)]' (**arg(3, 1211261))
$ update_portrait('oc001_01 5', 'p1', [mid(-2), light], 6)
play sfx2 "other_7034.ogg"
play sfxvoice "bcv_oc001_win_02.ogg"
get_char('c13') '[convertstrid(1211262)]' (**arg(4, 1211262))
return "avg25804"