label avg12568:

$ play_music("ED6105.ogg")
scene avg_bg_077
$ update_narrator('c13')
window show
with fade_in
$ update_portrait('oc001_01 1', 'p1', [r_entrance(-2), light], 6)
play sfx2 "other_7047.ogg"
get_char('c13') '[convertstrid(1155102)]' (**arg(1, 1155102))
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
get_char('c12581') '[convertstrid(1155103)]' (**arg(2, 1155103))
get_char('c12581') '[convertstrid(1155104)]' (**arg(3, 1155104))
hide p1
$ update_portrait('oc002_01 6', 'p2', [r(-3), r_shake, light], 6)
get_char('c23') '[convertstrid(1155105)]' (**arg(4, 1155105))
$ update_portrait('oc002_01 6', 'p2', [r(-3), dark], 5)
get_char('c12581') '[convertstrid(1155106)]' (**arg(5, 1155106))
hide p2
$ update_portrait('oc004_01 1', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1155107)]' (**arg(6, 1155107))
$ update_portrait('oc004_01 1', 'p4', [r(-5), dark], 5)
get_char('c12581') '[convertstrid(1155108)]' (**arg(7, 1155108))
hide p4
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na22.ogg"
get_char('c13') '[convertstrid(1155109)]' (**arg(8, 1155109))
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
get_char('c12581') '[convertstrid(1155110)]' (**arg(9, 1155110))
hide p1
$ update_portrait('oc002_01 10', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1155111)]' (**arg(10, 1155111))
$ update_portrait('oc002_01 10', 'p2', [r(-3), dark], 5)
$ update_portrait('oc004_01 1', 'p4', [l_entrance(-5), light, flip], 6)
get_char('c41') '[convertstrid(1155112)]' (**arg(11, 1155112))
hide p4
$ update_portrait('oc003_01 2', 'p3', [l(-6), light, flip], 6)
play sfxvoice "avg_vocal_ro11.ogg"
get_char('c31') '[convertstrid(1155113)]' (**arg(12, 1155113))
hide p3
get_char('c12581') '[convertstrid(1155114)]' (**arg(13, 1155114)) with shake
get_char('c12581') '[convertstrid(1155115)]' (**arg(14, 1155115))
hide p2
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1155116)]' (**arg(15, 1155116))
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 5', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1155117)]' (**arg(16, 1155117))
$ update_portrait('oc003_01 17', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1155118)]' (**arg(17, 1155118))
hide p1
$ update_portrait('oc003_01 17', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc002_01 18', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1155119)]' (**arg(18, 1155119))
hide p3
$ update_portrait('oc002_01 18', 'p2', [r(-3), dark], 5)
$ update_portrait('oc004_01 17', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1155120)]' (**arg(19, 1155120))
$ update_portrait('oc004_01 5', 'p4', [l(-5), light, flip], 6)
play sfxvoice "avg_vocal_li30.ogg"
get_char('c41') '[convertstrid(1155121)]' (**arg(20, 1155121))
hide p4
get_char('c12581') '[convertstrid(1155122)]' (**arg(21, 1155122))
get_char('c12581') '[convertstrid(1155123)]' (**arg(22, 1155123))
hide p2
$ update_portrait('oc004_01 1', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1155124)]' (**arg(23, 1155124))
$ update_portrait('oc004_01 1', 'p4', [r(-5), dark], 5)
get_char('c12581') '[convertstrid(1155125)]' (**arg(24, 1155125))
$ update_portrait('oc004_01 1', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1155126)]' (**arg(25, 1155126))
hide p4
$ update_portrait('oc002_01 14', 'p2', [r(-3), r_shake, light], 6)
get_char('c23') '[convertstrid(1155127)]' (**arg(26, 1155127))
$ update_portrait('oc002_01 14', 'p2', [r(-3), dark], 5)
get_char('c12581') '[convertstrid(1155128)]' (**arg(27, 1155128))
hide p2
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1155129)]' (**arg(28, 1155129))
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
get_char('c12581') '[convertstrid(1155130)]' (**arg(29, 1155130))
get_char('c12581') '[convertstrid(1155131)]' (**arg(30, 1155131))
get_char('c12581') '[convertstrid(1155132)]' (**arg(31, 1155132))
hide p1
$ update_portrait('oc002_01 14', 'p2', [r(-3), r_shake, light], 6)
play sfxvoice "avg_vocal_ch06.ogg"
get_char('c23') '[convertstrid(1155133)]' (**arg(32, 1155133))
$ update_portrait('oc002_01 14', 'p2', [r(-3), dark], 5)
$ update_portrait('oc004_01 9', 'p4', [l(-5), light, flip], 6)
play sfxvoice "avg_vocal_li23.ogg"
get_char('c41') '[convertstrid(1155134)]' (**arg(33, 1155134))
hide p4
$ update_portrait('oc003_01 8', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1155135)]' (**arg(34, 1155135))
hide p2
$ update_portrait('oc003_01 8', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1155136)]' (**arg(35, 1155136))
hide p3
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 5', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1155137)]' (**arg(36, 1155137))
hide p4
get_char('c12581') '[convertstrid(1155138)]' (**arg(37, 1155138))
return