label avg25131(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('uc002_01 2', 'p2012', [mid(2), light], 6)
$ update_narrator('c20123')
window show
with trans
play sfx2 "other_7088.ogg"
get_char('c20123') '[convertstrid(1210391)]' (**arg(1, 1210391))
hide p2012
$ update_portrait('oc002_01 12', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch11.ogg"
get_char('c23') '[convertstrid(1210392)]' (**arg(2, 1210392))
hide p2
$ update_portrait('uc002_01 1', 'p2012', [mid(2), light], 6)
get_char('c20123') '[convertstrid(1210393)]' (**arg(3, 1210393))
hide p2012
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1210394)]' (**arg(4, 1210394))
hide p1
play sfx2 "other_7004.ogg"
get_char('c0') '[convertstrid(1210395)]' (**arg(5, 1210395))
$ update_portrait('oc001_01 8', 'p1', [mid(-2), light], 6)
play sfxvoice "avg_vocal_na05.ogg"
get_char('c13') '[convertstrid(1210396)]' (**arg(6, 1210396))
hide p1
$ update_portrait('uc002_01 1', 'p2012', [mid(2), light], 6)
play sfx2 "common_36rewardsp.ogg"
get_char('c20123') '[convertstrid(1210397)]' (**arg(7, 1210397))
return "avg25131"