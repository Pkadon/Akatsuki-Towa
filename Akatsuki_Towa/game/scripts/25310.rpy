label avg25310(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc002_01 3', 'p2', [mid(-3), light], 6)
$ update_narrator('c23')
window show
with trans
play sfxvoice "avg_vocal_ch23.ogg"
get_char('c23') '[convertstrid(1211187)]' (**arg(1, 1211187))
hide p2
$ update_portrait('oc001_01 18', 'p1', [mid(-2), light], 6)
play sfxvoice "avg_vocal_na03.ogg"
get_char('c13') '[convertstrid(1211188)]' (**arg(2, 1211188))
hide p1
$ update_portrait('oc002_01 9', 'p2', [mid(-3), light], 6)
play sfx2 "common_35rewardholy.ogg"
play sfxvoice "bcv_oc002_atk_01.ogg"
get_char('c23') '[convertstrid(1211189)]' (**arg(3, 1211189))
return "avg25310"