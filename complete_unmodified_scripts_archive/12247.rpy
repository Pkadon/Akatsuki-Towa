label avg12247:

$ play_music("ed7105.ogg")
scene avg_bg_010
$ update_narrator('c21')
window show
with fade_in
$ update_portrait('oc002_01 12', 'p2', [l_entrance(-3), light, flip], 6)
get_char('c21') '[convertstrid(1121326)]' (**arg(1, 1121326))
$ update_portrait('oc002_01 12', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1121327)]' (**arg(2, 1121327))
hide p2
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1121328)]' (**arg(3, 1121328))
$ update_portrait('oc003_01 4', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1121329)]' (**arg(4, 1121329))
hide p3
hide p1
get_char('c0') '[convertstrid(1121330)]' (**arg(5, 1121330))
$ update_portrait('oc001_01 4', 'p1', [l(-2), light, flip], 6)
play sfx2 "fight_6024.ogg"
get_char('c11') '[convertstrid(1121331)]' (**arg(6, 1121331))
$ update_portrait('oc001_01 4', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc002_01 12', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1121332)]' (**arg(7, 1121332))
$ update_portrait('oc002_01 12', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 12', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1121333)]' (**arg(8, 1121333))
$ update_portrait('oc001_01 12', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc002_01 20', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1121334)]' (**arg(9, 1121334))
hide p2
$ update_portrait('oc003_01 12', 'p3', [r(-6), light], 6)
play sfxvoice "avg_vocal_ro09.ogg"
get_char('c33') '[convertstrid(1121335)]' (**arg(10, 1121335))
hide p1
$ update_portrait('oc003_01 12', 'p3', [r(-6), dark], 5)
play sfx2 "other_7077.ogg"
get_char('c20161') '[convertstrid(1121336)]' (**arg(11, 1121336))
hide p3
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na02.ogg"
get_char('c13') '[convertstrid(1121337)]' (**arg(12, 1121337))
hide p1
$ update_portrait('oc003_01 4', 'p3', [r_midback(-6), light], 6)
get_char('c33') '[convertstrid(1121338)]' (**arg(13, 1121338))
return