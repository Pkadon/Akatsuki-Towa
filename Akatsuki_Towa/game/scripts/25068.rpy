label avg25068(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc002_01 14', 'p2', [mid(-3), light], 6)
$ update_narrator('c23')
window show
with trans
get_char('c23') '[convertstrid(1210209)]' (**arg(1, 1210209))
hide p2
$ update_portrait('oc001_01 8', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1210210)]' (**arg(2, 1210210))
hide p1
$ update_portrait('oc002_01 18', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1210211)]' (**arg(3, 1210211))
hide p2
$ update_portrait('oc001_01 8', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1210212)]' (**arg(4, 1210212))
$ update_portrait('oc001_01 12', 'p1', [mid(-2), light], 6)
play sfx2 "fight_6025.ogg"
play sfxvoice "avg_vocal_na21.ogg"
get_char('c13') '[convertstrid(1210213)]' (**arg(5, 1210213))
$ update_portrait('oc001_01 14', 'p1', [mid(-2), light], 6)
play sfx2 "elc_5004.ogg"
play sfxvoice "bcv_oc001_hurt_02.ogg"
get_char('c13') '[convertstrid(1210214)]' (**arg(6, 1210214))
hide p1
$ update_portrait('oc002_01 20', 'p2', [mid(-3), light], 6)
play sfx2 "elc_5003.ogg"
play sfxvoice "avg_vocal_ch23.ogg"
get_char('c23') '[convertstrid(1210215)]' (**arg(7, 1210215))
$ update_portrait('oc002_01 2', 'p2', [mid(-3), light], 6)
play sfx2 "other_7001.ogg"
play sfxvoice "avg_vocal_ch12.ogg"
get_char('c23') '[convertstrid(1210216)]' (**arg(8, 1210216))
hide p2
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1210217)]' (**arg(9, 1210217))
hide p1
$ update_portrait('oc002_01 6', 'p2', [mid(-3), light], 6)
play sfx2 "common_tag_2.ogg"
play sfxvoice "avg_vocal_ch08.ogg"
get_char('c23') '[convertstrid(1210218)]' (**arg(10, 1210218))
hide p2
$ update_portrait('oc001_01 11', 'p1', [mid(-2), light], 6)
play sfx2 "common_36rewardsp.ogg"
play sfxvoice "avg_vocal_na20.ogg"
get_char('c13') '[convertstrid(1210219)]' (**arg(11, 1210219))
return "avg25068"