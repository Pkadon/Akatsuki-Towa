label avg12797:

$ play_music("ed6323.ogg")
scene avg_bg_213
$ update_portrait('oc004_01 8', 'p4', [l(-5), light, flip], 6)
$ update_narrator('c41')
window show
with fade_in
get_char('c41') '[convertstrid(1177681)]' (**arg(1, 1177681))
$ update_portrait('oc004_01 8', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1177682)]' (**arg(2, 1177682))
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1177683)]' (**arg(3, 1177683))
hide p4
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1177684)]' (**arg(4, 1177684))
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1177685)]' (**arg(5, 1177685))
$ update_portrait('oc003_01 1', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1177686)]' (**arg(6, 1177686))
hide p1
$ update_portrait('oc003_01 1', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('st064_01 3', 'p1469', [r(-2), light], 6)
get_char('c14693') '[convertstrid(1177687)]' (**arg(7, 1177687))
return