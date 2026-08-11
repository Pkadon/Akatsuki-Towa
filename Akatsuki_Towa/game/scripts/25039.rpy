label avg25039(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc002_01 11', 'p2', [mid(-3), light], 6)
$ update_narrator('c23')
window show
with trans
get_char('c23') '[convertstrid(1210099)]' (**arg(1, 1210099))
hide p2
$ update_portrait('oc001_01 8', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1210100)]' (**arg(2, 1210100))
hide p1
$ update_portrait('oc002_01 8', 'p2', [mid(-3), light], 6)
play sfx2 "common_36rewardsp.ogg"
play sfxvoice "bcv_oc002_win_02.ogg"
get_char('c23') '[convertstrid(1210101)]' (**arg(3, 1210101))
return "avg25039"