label avg25060(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc002_01 3', 'p2', [mid(-3), light], 6)
$ update_narrator('c23')
window show
with trans
play sfxvoice "avg_vocal_ch22.ogg"
get_char('c23') '[convertstrid(1210174)]' (**arg(1, 1210174))
hide p2
$ update_portrait('oc001_01 8', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1210175)]' (**arg(2, 1210175))
hide p1
$ update_portrait('oc002_01 8', 'p2', [mid(-3), light], 6)
play sfx2 "common_36rewardsp.ogg"
play sfxvoice "avg_vocal_ch05.ogg"
get_char('c23') '[convertstrid(1210176)]' (**arg(3, 1210176))
return "avg25060"