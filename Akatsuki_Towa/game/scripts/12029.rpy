label avg12029:

$ play_music("ed7150.ogg")
scene avg_bg_014
$ update_narrator('c9693')
window show
with fade_in
play sfx2 "other_7046.ogg"
get_char('c9693') '[convertstrid(1120114)]' (**arg(1, 1120114))
$ update_portrait('oc001_01 1', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1120115)]' (**arg(2, 1120115))
$ update_portrait('oc001_01 1', 'p1', [l(-2), dark, flip], 5)
get_char('c9693') '[convertstrid(1120116)]' (**arg(3, 1120116))
hide p1
$ update_portrait('oc002_01 1', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1120117)]' (**arg(4, 1120117))
$ update_portrait('oc002_01 1', 'p2', [l(-3), dark, flip], 5)
get_char('c9693') '[convertstrid(1120118)]' (**arg(5, 1120118))
hide p2
get_char('c0') '[convertstrid(1120119)]' (**arg(6, 1120119))
get_char('c9691') '[convertstrid(1120120)]' (**arg(7, 1120120))
$ update_portrait('oc001_01 12', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na21.ogg"
get_char('c13') '[convertstrid(1120121)]' (**arg(8, 1120121))
$ update_portrait('oc001_01 12', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 12', 'p2', [l(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch11.ogg"
get_char('c21') '[convertstrid(1120122)]' (**arg(9, 1120122))
$ update_portrait('oc002_01 12', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1120123)]' (**arg(10, 1120123))
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1120124)]' (**arg(11, 1120124))
hide p2
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
get_char('c9691') '[convertstrid(1120125)]' (**arg(12, 1120125))
hide p1
$ update_portrait('oc002_01 5', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1120126)]' (**arg(13, 1120126))
return