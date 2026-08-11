label avg25141(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc001_01 18', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with trans
play sfxvoice "avg_vocal_na06.ogg"
get_char('c13') '[convertstrid(1210438)]' (**arg(1, 1210438))
hide p1
$ update_portrait('oc002_01 9', 'p2', [mid(-3), light], 6)
play sfxvoice "bcv_oc002_atk_01.ogg"
get_char('c23') '[convertstrid(1210439)]' (**arg(2, 1210439))
hide p2
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1210440)]' (**arg(3, 1210440))
hide p1
play sfx2 "other_7004.ogg"
get_char('c0') '[convertstrid(1210441)]' (**arg(4, 1210441))
$ update_portrait('oc001_01 7', 'p1', [mid(-2), light], 6)
play sfx2 "common_35rewardholy.ogg"
play sfxvoice "avg_vocal_na05.ogg"
get_char('c13') '[convertstrid(1210442)]' (**arg(5, 1210442))
return "avg25141"