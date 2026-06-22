label avg25195:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 1', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
get_char('c13') '[convertstrid(1210655)]' (**arg(1, 1210655))
hide p1
play sfx2 "other_7039.ogg"
get_char('c20133') '[convertstrid(1210656)]' (**arg(2, 1210656))
play sfx2 "other_7092.ogg"
get_char('c0') '[convertstrid(1210657)]' (**arg(3, 1210657))
$ update_portrait('oc002_01 14', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch08.ogg"
get_char('c23') '[convertstrid(1210658)]' (**arg(4, 1210658))
hide p2
$ update_portrait('oc001_01 10', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1210659)]' (**arg(5, 1210659))
hide p1
get_char('c20133') '[convertstrid(1210660)]' (**arg(6, 1210660))
$ update_portrait('oc001_01 21', 'p1', [mid(-2), light], 6)
play sfx2 "common_35rewardholy.ogg"
play sfxvoice "avg_vocal_na16.ogg"
get_char('c13') '[convertstrid(1210661)]' (**arg(7, 1210661))
return