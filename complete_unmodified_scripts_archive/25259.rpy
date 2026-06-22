label avg25259:

stop music
scene placeholderbackground
$ update_narrator('c20183')
window show
with fade_in
play sfx2 "other_7043.ogg"
get_char('c20183') '[convertstrid(1210966)]' (**arg(1, 1210966))
$ update_portrait('oc002_01 9', 'p2', [mid(-3), light], 6)
play sfxvoice "bcv_oc002_atk_01.ogg"
get_char('c23') '[convertstrid(1210967)]' (**arg(2, 1210967))
hide p2
play sfx2 "other_7091.ogg"
get_char('c20183') '[convertstrid(1210968)]' (**arg(3, 1210968))
play sfx2 "other_7086.ogg"
get_char('c0') '[convertstrid(1210969)]' (**arg(4, 1210969))
$ update_portrait('oc002_01 4', 'p2', [mid(-3), light], 6)
play sfx2 "fight_6026.ogg"
play sfxvoice "avg_vocal_ch13.ogg"
get_char('c23') '[convertstrid(1210970)]' (**arg(5, 1210970))
hide p2
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 6)
play sfxvoice "bcv_oc001_com_01.ogg"
get_char('c13') '[convertstrid(1210971)]' (**arg(6, 1210971))
return