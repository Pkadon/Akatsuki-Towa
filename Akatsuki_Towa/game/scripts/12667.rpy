label avg12667:

$ play_music("ed7150.ogg")
scene avg_bg_015
$ update_narrator('c0')
window show
with fade_in
get_char('c0') '[convertstrid(1166645)]' (**arg(1, 1166645))
$ update_portrait('oc002_01 23', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1166646)]' (**arg(2, 1166646))
$ update_portrait('oc002_01 23', 'p2', [r(-3), dark], 5)
$ update_portrait('oc004_01 17', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1166647)]' (**arg(3, 1166647))
$ update_portrait('oc004_01 1', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1166648)]' (**arg(4, 1166648))
hide p2
$ update_portrait('oc004_01 1', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
play sfx2 "fight_6021.ogg"
get_char('c13') '[convertstrid(1166649)]' (**arg(5, 1166649))
$ play_music("ed7511.ogg")
$ update_portrait('oc001_01 9', 'p1', [r_midback(-2), light], 6)
play sfx2 "other_7087.ogg"
get_char('c13') '[convertstrid(1166650)]' (**arg(6, 1166650, size=(1.2)))
hide p4
$ update_portrait('oc001_01 9', 'p1', [r(-2), dark], 5)
play sfx2 "other_7007.ogg"
get_char('c13671') '[convertstrid(1166651)]' (**arg(7, 1166651)) with shake
hide p1
play sfx2 "fight_6022.ogg"
get_char('c0') '[convertstrid(1166652)]' (**arg(8, 1166652))
$ update_portrait('oc001_01 20', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1166653)]' (**arg(9, 1166653))
$ update_portrait('oc001_01 20', 'p1', [r(-2), dark], 5)
get_char('c13671') '[convertstrid(1166654)]' (**arg(10, 1166654))
hide p1
get_char('c0') '[convertstrid(1166655)]' (**arg(11, 1166655))
$ update_portrait('oc004_01 4', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1166656)]' (**arg(12, 1166656))
$ update_portrait('oc004_01 4', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
play sfx2 "fight_6024.ogg"
get_char('c13') '[convertstrid(1166657)]' (**arg(13, 1166657))
hide p4
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
get_char('c13661') '[convertstrid(1166658)]' (**arg(14, 1166658))
hide p1
$ update_portrait('oc002_01 9', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1166659)]' (**arg(15, 1166659))
return