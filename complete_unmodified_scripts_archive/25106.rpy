label avg25106(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc002_01 8', 'p2', [mid(-3), light], 6)
$ update_narrator('c23')
window show
with trans
play sfxvoice "avg_vocal_ch05.ogg"
get_char('c23') '[convertstrid(1210301)]' (**arg(1, 1210301))
hide p2
get_char('c20073') '[convertstrid(1210302)]' (**arg(2, 1210302))
$ update_portrait('oc001_01 6', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1210303)]' (**arg(3, 1210303))
hide p1
play sfx2 "other_7051.ogg"
get_char('c20073') '[convertstrid(1210304)]' (**arg(4, 1210304))
$ update_portrait('oc002_01 12', 'p2', [mid(-3), light], 6)
play sfx2 "other_7092.ogg"
play sfxvoice "avg_vocal_ch11.ogg"
get_char('c23') '[convertstrid(1210305)]' (**arg(5, 1210305))
hide p2
$ update_portrait('oc001_01 7', 'p1', [mid(-2), light], 6)
play sfxvoice "avg_vocal_na05.ogg"
get_char('c13') '[convertstrid(1210306)]' (**arg(6, 1210306))
hide p1
get_char('c20073') '[convertstrid(1210307)]' (**arg(7, 1210307))
get_char('c20073') '[convertstrid(1210308)]' (**arg(8, 1210308))
$ update_portrait('oc001_01 8', 'p1', [mid(-2), light], 6)
play sfx2 "common_36rewardsp.ogg"
play sfxvoice "avg_vocal_na06.ogg"
get_char('c13') '[convertstrid(1210309)]' (**arg(9, 1210309))
return "avg25106"