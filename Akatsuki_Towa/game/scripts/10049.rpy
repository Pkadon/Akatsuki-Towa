label avg10049(trans=fade_in):

$ play_music("ed7150.ogg")
scene avg_bg_023
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
window show
with trans
play sfxvoice "avg_vocal_na15.ogg"
get_char('c13') '[convertstrid(1004117)]' (**arg(1, 1004117))
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
$ update_portrait('sc042_01 1', 'p49', [l(-19), light, flip], 6)
get_char('c491') '[convertstrid(1004118)]' (**arg(2, 1004118))
hide p49
$ update_portrait('oc003_01 7', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1004127)]' (**arg(3, 1004127))
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1004128)]' (**arg(4, 1004128))
$ update_portrait('oc003_01 8', 'p3', [l(-6), light, flip], 6)
play sfxvoice "avg_vocal_ro13.ogg"
get_char('c31') '[convertstrid(1004129)]' (**arg(5, 1004129))
hide p1
$ update_portrait('oc003_01 8', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('sc042_01 5', 'p49', [r(-19), light], 6)
get_char('c493') '[convertstrid(1004130)]' (**arg(6, 1004130))
hide p49
$ update_portrait('oc002_01 4', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1004131)]' (**arg(7, 1004131))
hide p3
$ update_portrait('oc002_01 4', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 18', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1004132)]' (**arg(8, 1004132))
$ update_portrait('oc001_01 4', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1004133)]' (**arg(9, 1004133))
$ update_portrait('oc001_01 4', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1004134)]' (**arg(10, 1004134))
hide p2
$ update_portrait('oc003_01 4', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1004135)]' (**arg(11, 1004135))
$ update_portrait('oc003_01 4', 'p3', [r(-6), dark], 5)
$ update_portrait('oc001_01 4', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1004136)]' (**arg(12, 1004136))
hide p3
$ update_portrait('oc001_01 4', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc004_01 2', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1004137)]' (**arg(13, 1004137))
$ update_portrait('oc004_01 2', 'p4', [r(-5), dark], 5)
$ update_portrait('oc001_01 4', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1004138)]' (**arg(14, 1004138))
hide p4
$ update_portrait('oc001_01 4', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('sc042_01 4', 'p49', [r(-19), light], 6)
get_char('c493') '[convertstrid(1001032)]' (**arg(15, 1001032))
hide p1
$ update_portrait('sc042_01 4', 'p49', [r(-19), dark], 5)
$ update_portrait('oc003_01 2', 'p3', [l(-6), light, flip], 6)
play sfx2 "other_7071.ogg"
get_char('c31') '[convertstrid(1004140)]' (**arg(16, 1004140))
hide p49
$ update_portrait('oc003_01 2', 'p3', [l(-6), dark, flip], 5)
play sfx2 "other_7072.ogg"
play sfxvoice "avg_vocal_ji10.ogg"
get_char('c5583') '[convertstrid(1004141)]' (**arg(17, 1004141))
$ update_portrait('oc003_01 1', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1004142)]' (**arg(18, 1004142))
$ update_portrait('oc003_01 1', 'p3', [l(-6), dark, flip], 5)
get_char('c5583') '[convertstrid(1004143)]' (**arg(19, 1004143))
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1004144)]' (**arg(20, 1004144))
$ update_portrait('oc003_01 4', 'p3', [l(-6), dark, flip], 5)
play sfxvoice "avg_vocal_ji05.ogg"
get_char('c5583') '[convertstrid(1004145)]' (**arg(21, 1004145))
hide p3
$ update_portrait('oc001_01 4', 'p1', [l(-2), light, flip], 6)
play sfx2 "other_7073.ogg"
get_char('c11') '[convertstrid(1004146)]' (**arg(22, 1004146))
$ update_portrait('oc001_01 4', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc002_01 9', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1004147)]' (**arg(23, 1004147))
hide p2
$ update_portrait('sc042_01 1', 'p49', [r(-19), light], 6)
get_char('c493') '[convertstrid(1004148)]' (**arg(24, 1004148))
hide p1
$ update_portrait('sc042_01 1', 'p49', [r(-19), dark], 5)
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1004149)]' (**arg(25, 1004149))
return "avg10049"