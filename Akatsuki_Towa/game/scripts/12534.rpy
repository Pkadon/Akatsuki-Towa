label avg12534:

$ play_music("ED6301.ogg")
scene placeholderbackground
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
$ update_narrator('c31')
window show
with fade_in
get_char('c31') '[convertstrid(1151733)]' (**arg(1, 1151733))
$ update_portrait('oc003_01 4', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc002_01 10', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1151734)]' (**arg(2, 1151734))
hide p2
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1151735)]' (**arg(3, 1151735))
hide p3
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 24', 'p4', [l(-5), light, flip], 6)
play sfxvoice "avg_vocal_li11.ogg"
get_char('c41') '[convertstrid(1151736)]' (**arg(4, 1151736))
hide p4
hide p1
get_char('c0') '[convertstrid(1151737)]' (**arg(5, 1151737))
$ update_portrait('oc004_01 15', 'p4', [l(-5), light, flip], 6)
play sfxvoice "avg_vocal_li27.ogg"
get_char('c41') '[convertstrid(1151738)]' (**arg(6, 1151738)) with shake
$ update_portrait('oc004_01 15', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc002_01 12', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1151739)]' (**arg(7, 1151739))
hide p4
$ update_portrait('oc002_01 12', 'p2', [r(-3), dark], 5)
$ update_portrait('oc003_01 17', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1151740)]' (**arg(8, 1151740))
$ update_portrait('oc003_01 16', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1151741)]' (**arg(9, 1151741))
$ update_portrait('oc003_01 2', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1151742)]' (**arg(10, 1151742))
hide p3
hide p2
$ update_narrator('c13')
with fade
$ update_portrait('oc001_01 4', 'p1', [r_entrance(-2), light], 6)
get_char('c13') '[convertstrid(1151743)]' (**arg(11, 1151743))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 12', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1151744)]' (**arg(12, 1151744))
$ update_portrait('oc003_01 12', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1151745)]' (**arg(13, 1151745))
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 8', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1151746)]' (**arg(14, 1151746))
return