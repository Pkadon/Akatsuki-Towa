label avg20052(trans=fade_in):

$ play_music("ed7151.ogg")
scene placeholderbackground
$ update_portrait('oc001_01 4', 'p1', [l(-2), light, flip], 6)
$ update_narrator('c11')
window show
with trans
get_char('c11') '[convertstrid(1002801)]' (**arg(1, 1002801))
hide p1
get_char('c0') '[convertstrid(1002802)]' (**arg(2, 1002802))
get_char('c5993') '[convertstrid(1002803)]' (**arg(3, 1002803))
get_char('c5993') '[convertstrid(1002804)]' (**arg(4, 1002804))
$ update_portrait('oc002_01 4', 'p2', [l(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch24.ogg"
get_char('c21') '[convertstrid(1002805)]' (**arg(5, 1002805))
$ update_portrait('oc002_01 4', 'p2', [l(-3), dark, flip], 5)
get_char('c5993') '[convertstrid(1002806)]' (**arg(6, 1002806))
hide p2
$ update_portrait('oc001_01 8', 'p1', [l(-2), light, flip], 6)
play sfxvoice "avg_vocal_na05.ogg"
get_char('c11') '[convertstrid(1002807)]' (**arg(7, 1002807))
$ update_portrait('oc001_01 8', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc003_01 1', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1002808)]' (**arg(8, 1002808))
hide p3
get_char('c5993') '[convertstrid(1002809)]' (**arg(9, 1002809))
hide p1
$ update_portrait('oc001_01 4', 'p1', [l(-2), light, flip], 6)
$ update_narrator('c11')
with fade
get_char('c11') '[convertstrid(1002810)]' (**arg(10, 1002810))
$ update_portrait('oc001_01 4', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc003_01 4', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1002811)]' (**arg(11, 1002811))
$ play_music("ed7511.ogg")
$ update_portrait('oc003_01 4', 'p3', [r(-6), dark], 5)
$ update_portrait('oc001_01 2', 'p1', [l(-2), light, flip], 6)
play sfx2 "other_7085.ogg"
get_char('c11') '[convertstrid(1002812)]' (**arg(12, 1002812))
hide p3
$ update_portrait('oc001_01 2', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1002813)]' (**arg(13, 1002813))
hide p1
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
get_char('c5991') '[convertstrid(1002814)]' (**arg(14, 1002814))
get_char('c5991') '[convertstrid(1002815)]' (**arg(15, 1002815))
hide p2
play sfx2 "other_7085.ogg"
get_char('c0') '[convertstrid(1002816)]' (**arg(16, 1002816))
get_char('c0') '[convertstrid(1002817)]' (**arg(17, 1002817))
$ play_music("ed7151.ogg")
$ update_portrait('oc004_01 1', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1002818)]' (**arg(18, 1002818))
$ update_portrait('oc004_01 1', 'p4', [r(-5), dark], 5)
get_char('c5991') '[convertstrid(1002819)]' (**arg(19, 1002819))
hide p4
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1002820)]' (**arg(20, 1002820))
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
get_char('c5991') '[convertstrid(1002821)]' (**arg(21, 1002821))
get_char('c5991') '[convertstrid(1002822)]' (**arg(22, 1002822))
hide p1
$ update_portrait('oc004_01 2', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1002823)]' (**arg(23, 1002823))
$ update_portrait('oc004_01 2', 'p4', [r(-5), dark], 5)
get_char('c5991') '[convertstrid(1002824)]' (**arg(24, 1002824))
$ update_portrait('oc004_01 2', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1002825)]' (**arg(25, 1002825))
$ update_portrait('oc004_01 2', 'p4', [r(-5), dark], 5)
get_char('c5991') '[convertstrid(1002826)]' (**arg(26, 1002826))
get_char('c5991') '[convertstrid(1002827)]' (**arg(27, 1002827))
get_char('c5991') '[convertstrid(1002828)]' (**arg(28, 1002828))
get_char('c5991') '[convertstrid(1002829)]' (**arg(29, 1002829))
$ update_portrait('oc004_01 9', 'p4', [r(-5), light], 6)
play sfxvoice "avg_vocal_li05.ogg"
get_char('c43') '[convertstrid(1002830)]' (**arg(30, 1002830))
$ update_portrait('oc004_01 9', 'p4', [r(-5), dark], 5)
$ update_portrait('oc002_01 1', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1002831)]' (**arg(31, 1002831))
hide p4
$ update_portrait('oc002_01 1', 'p2', [l(-3), dark, flip], 5)
get_char('c5993') '[convertstrid(1002832)]' (**arg(32, 1002832))
return "avg20052"