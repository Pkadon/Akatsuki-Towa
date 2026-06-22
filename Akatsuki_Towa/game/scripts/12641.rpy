label avg12641:

$ play_music("ed7100.ogg")
scene avg_bg_023
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
get_char('c13') '[convertstrid(1163012)]' (**arg(1, 1163012))
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 2', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1163013)]' (**arg(2, 1163013))
$ update_portrait('oc003_01 2', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1163014)]' (**arg(3, 1163014))
hide p3
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 14', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1163015)]' (**arg(4, 1163015))
hide p2
$ update_portrait('oc004_01 1', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1163016)]' (**arg(5, 1163016))
$ update_portrait('oc004_01 1', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc001_01 22', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1163017)]' (**arg(6, 1163017))
scene avg_bg_070
$ update_narrator('c0')
with fade
play sfx2 "other_7018.ogg"
get_char('c0') '[convertstrid(1163018)]' (**arg(7, 1163018))
get_char('c0') '[convertstrid(1163019)]' (**arg(8, 1163019))
return