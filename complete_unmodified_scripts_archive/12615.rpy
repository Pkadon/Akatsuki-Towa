label avg12615:

$ play_music("ed7105.ogg")
scene avg_bg_010
$ update_narrator('c21')
window show
with fade_in
$ update_portrait('oc002_01 8', 'p2', [l_entrance(-3), light, flip], 6)
get_char('c21') '[convertstrid(1161595)]' (**arg(1, 1161595))
$ update_portrait('oc002_01 8', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc003_01 13', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1161596)]' (**arg(2, 1161596))
hide p2
$ update_portrait('oc003_01 13', 'p3', [r(-6), dark], 5)
$ update_portrait('oc004_01 8', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1161597)]' (**arg(3, 1161597))
hide p3
$ update_portrait('oc004_01 8', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc002_01 15', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1161598)]' (**arg(4, 1161598))
hide p2
$ update_portrait('oc001_01 2', 'p1', [r_entrance(-2), light], 6)
get_char('c13') '[convertstrid(1161599)]' (**arg(5, 1161599))
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1161600)]' (**arg(6, 1161600))
hide p4
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 1', 'p2', [l_exit(-3), light, flip], 6)
play sfx2 "other_7085.ogg"
get_char('c21') '[convertstrid(1161601)]' (**arg(7, 1161601))
hide p2
hide p1
$ update_portrait('oc003_01 13', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1161602)]' (**arg(8, 1161602))
$ update_portrait('oc003_01 13', 'p3', [r(-6), dark], 5)
$ update_portrait('oc004_01 12', 'p4', [l_entrance(-5), light, flip], 6)
get_char('c41') '[convertstrid(1161603)]' (**arg(9, 1161603))
hide p3
$ update_portrait('oc004_01 12', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc001_01 16', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1161604)]' (**arg(10, 1161604))
hide p4
$ update_portrait('oc001_01 16', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 8', 'p3', [l(-6), light, flip], 6)
play sfxvoice "avg_vocal_ro13.ogg"
get_char('c31') '[convertstrid(1161605)]' (**arg(11, 1161605))
$ update_portrait('oc003_01 8', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1161606)]' (**arg(12, 1161606))
hide p3
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 4', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1161607)]' (**arg(13, 1161607))
$ update_portrait('oc004_01 4', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1161608)]' (**arg(14, 1161608))
hide p1
$ update_portrait('oc004_01 4', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc003_01 2', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1161609)]' (**arg(15, 1161609))
$ play_music("ed7511.ogg")
hide p4
$ update_portrait('oc003_01 2', 'p3', [r(-6), dark], 5)
$ update_portrait('oc002_01 3', 'p2', [l_entrance(-3), light, flip], 6)
get_char('c21') '[convertstrid(1161610)]' (**arg(16, 1161610)) with shake
hide p3
$ update_portrait('oc002_01 3', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 12', 'p1', [r(-2), light], 6)
play sfx2 "other_7080.ogg"
get_char('c13') '[convertstrid(1161611)]' (**arg(17, 1161611))
$ update_portrait('oc001_01 12', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 12', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1161612)]' (**arg(18, 1161612))
hide p2
$ update_portrait('oc004_01 16', 'p4', [l(-5), light, flip], 6)
play sfx2 "other_7093.ogg"
get_char('c41') '[convertstrid(1161613)]' (**arg(19, 1161613))
$ update_portrait('oc004_01 16', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc001_01 20', 'p1', [r(-2), light], 6)
play sfx2 "fight_6024.ogg"
get_char('c13') '[convertstrid(1161614)]' (**arg(20, 1161614))
return