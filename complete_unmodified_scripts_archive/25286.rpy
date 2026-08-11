label avg25286(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc002_01 5', 'p2', [mid(-3), light], 6)
$ update_narrator('c23')
window show
with trans
play sfxvoice "avg_vocal_ch07.ogg"
get_char('c23') '[convertstrid(1211091)]' (**arg(1, 1211091))
hide p2
$ update_portrait('oc001_01 23', 'p1', [mid(-2), light], 6)
play sfxvoice "avg_vocal_na03.ogg"
get_char('c13') '[convertstrid(1211092)]' (**arg(2, 1211092))
hide p1
$ update_portrait('oc002_01 8', 'p2', [mid(-3), light], 6)
play sfx2 "other_7059.ogg"
get_char('c23') '[convertstrid(1211093)]' (**arg(3, 1211093))
hide p2
play sfx2 "other_7092.ogg"
get_char('c0') '[convertstrid(1211094)]' (**arg(4, 1211094))
$ update_portrait('oc002_01 17', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch21.ogg"
get_char('c23') '[convertstrid(1211095)]' (**arg(5, 1211095))
hide p2
$ update_portrait('oc001_01 7', 'p1', [mid(-2), light], 6)
play sfx2 "common_36rewardsp.ogg"
play sfxvoice "avg_vocal_na02.ogg"
get_char('c13') '[convertstrid(1211096)]' (**arg(6, 1211096))
return "avg25286"