label avg20012(trans=fade_in):

$ play_music("ed7150.ogg")
scene avg_bg_014
$ update_portrait('oc002_01 8', 'p2', [mid(-3), light], 6)
$ update_narrator('c23')
window show
with trans
play sfx2 "other_7064.ogg"
get_char('c23') '[convertstrid(1000906)]' (**arg(1, 1000906))
hide p2
$ update_portrait('oc001_01 7', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1000907)]' (**arg(2, 1000907))
hide p1
$ update_portrait('oc002_01 2', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1000908)]' (**arg(3, 1000908))
hide p2
$ update_portrait('oc001_01 8', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1000909)]' (**arg(4, 1000909))
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1000910)]' (**arg(5, 1000910))
$ update_portrait('oc001_01 10', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1000911)]' (**arg(6, 1000911))
hide p1
$ update_portrait('oc002_01 10', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch25.ogg"
get_char('c23') '[convertstrid(1000912)]' (**arg(7, 1000912))
hide p2
$ update_portrait('oc001_01 10', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1000913)]' (**arg(8, 1000913))
hide p1
$ update_portrait('oc002_01 8', 'p2', [mid(-3), light], 6)
play sfx2 "other_7091.ogg"
get_char('c23') '[convertstrid(1000914)]' (**arg(9, 1000914))
hide p2
$ update_portrait('oc001_01 12', 'p1', [mid(-2), r_shake, light], 6)
get_char('c13') '[convertstrid(1000915)]' (**arg(10, 1000915))
hide p1
$ update_portrait('oc002_01 1', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1000916)]' (**arg(11, 1000916))
hide p2
$ update_portrait('oc001_01 7', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1000917)]' (**arg(12, 1000917))
hide p1
$ update_portrait('oc002_01 8', 'p2', [mid(-3), light], 6)
play sfx2 "other_7075.ogg"
get_char('c23') '[convertstrid(1000918)]' (**arg(13, 1000918))
$ update_portrait('oc002_01 1', 'p2', [mid(-3), light], 6)
play sfx2 "other_7074.ogg"
get_char('c23') '[convertstrid(1000919)]' (**arg(14, 1000919))
hide p2
$ update_portrait('sc049_01 2', 'p524', [mid(-8), light], 6)
play sfx2 "other_7072.ogg"
get_char('c5243') '[convertstrid(1000920)]' (**arg(15, 1000920))
hide p524
$ update_portrait('oc002_01 1', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1000921)]' (**arg(16, 1000921))
$ update_portrait('oc002_01 4', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1000922)]' (**arg(17, 1000922))
hide p2
get_char('c0') '[convertstrid(1000923)]' (**arg(18, 1000923))
$ update_portrait('oc002_01 8', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1000924)]' (**arg(19, 1000924))
hide p2
$ update_portrait('oc001_01 8', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1000925)]' (**arg(20, 1000925))
hide p1
$ update_portrait('sc049_01 1', 'p524', [mid(-8), light], 6)
get_char('c5243') '[convertstrid(1000926)]' (**arg(21, 1000926))
hide p524
$ update_portrait('oc001_01 12', 'p1', [mid(-2), r_shake, light], 6)
play sfxvoice "avg_vocal_na21.ogg"
get_char('c13') '[convertstrid(1000927)]' (**arg(22, 1000927))
hide p1
$ update_portrait('sc049_01 2', 'p524', [mid(-8), light], 6)
get_char('c5243') '[convertstrid(1000928)]' (**arg(23, 1000928))
$ update_portrait('sc049_01 4', 'p524', [mid(-8), light], 6)
get_char('c5243') '[convertstrid(1000929)]' (**arg(24, 1000929))
$ update_portrait('sc049_01 1', 'p524', [mid(-8), light], 6)
get_char('c5243') '[convertstrid(1000930)]' (**arg(25, 1000930))
$ update_portrait('sc049_01 10', 'p524', [mid(-8), light], 6)
get_char('c5243') '[convertstrid(1000931)]' (**arg(26, 1000931))
hide p524
$ update_portrait('oc001_01 1', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1000932)]' (**arg(27, 1000932))
hide p1
$ update_portrait('sc049_01 6', 'p524', [mid(-8), light], 6)
get_char('c5243') '[convertstrid(1000933)]' (**arg(28, 1000933))
hide p524
$ update_portrait('oc002_01 6', 'p2', [mid(-3), light], 6)
play sfx2 "other_7073.ogg"
play sfxvoice "avg_vocal_ch08.ogg"
get_char('c23') '[convertstrid(1000934)]' (**arg(29, 1000934))
return "avg20012"