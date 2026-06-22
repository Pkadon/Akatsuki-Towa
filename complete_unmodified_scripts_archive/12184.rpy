label avg12184:

$ play_music("ed7513.ogg")
scene avg_bg_070
$ update_narrator('c0')
window show
with fade_in
get_char('c0') '[convertstrid(1120664)]' (**arg(1, 1120664))
get_char('c0') '[convertstrid(1120665)]' (**arg(2, 1120665))
scene avg_bg_004
$ update_narrator('c0')
with fade
play sfx2 "other_7040.ogg"
get_char('c0') '[convertstrid(1120666)]' (**arg(3, 1120666))
$ update_portrait('oc001_01 17', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1120667)]' (**arg(4, 1120667))
$ update_portrait('oc001_01 12', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1120668)]' (**arg(5, 1120668))
$ update_portrait('oc001_01 13', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1120669)]' (**arg(6, 1120669))
$ update_portrait('oc001_01 19', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na07.ogg"
get_char('c13') '[convertstrid(1120670)]' (**arg(7, 1120670))
$ update_portrait('oc001_01 16', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1120671)]' (**arg(8, 1120671))
$ update_portrait('oc001_01 17', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1120672)]' (**arg(9, 1120672))
$ update_portrait('oc001_01 17', 'p1', [r(-2), dark], 5)
get_char('c5531') '[convertstrid(1007720)]' (**arg(10, 1007720))
$ update_portrait('oc001_01 9', 'p1', [r(-2), r_shake, light], 6)
get_char('c13') '[convertstrid(1007721)]' (**arg(11, 1007721))
return