label avg12827(trans=fade_in):

$ play_music("ed7102.ogg")
scene avg_bg_036
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
window show
with trans
get_char('c13') '[convertstrid(1184622)]' (**arg(1, 1184622))
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1184623)]' (**arg(2, 1184623))
hide p1
play sfx2 "other_7088.ogg"
get_char('c0') '[convertstrid(1184624)]' (**arg(3, 1184624))
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1184625)]' (**arg(4, 1184625))
$ update_portrait('oc003_01 4', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('st061_01 1', 'p1304', [r(-2), light], 6)
get_char('c13043') '[convertstrid(1184626)]' (**arg(5, 1184626))
hide p1304
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1184627)]' (**arg(6, 1184627))
hide p3
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 4', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1184628)]' (**arg(7, 1184628))
hide p4
hide p1
$ update_narrator('c0')
with fade
get_char('c0') '[convertstrid(1184629)]' (**arg(8, 1184629))
get_char('c25641') '[convertstrid(1184630)]' (**arg(9, 1184630))
get_char('c25651') '[convertstrid(1184631)]' (**arg(10, 1184631))
$ update_portrait('st061_01 5', 'p1304', [r(-2), light], 6)
get_char('c13043') '[convertstrid(1184632)]' (**arg(11, 1184632))
hide p1304
$ update_portrait('oc004_01 1', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1184633)]' (**arg(12, 1184633))
$ update_portrait('oc004_01 1', 'p4', [r(-5), dark], 5)
get_char('c25641') '[convertstrid(1184634)]' (**arg(13, 1184634))
get_char('c25651') '[convertstrid(1184635)]' (**arg(14, 1184635))
hide p4
$ update_portrait('oc002_01 14', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1184636)]' (**arg(15, 1184636))
$ update_portrait('oc002_01 14', 'p2', [r(-3), dark], 5)
get_char('c25661') '[convertstrid(1184637)]' (**arg(16, 1184637))
$ update_portrait('oc002_01 15', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1184638)]' (**arg(17, 1184638))
hide p2
$ update_portrait('oc004_01 2', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1184639)]' (**arg(18, 1184639))
$ update_portrait('oc004_01 2', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1184640)]' (**arg(19, 1184640))
$ update_portrait('oc004_01 2', 'p4', [r(-5), dark], 5)
get_char('c25641') '[convertstrid(1184641)]' (**arg(20, 1184641))
get_char('c25651') '[convertstrid(1184642)]' (**arg(21, 1184642))
hide p4
$ update_portrait('oc001_01 22', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1184643)]' (**arg(22, 1184643))
$ update_portrait('oc001_01 22', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 17', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1184644)]' (**arg(23, 1184644))
hide p1
$ update_portrait('oc003_01 17', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc002_01 15', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1184645)]' (**arg(24, 1184645))
hide p3
$ update_portrait('oc002_01 15', 'p2', [r(-3), dark], 5)
get_char('c25661') '[convertstrid(1184646)]' (**arg(25, 1184646))
get_char('c25661') '[convertstrid(1184647)]' (**arg(26, 1184647))
get_char('c25661') '[convertstrid(1184648)]' (**arg(27, 1184648))
$ update_portrait('oc002_01 12', 'p2', [r(-3), r_shake, light], 6)
get_char('c23') '[convertstrid(1184649)]' (**arg(28, 1184649))
$ update_portrait('oc002_01 12', 'p2', [r(-3), dark], 5)
$ update_portrait('oc003_01 8', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1184650)]' (**arg(29, 1184650))
hide p3
$ update_portrait('st061_01 1', 'p1304', [l(-2), light, flip], 6)
get_char('c13041') '[convertstrid(1184651)]' (**arg(30, 1184651))
hide p2
$ update_portrait('st061_01 1', 'p1304', [l(-2), dark, flip], 5)
$ update_portrait('oc001_01 22', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1184652)]' (**arg(31, 1184652))
hide p1304
$ update_portrait('oc001_01 22', 'p1', [r(-2), dark], 5)
get_char('c25641') '[convertstrid(1184653)]' (**arg(32, 1184653))
return "avg12827"