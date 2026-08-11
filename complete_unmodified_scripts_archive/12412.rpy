label avg12412(trans=fade_in):

$ play_music("ed7514.ogg")
scene avg_bg_050
$ update_narrator('c23')
window show
with trans
$ update_portrait('oc002_01 1', 'p2', [r_entrance(-3), light], 6)
get_char('c23') '[convertstrid(1142631)]' (**arg(1, 1142631))
$ update_portrait('oc002_01 13', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1142632)]' (**arg(2, 1142632))
$ update_portrait('oc002_01 13', 'p2', [r(-3), dark], 5)
$ update_portrait('oc003_01 1', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1142633)]' (**arg(3, 1142633))
hide p3
$ update_portrait('uc003_04 1', 'p1045', [l(-14), light, flip], 6)
get_char('c10451') '[convertstrid(1142634)]' (**arg(4, 1142634))
hide p1045
$ update_portrait('uc003_04 1', 'p1046', [l(-14), light, flip], 6)
get_char('c10461') '[convertstrid(1142635)]' (**arg(5, 1142635))
hide p1046
hide p2
$ update_narrator('c0')
with fade
get_char('c0') '[convertstrid(1142636)]' (**arg(6, 1142636))
$ update_portrait('oc003_01 1', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1142637)]' (**arg(7, 1142637))
$ update_portrait('oc003_01 1', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc004_01 1', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1142638)]' (**arg(8, 1142638))
$ update_portrait('oc004_01 1', 'p4', [r(-5), dark], 5)
$ update_portrait('oc003_01 2', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1142639)]' (**arg(9, 1142639))
hide p4
$ update_portrait('oc003_01 2', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1142640)]' (**arg(10, 1142640))
hide p2
$ update_portrait('oc001_01 18', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1142641)]' (**arg(11, 1142641))
$ update_portrait('oc001_01 16', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1142642)]' (**arg(12, 1142642))
hide p3
$ update_portrait('oc001_01 16', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 1', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1142643)]' (**arg(13, 1142643))
hide p2
$ update_portrait('oc004_01 1', 'p4', [l(-5), light, flip], 6)
play sfxvoice "avg_vocal_li03.ogg"
get_char('c41') '[convertstrid(1142644)]' (**arg(14, 1142644))
$ update_portrait('oc004_01 1', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc001_01 18', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1142645)]' (**arg(15, 1142645))
$ update_portrait('oc001_01 18', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1142646)]' (**arg(16, 1142646))
$ update_portrait('oc001_01 16', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1142647)]' (**arg(17, 1142647))
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na20.ogg"
get_char('c13') '[convertstrid(1142648)]' (**arg(18, 1142648))
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 1', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1142649)]' (**arg(19, 1142649))
hide p4
hide p1
$ update_portrait('oc004_01 18', 'p4', [l(-5), light, flip], 6)
$ update_narrator('c41')
with fade
get_char('c41') '[convertstrid(1142650)]' (**arg(20, 1142650))
$ update_portrait('oc004_01 18', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1142651)]' (**arg(21, 1142651))
$ update_portrait('oc004_01 21', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1142652)]' (**arg(22, 1142652))
$ update_portrait('oc004_01 20', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1142653)]' (**arg(23, 1142653))
return "avg12412"