label avg12763(trans=fade_in):

$ play_music("ED6202.ogg")
scene avg_bg_201
$ update_narrator('c14521')
window show
with trans
get_char('c14521') '[convertstrid(1174614)]' (**arg(1, 1174614))
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1174615)]' (**arg(2, 1174615))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
get_char('c14521') '[convertstrid(1174616)]' (**arg(3, 1174616))
get_char('c14631') '[convertstrid(1174617)]' (**arg(4, 1174617))
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1174618)]' (**arg(5, 1174618))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1174619)]' (**arg(6, 1174619))
hide p3
hide p1
$ update_narrator('c0')
with fade
get_char('c0') '[convertstrid(1174620)]' (**arg(7, 1174620))
get_char('c13051') '[convertstrid(1174621)]' (**arg(8, 1174621))
$ update_portrait('st061_01 5', 'p1304', [r(-2), light], 6)
get_char('c13043') '[convertstrid(1174622)]' (**arg(9, 1174622))
$ update_portrait('st061_01 5', 'p1304', [r(-2), dark], 5)
get_char('c13051') '[convertstrid(1174623)]' (**arg(10, 1174623))
get_char('c13051') '[convertstrid(1174624)]' (**arg(11, 1174624))
hide p1304
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1174625)]' (**arg(12, 1174625))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('st061_01 4', 'p1304', [l(-2), light, flip], 6)
get_char('c13041') '[convertstrid(1174626)]' (**arg(13, 1174626))
hide p1304
get_char('c13051') '[convertstrid(1174627)]' (**arg(14, 1174627))
get_char('c13051') '[convertstrid(1174628)]' (**arg(15, 1174628))
get_char('c13051') '[convertstrid(1174629)]' (**arg(16, 1174629))
get_char('c13051') '[convertstrid(1174630)]' (**arg(17, 1174630))
get_char('c13051') '[convertstrid(1174631)]' (**arg(18, 1174631))
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1174632)]' (**arg(19, 1174632))
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
get_char('c13051') '[convertstrid(1174633)]' (**arg(20, 1174633))
$ update_portrait('st061_01 1', 'p1304', [l(-2), light, flip], 6)
get_char('c13041') '[convertstrid(1174634)]' (**arg(21, 1174634))
return "avg12763"