label avg25211(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with trans
play sfx2 "other_7059.ogg"
get_char('c13') '[convertstrid(1210732)]' (**arg(1, 1210732))
hide p1
$ update_portrait('oc002_01 5', 'p2', [mid(-3), light], 6)
play sfx2 "common_35rewardholy.ogg"
play sfxvoice "avg_vocal_ch07.ogg"
get_char('c23') '[convertstrid(1210733)]' (**arg(2, 1210733))
hide p2
$ update_portrait('oc001_01 8', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1210734)]' (**arg(3, 1210734))
hide p1
$ update_portrait('oc002_01 9', 'p2', [mid(-3), light], 6)
play sfxvoice "bcv_oc002_arts_03.ogg"
get_char('c23') '[convertstrid(1210735)]' (**arg(4, 1210735))
hide p2
$ update_portrait('oc001_01 6', 'p1', [mid(-2), light], 6)
play sfx2 "common_36rewardsp.ogg"
play sfxvoice "avg_vocal_na20.ogg"
get_char('c13') '[convertstrid(1210736)]' (**arg(5, 1210736))
return "avg25211"