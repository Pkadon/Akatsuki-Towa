label avg12464:

$ play_music("ed7116.ogg")
scene avg_bg_020
$ update_narrator('c0')
window show
with fade_in
get_char('c0') '[convertstrid(1143858)]' (**arg(1, 1143858))
$ update_portrait('oc003_01 17', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1143859)]' (**arg(2, 1143859))
$ update_portrait('oc003_01 17', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1143860)]' (**arg(3, 1143860))
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
$ update_portrait('oc003_01 17', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1143861)]' (**arg(4, 1143861))
$ update_portrait('oc003_01 8', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1143862)]' (**arg(5, 1143862))
$ update_portrait('oc003_01 8', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc002_01 10', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1143863)]' (**arg(6, 1143863))
hide p3
$ update_portrait('oc002_01 10', 'p2', [r(-3), dark], 5)
$ update_portrait('oc004_01 7', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1143864)]' (**arg(7, 1143864))
hide p4
hide p2
get_char('c0') '[convertstrid(1143865)]' (**arg(8, 1143865))
$ update_portrait('oc002_01 10', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1143866)]' (**arg(9, 1143866))
$ update_portrait('oc002_01 10', 'p2', [r(-3), dark], 5)
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1143867)]' (**arg(10, 1143867))
hide p2
$ update_portrait('oc003_01 4', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc004_01 8', 'p4', [r(-5), light], 6)
play sfxvoice "avg_vocal_li15.ogg"
get_char('c43') '[convertstrid(1143868)]' (**arg(11, 1143868))
return