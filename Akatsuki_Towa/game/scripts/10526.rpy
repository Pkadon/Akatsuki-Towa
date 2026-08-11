label avg10526(trans=fade_in):

$ play_music("ED6103.ogg")
scene avg_bg_070
$ update_narrator('c0')
window show
with trans
play sfx2 "other_7047.ogg"
get_char('c0') '[convertstrid(1152185)]' (**arg(1, 1152185))
scene avg_bg_023
$ update_portrait('uc001_01 1', 'p1255', [l(-2), light, flip], 6)
$ update_narrator('c12551')
with fade
get_char('c12551') '[convertstrid(1152186)]' (**arg(2, 1152186))
$ update_portrait('uc001_01 1', 'p1255', [l(-2), dark, flip], 5)
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1152187)]' (**arg(3, 1152187))
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
$ update_portrait('uc001_01 1', 'p1255', [l(-2), light, flip], 6)
get_char('c12551') '[convertstrid(1152188)]' (**arg(4, 1152188))
hide p1
$ update_portrait('uc001_01 1', 'p1255', [l(-2), dark, flip], 5)
$ update_portrait('oc003_01 5', 'p3', [r(-6), light], 6)
play sfxvoice "avg_vocal_ro02.ogg"
get_char('c33') '[convertstrid(1152189)]' (**arg(5, 1152189))
$ update_portrait('oc003_01 5', 'p3', [r(-6), dark], 5)
$ update_portrait('uc001_01 1', 'p1255', [l(-2), light, flip], 6)
get_char('c12551') '[convertstrid(1152190)]' (**arg(6, 1152190))
hide p3
$ update_portrait('uc001_01 1', 'p1255', [l(-2), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1152191)]' (**arg(7, 1152191))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('uc001_01 1', 'p1255', [l(-2), light, flip], 6)
get_char('c12551') '[convertstrid(1152192)]' (**arg(8, 1152192))
hide p1
$ update_portrait('uc001_01 1', 'p1255', [l(-2), dark, flip], 5)
$ update_portrait('oc002_01 8', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1152193)]' (**arg(9, 1152193))
$ update_portrait('oc002_01 8', 'p2', [r(-3), dark], 5)
$ update_portrait('uc001_01 1', 'p1255', [l(-2), light, flip], 6)
get_char('c12551') '[convertstrid(1152194)]' (**arg(10, 1152194))
hide p2
$ update_portrait('uc001_01 1', 'p1255', [l(-2), dark, flip], 5)
$ update_portrait('oc003_01 8', 'p3', [r(-6), light], 6)
play sfxvoice "avg_vocal_ro13.ogg"
get_char('c33') '[convertstrid(1152195)]' (**arg(11, 1152195))
return "avg10526"