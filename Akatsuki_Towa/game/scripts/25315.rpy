label avg25315:

stop music
scene placeholderbackground
$ update_portrait('oc002_01 14', 'p2', [mid(-3), light], 6)
$ update_narrator('c23')
window show
with fade_in
play sfx2 "other_7051.ogg"
play sfxvoice "avg_vocal_ch06.ogg"
get_char('c23') '[convertstrid(1211210)]' (**arg(1, 1211210))
hide p2
$ update_portrait('oc001_01 6', 'p1', [mid(-2), light], 6)
play sfxvoice "avg_vocal_na16.ogg"
get_char('c13') '[convertstrid(1211211)]' (**arg(2, 1211211))
hide p1
$ update_portrait('oc002_01 8', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1211212)]' (**arg(3, 1211212))
hide p2
play sfx2 "other_7093.ogg"
get_char('c20153') '[convertstrid(1211213)]' (**arg(4, 1211213))
$ update_portrait('oc001_01 22', 'p1', [mid(-2), light], 6)
play sfxvoice "avg_vocal_na18.ogg"
get_char('c13') '[convertstrid(1211214)]' (**arg(5, 1211214))
hide p1
get_char('c20153') '[convertstrid(1211215)]' (**arg(6, 1211215))
$ update_portrait('oc002_01 5', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch07.ogg"
get_char('c23') '[convertstrid(1211216)]' (**arg(7, 1211216))
hide p2
get_char('c20153') '[convertstrid(1211217)]' (**arg(8, 1211217))
play sfx2 "other_7086.ogg"
get_char('c0') '[convertstrid(1211218)]' (**arg(9, 1211218))
$ update_portrait('oc001_01 7', 'p1', [mid(-2), light], 6)
play sfx2 "common_35rewardholy.ogg"
play sfxvoice "avg_vocal_na02.ogg"
get_char('c13') '[convertstrid(1211219)]' (**arg(10, 1211219))
return