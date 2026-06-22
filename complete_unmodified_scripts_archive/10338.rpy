label avg10338:

$ play_music("ed7105.ogg")
scene avg_bg_003
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
get_char('c13') '[convertstrid(1131032)]' (**arg(1, 1131032))
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1131033)]' (**arg(2, 1131033))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 4', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1131034)]' (**arg(3, 1131034))
$ update_portrait('oc002_01 4', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1131011)]' (**arg(4, 1131011))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 9', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1131012)]' (**arg(5, 1131012))
$ update_portrait('oc002_01 9', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 12', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1131013)]' (**arg(6, 1131013))
hide p2
$ update_portrait('oc001_01 12', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 5', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1131014)]' (**arg(7, 1131014))
hide p3
$ update_portrait('oc005_01 12', 'p5', [l(-6), light, flip], 6)
get_char('c51') '[convertstrid(1131015)]' (**arg(8, 1131015))
$ update_portrait('oc005_01 12', 'p5', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1131016)]' (**arg(9, 1131016))
hide p5
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 5', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1131017)]' (**arg(10, 1131017))
$ update_portrait('oc004_01 5', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc001_01 9', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1131018)]' (**arg(11, 1131018))
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1131019)]' (**arg(12, 1131019))
hide p4
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('oc005_01 9', 'p5', [l(-6), light, flip], 6)
get_char('c51') '[convertstrid(1131020)]' (**arg(13, 1131020))
$ update_portrait('oc005_01 9', 'p5', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 12', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1131021)]' (**arg(14, 1131021))
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1131022)]' (**arg(15, 1131022))
hide p5
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 9', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1131023)]' (**arg(16, 1131023))
return