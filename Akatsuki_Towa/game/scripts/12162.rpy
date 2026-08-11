label avg12162(trans=fade_in):

$ play_music("ED6104.ogg")
scene avg_bg_011
$ update_narrator('c9661')
window show
with trans
play sfx2 "other_7047.ogg"
get_char('c9661') '[convertstrid(1128445)]' (**arg(1, 1128445))
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1128446)]' (**arg(2, 1128446))
hide p1
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1128447)]' (**arg(3, 1128447))
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
get_char('c9641') '[convertstrid(1128448)]' (**arg(4, 1128448))
hide p2
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1128449)]' (**arg(5, 1128449))
hide p1
$ update_portrait('oc003_01 4', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1128451)]' (**arg(6, 1128451))
$ update_portrait('oc003_01 4', 'p3', [r(-6), dark], 5)
get_char('c9641') '[convertstrid(1128452)]' (**arg(7, 1128452))
hide p3
$ update_portrait('oc001_01 11', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1128453)]' (**arg(8, 1128453))
$ update_portrait('oc001_01 11', 'p1', [r(-2), dark], 5)
get_char('c9641') '[convertstrid(1128454)]' (**arg(9, 1128454))
get_char('c9641') '[convertstrid(1128455)]' (**arg(10, 1128455))
hide p1
$ update_portrait('oc003_01 12', 'p3', [r(-6), light], 6)
play sfxvoice "avg_vocal_ro09.ogg"
get_char('c33') '[convertstrid(1128456)]' (**arg(11, 1128456))
hide p3
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1128457)]' (**arg(12, 1128457))
hide p1
$ update_portrait('oc002_01 21', 'p2', [r(-3), light], 6)
play sfxvoice "avg_vocal_ch25.ogg"
get_char('c23') '[convertstrid(1128458)]' (**arg(13, 1128458))
$ update_portrait('oc002_01 21', 'p2', [r(-3), dark], 5)
get_char('c9641') '[convertstrid(1128459)]' (**arg(14, 1128459))
$ play_music("ed7511.ogg")
hide p2
play sfx2 "other_7080.ogg"
get_char('c5003') '[convertstrid(1128460)]' (**arg(15, 1128460)) with shake
get_char('c9641') '[convertstrid(1128461)]' (**arg(16, 1128461))
$ update_portrait('oc001_01 9', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1128462)]' (**arg(17, 1128462))
$ update_portrait('oc001_01 9', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 8', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1128463)]' (**arg(18, 1128463))
hide p3
$ update_portrait('oc002_01 9', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1128464)]' (**arg(19, 1128464))
scene avg_bg_070
$ update_portrait('oc001_01 3', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
with fade
play sfx2 "other_7085.ogg"
play sfxvoice "avg_vocal_na21.ogg"
get_char('c13') '[convertstrid(1128465)]' (**arg(20, 1128465)) with shake
scene avg_bg_011
$ update_portrait('oc003_01 3', 'p3', [l(-6), light, flip], 6)
$ update_narrator('c31')
with fade
get_char('c31') '[convertstrid(1128467)]' (**arg(21, 1128467))
$ update_portrait('oc003_01 3', 'p3', [l(-6), dark, flip], 5)
get_char('c9643') '[convertstrid(1128468)]' (**arg(22, 1128468))
$ update_portrait('oc003_01 7', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1128469)]' (**arg(23, 1128469))
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1128470)]' (**arg(24, 1128470))
$ update_portrait('oc003_01 4', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 15', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1128471)]' (**arg(25, 1128471))
hide p1
get_char('c9643') '[convertstrid(1128472)]' (**arg(26, 1128472))
hide p3
$ update_portrait('oc002_01 21', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1128473)]' (**arg(27, 1128473))
$ update_portrait('oc002_01 21', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 13', 'p1', [r(-2), light], 6)
play sfx2 "other_7079.ogg"
get_char('c13') '[convertstrid(1128474)]' (**arg(28, 1128474))
return "avg12162"