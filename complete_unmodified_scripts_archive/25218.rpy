label avg25218:

stop music
scene placeholderbackground
$ update_portrait('oc002_01 12', 'p2', [mid(-3), light], 6)
$ update_narrator('c23')
window show
with fade_in
play sfx2 "fight_6020.ogg"
play sfxvoice "bcv_oc002_hurt_02.ogg"
get_char('c23') '[convertstrid(1210755)]' (**arg(1, 1210755))
hide p2
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1210756)]' (**arg(2, 1210756))
hide p1
$ update_portrait('oc002_01 21', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch25.ogg"
get_char('c23') '[convertstrid(1210757)]' (**arg(3, 1210757))
hide p2
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 6)
play sfxvoice "avg_vocal_na04.ogg"
get_char('c13') '[convertstrid(1210758)]' (**arg(4, 1210758))
return