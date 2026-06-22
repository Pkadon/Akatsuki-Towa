label avg12567:

$ play_music("ED6102.ogg")
scene avg_bg_023
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
$ update_narrator('c23')
window show
with fade_in
get_char('c23') '[convertstrid(1155091)]' (**arg(1, 1155091))
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
get_char('c12321') '[convertstrid(1155092)]' (**arg(2, 1155092))
hide p2
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1155093)]' (**arg(3, 1155093))
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 17', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1155094)]' (**arg(4, 1155094))
hide p1
$ update_portrait('oc003_01 17', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc002_01 8', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1155095)]' (**arg(5, 1155095))
hide p3
$ update_portrait('oc002_01 8', 'p2', [r(-3), dark], 5)
$ update_portrait('oc004_01 5', 'p4', [l(-5), light, flip], 6)
play sfxvoice "avg_vocal_li30.ogg"
get_char('c41') '[convertstrid(1155096)]' (**arg(6, 1155096))
$ update_portrait('oc004_01 5', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc002_01 12', 'p2', [r(-3), light], 6)
play sfxvoice "avg_vocal_ch11.ogg"
get_char('c23') '[convertstrid(1155097)]' (**arg(7, 1155097))
hide p2
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1155098)]' (**arg(8, 1155098))
hide p4
$ update_portrait('oc001_01 7', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 5', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1155099)]' (**arg(9, 1155099))
hide p3
get_char('c12321') '[convertstrid(1155100)]' (**arg(10, 1155100))
return