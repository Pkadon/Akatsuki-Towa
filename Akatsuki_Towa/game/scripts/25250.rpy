label avg25250:

stop music
scene placeholderbackground
$ update_portrait('oc002_01 2', 'p2', [mid(-3), light], 6)
$ update_narrator('c23')
window show
with fade_in
get_char('c23') '[convertstrid(1210913)]' (**arg(1, 1210913))
hide p2
get_char('c20153') '[convertstrid(1210914)]' (**arg(2, 1210914))
$ update_portrait('oc001_01 10', 'p1', [mid(-2), light], 6)
play sfxvoice "avg_vocal_na20.ogg"
get_char('c13') '[convertstrid(1210915)]' (**arg(3, 1210915))
hide p1
get_char('c20153') '[convertstrid(1210916)]' (**arg(4, 1210916))
$ update_portrait('oc002_01 5', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch07.ogg"
get_char('c23') '[convertstrid(1210917)]' (**arg(5, 1210917))
hide p2
play sfx2 "other_7007.ogg"
get_char('c20153') '[convertstrid(1210918)]' (**arg(6, 1210918))
play sfx2 "other_7086.ogg"
get_char('c0') '[convertstrid(1210919)]' (**arg(7, 1210919))
$ update_portrait('oc001_01 7', 'p1', [mid(-2), light], 6)
play sfxvoice "avg_vocal_na05.ogg"
get_char('c13') '[convertstrid(1210920)]' (**arg(8, 1210920))
hide p1
$ update_portrait('oc002_01 19', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch25.ogg"
get_char('c23') '[convertstrid(1210921)]' (**arg(9, 1210921))
hide p2
$ update_portrait('oc001_01 8', 'p1', [mid(-2), light], 6)
play sfx2 "common_35rewardholy.ogg"
get_char('c13') '[convertstrid(1210922)]' (**arg(10, 1210922))
return