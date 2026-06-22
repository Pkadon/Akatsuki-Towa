label avg1084:

$ play_music("ed7202.ogg")
scene avg_bg_079
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
play sfxvoice "avg_vocal_na18.ogg"
get_char('c13') '[convertstrid(2101840)]' (**arg(1, 2101840))
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 7', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(2101841)]' (**arg(2, 2101841))
$ update_portrait('oc004_01 7', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc001_01 5', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2101842)]' (**arg(3, 2101842))
$ update_portrait('oc001_01 5', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 23', 'p4', [l(-5), l_shake, light, flip], 6)
get_char('c41') '[convertstrid(2101843)]' (**arg(4, 2101843))
$ update_portrait('oc004_01 23', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2101844)]' (**arg(5, 2101844))
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 19', 'p4', [l(-5), light, flip], 6)
play sfxvoice "avg_vocal_li26.ogg"
get_char('c41') '[convertstrid(2101845)]' (**arg(6, 2101845))
$ update_portrait('oc004_01 19', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na22.ogg"
get_char('c13') '[convertstrid(2101846)]' (**arg(7, 2101846))
$ update_portrait('oc001_01 7', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 15', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(2101847)]' (**arg(8, 2101847))
$ update_portrait('oc004_01 15', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2101848)]' (**arg(9, 2101848))
$ update_portrait('oc001_01 7', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 16', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(2101849)]' (**arg(10, 2101849)) with shake
hide p4
hide p1
get_char('c0') '[convertstrid(2101850)]' (**arg(11, 2101850))
$ update_portrait('oc004_01 24', 'p4', [l(-5), light, flip], 6)
play sfxvoice "avg_vocal_li07.ogg"
get_char('c41') '[convertstrid(2101851)]' (**arg(12, 2101851))
$ update_portrait('oc004_01 24', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2101852)]' (**arg(13, 2101852))
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2101853)]' (**arg(14, 2101853))
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2101854)]' (**arg(15, 2101854))
$ update_portrait('oc001_01 22', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2101855)]' (**arg(16, 2101855))
return