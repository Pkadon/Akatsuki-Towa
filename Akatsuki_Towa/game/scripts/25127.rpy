label avg25127(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc001_01 7', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with trans
play sfx2 "other_7077.ogg"
play sfxvoice "avg_vocal_na15.ogg"
get_char('c13') '[convertstrid(1210374)]' (**arg(1, 1210374))
hide p1
$ update_portrait('oc002_01 17', 'p2', [mid(-3), light], 6)
play sfx2 "other_7077.ogg"
play sfxvoice "avg_vocal_ch10.ogg"
get_char('c23') '[convertstrid(1210375)]' (**arg(2, 1210375))
hide p2
$ update_portrait('oc001_01 10', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1210376)]' (**arg(3, 1210376))
hide p1
$ update_portrait('oc002_01 2', 'p2', [mid(-3), light], 6)
play sfx2 "other_7086.ogg"
play sfxvoice "avg_vocal_ch12.ogg"
get_char('c23') '[convertstrid(1210377)]' (**arg(4, 1210377))
hide p2
$ update_portrait('oc001_01 1', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1210378)]' (**arg(5, 1210378))
hide p1
$ update_portrait('oc002_01 17', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1210379)]' (**arg(6, 1210379))
hide p2
$ update_portrait('oc001_01 11', 'p1', [mid(-2), light], 6)
play sfx2 "common_36rewardsp.ogg"
play sfxvoice "avg_vocal_na17.ogg"
get_char('c13') '[convertstrid(1210380)]' (**arg(7, 1210380))
return "avg25127"