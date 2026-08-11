label avg25135(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc001_01 21', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with trans
get_char('c13') '[convertstrid(1210409)]' (**arg(1, 1210409))
hide p1
get_char('c20133') '[convertstrid(1210410)]' (**arg(2, 1210410))
$ update_portrait('oc002_01 6', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch10.ogg"
get_char('c23') '[convertstrid(1210411)]' (**arg(3, 1210411))
hide p2
get_char('c20133') '[convertstrid(1210412)]' (**arg(4, 1210412))
$ update_portrait('oc002_01 13', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch05.ogg"
get_char('c23') '[convertstrid(1210413)]' (**arg(5, 1210413))
hide p2
play sfx2 "other_7039.ogg"
get_char('c20133') '[convertstrid(1210414)]' (**arg(6, 1210414))
$ update_portrait('oc001_01 6', 'p1', [mid(-2), light], 6)
play sfx2 "common_35rewardholy.ogg"
play sfxvoice "avg_vocal_na17.ogg"
get_char('c13') '[convertstrid(1210415)]' (**arg(7, 1210415))
return "avg25135"