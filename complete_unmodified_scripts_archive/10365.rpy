label avg10365(trans=fade_in):

$ play_music("ed7102.ogg")
scene avg_bg_049
$ update_narrator('c10401')
window show
with trans
get_char('c10401') '[convertstrid(1131999)]' (**arg(1, 1131999))
get_char('c10413') '[convertstrid(1132000)]' (**arg(2, 1132000))
get_char('c10401') '[convertstrid(1132001)]' (**arg(3, 1132001))
get_char('c10413') '[convertstrid(1132002)]' (**arg(4, 1132002))
get_char('c10401') '[convertstrid(1132003)]' (**arg(5, 1132003))
get_char('c10413') '[convertstrid(1132004)]' (**arg(6, 1132004))
get_char('c10401') '[convertstrid(1132005)]' (**arg(7, 1132005))
get_char('c10401') '[convertstrid(1132006)]' (**arg(8, 1132006))
get_char('c10413') '[convertstrid(1132007)]' (**arg(9, 1132007))
get_char('c10401') '[convertstrid(1132008)]' (**arg(10, 1132008))
get_char('c10413') '[convertstrid(1132009)]' (**arg(11, 1132009))
get_char('c10401') '[convertstrid(1132010)]' (**arg(12, 1132010))
get_char('c10413') '[convertstrid(1132011)]' (**arg(13, 1132011))
$ update_portrait('oc001_01 4', 'p1', [r_entrance(-2), light], 6)
get_char('c13') '[convertstrid(1132012)]' (**arg(14, 1132012))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 8', 'p4', [l(-5), light, flip], 6)
play sfxvoice "avg_vocal_li18.ogg"
get_char('c41') '[convertstrid(1132013)]' (**arg(15, 1132013))
$ update_portrait('oc004_01 17', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1132014)]' (**arg(16, 1132014))
hide p4
$ update_portrait('oc003_01 2', 'p3', [l_entrance(-6), light, flip], 6)
get_char('c31') '[convertstrid(1132015)]' (**arg(17, 1132015))
$ update_portrait('oc003_01 7', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1132016)]' (**arg(18, 1132016))
$ update_portrait('oc003_01 8', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1132017)]' (**arg(19, 1132017))
hide p1
$ update_portrait('oc003_01 8', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc002_01 21', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1132018)]' (**arg(20, 1132018))
hide p2
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na02.ogg"
get_char('c13') '[convertstrid(1132019)]' (**arg(21, 1132019))
hide p3
$ update_portrait('oc001_01 7', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 4', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1132020)]' (**arg(22, 1132020))
$ update_portrait('oc004_01 8', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1132021)]' (**arg(23, 1132021))
$ update_portrait('oc004_01 8', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc001_01 12', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1132022)]' (**arg(24, 1132022))
hide p4
$ update_portrait('oc001_01 12', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1132023)]' (**arg(25, 1132023))
hide p3
$ update_portrait('oc004_01 7', 'p4', [l(-5), light, flip], 6)
play sfxvoice "avg_vocal_li19.ogg"
get_char('c41') '[convertstrid(1132024)]' (**arg(26, 1132024))
hide p1
$ update_portrait('oc004_01 7', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1132025)]' (**arg(27, 1132025))
$ update_portrait('oc002_01 8', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1132026)]' (**arg(28, 1132026))
$ update_portrait('oc002_01 8', 'p2', [r(-3), dark], 5)
$ update_portrait('oc004_01 8', 'p4', [l(-5), light, flip], 6)
play sfxvoice "avg_vocal_li18.ogg"
get_char('c41') '[convertstrid(1132027)]' (**arg(29, 1132027))
$ update_portrait('oc004_01 16', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1132028)]' (**arg(30, 1132028))
hide p2
$ update_portrait('oc004_01 16', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1132029)]' (**arg(31, 1132029))
return "avg10365"