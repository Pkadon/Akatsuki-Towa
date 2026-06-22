label avg12189:

$ play_music("ed6570.ogg")
scene placeholderbackground
$ update_portrait('sc027_01 4', 'p35', [l(-10), light, flip], 6)
$ update_narrator('c351')
window show
with fade_in
play sfx2 "other_7088.ogg"
get_char('c351') '[convertstrid(1120718)]' (**arg(1, 1120718))
$ update_portrait('sc027_01 3', 'p35', [l(-10), l_shake, light, flip], 6)
get_char('c351') '[convertstrid(1120719)]' (**arg(2, 1120719))
$ update_portrait('sc027_01 3', 'p35', [l(-10), dark, flip], 5)
$ update_portrait('oc001_01 2', 'p1', [r_entrance(-2), light], 6)
get_char('c13') '[convertstrid(1120720)]' (**arg(3, 1120720))
hide p35
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 8', 'p2', [l(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch04_b.ogg"
get_char('c21') '[convertstrid(1120721)]' (**arg(4, 1120721))
hide p2
$ update_portrait('oc003_01 8', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1120722)]' (**arg(5, 1120722))
hide p1
$ update_portrait('oc003_01 8', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc004_01 8', 'p4', [r(-5), r_shake, light], 6)
get_char('c43') '[convertstrid(1120723)]' (**arg(6, 1120723))
hide p3
$ update_portrait('oc004_01 8', 'p4', [r(-5), dark], 5)
$ update_portrait('sc027_01 2', 'p35', [l(-10), light, flip], 6)
get_char('c351') '[convertstrid(1120724)]' (**arg(7, 1120724))
hide p4
$ update_portrait('sc027_01 2', 'p35', [l(-10), dark, flip], 5)
$ update_portrait('oc001_01 20', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1120725)]' (**arg(8, 1120725))
$ update_portrait('oc001_01 20', 'p1', [r(-2), dark], 5)
$ update_portrait('sc027_01 3', 'p35', [l(-10), l_shake, light, flip], 6)
get_char('c351') '[convertstrid(1120726)]' (**arg(9, 1120726))
$ update_portrait('sc027_01 3', 'p35', [l(-10), dark, flip], 5)
$ update_portrait('oc001_01 7', 'p1', [r(-2), r_shake, light], 6)
play sfxvoice "avg_vocal_na22.ogg"
get_char('c13') '[convertstrid(1120727)]' (**arg(10, 1120727))
$ update_portrait('oc001_01 7', 'p1', [r(-2), dark], 5)
$ update_portrait('sc027_01 3', 'p35', [l(-10), light, flip], 6)
get_char('c351') '[convertstrid(1120728)]' (**arg(11, 1120728))
hide p1
$ update_portrait('sc027_01 3', 'p35', [l(-10), dark, flip], 5)
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1120729)]' (**arg(12, 1120729))
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
$ update_portrait('sc027_01 3', 'p35', [l_midback(-10), light, flip], 6)
get_char('c351') '[convertstrid(1120730)]' (**arg(13, 1120730))
stop music
hide p35
hide p2
$ update_narrator('c20161')
with fade
play sfx2 "other_7080.ogg"
get_char('c20161') '[convertstrid(1120731)]' (**arg(14, 1120731)) with shake
$ play_music("ed7511.ogg")
$ update_portrait('oc001_01 3', 'p1', [r(-2), r_shake, light], 6)
get_char('c13') '[convertstrid(1120732)]' (**arg(15, 1120732))
$ update_portrait('oc001_01 3', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 4', 'p2', [l(-3), light, flip], 6)
play sfx2 "fight_6024.ogg"
get_char('c21') '[convertstrid(1120733)]' (**arg(16, 1120733))
return