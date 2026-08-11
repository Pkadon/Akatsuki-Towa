label avg10356(trans=fade_in):

$ play_music("ed9999.ogg")
scene avg_bg_050
$ update_portrait('oc002_01 14', 'p2', [l(-3), light, flip], 6)
$ update_narrator('c21')
window show
with trans
play sfxvoice "avg_vocal_ch08.ogg"
get_char('c21') '[convertstrid(1131661)]' (**arg(1, 1131661))
$ update_portrait('oc002_01 14', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1131662)]' (**arg(2, 1131662))
hide p2
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 1', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1131663)]' (**arg(3, 1131663))
$ update_portrait('oc004_01 1', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1131664)]' (**arg(4, 1131664))
hide p4
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch12.ogg"
get_char('c21') '[convertstrid(1131665)]' (**arg(5, 1131665))
hide p2
hide p1
$ update_narrator('c10301')
with fade
get_char('c10301') '[convertstrid(1131666)]' (**arg(6, 1131666))
get_char('c10313') '[convertstrid(1131667)]' (**arg(7, 1131667))
play sfx2 "other_7007.ogg"
get_char('c10301') '[convertstrid(1131668)]' (**arg(8, 1131668, size=(1.3)))
$ update_portrait('oc001_01 12', 'p1', [r(-2), r_shake, light], 6)
play sfxvoice "avg_vocal_na21.ogg"
get_char('c13') '[convertstrid(1131669)]' (**arg(9, 1131669))
hide p1
play sfx2 "other_7012.ogg"
get_char('c0') '[convertstrid(1131670)]' (**arg(10, 1131670)) with shake
$ update_portrait('oc002_01 21', 'p2', [r(-3), light], 6)
play sfxvoice "avg_vocal_ch20.ogg"
get_char('c23') '[convertstrid(1131671)]' (**arg(11, 1131671)) with shake
$ update_portrait('oc002_01 21', 'p2', [r(-3), dark], 5)
$ update_portrait('oc004_01 17', 'p4', [l(-5), light, flip], 6)
play sfxvoice "avg_vocal_li18.ogg"
get_char('c41') '[convertstrid(1131672)]' (**arg(12, 1131672))
$ update_portrait('oc004_01 21', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1131673)]' (**arg(13, 1131673))
$ update_portrait('oc004_01 7', 'p4', [l(-5), light, flip], 6)
play sfxvoice "avg_vocal_li19.ogg"
get_char('c41') '[convertstrid(1131675)]' (**arg(14, 1131675))
hide p4
$ update_portrait('oc003_01 4', 'p3', [l_entrance(-6), light, flip], 6)
get_char('c31') '[convertstrid(1131676)]' (**arg(15, 1131676))
$ update_portrait('oc003_01 7', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1131677)]' (**arg(16, 1131677))
$ update_portrait('oc003_01 17', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1131678)]' (**arg(17, 1131678))
hide p2
$ update_portrait('oc003_01 17', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1131679)]' (**arg(18, 1131679))
hide p3
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 5', 'p2', [l_midback(-3), light, flip], 6)
get_char('c21') '[convertstrid(1131680)]' (**arg(19, 1131680))
$ update_portrait('oc002_01 5', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na02.ogg"
get_char('c13') '[convertstrid(1131681)]' (**arg(20, 1131681))
$ update_portrait('oc001_01 7', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 17', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1131682)]' (**arg(21, 1131682))
$ update_portrait('oc002_01 17', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1131683)]' (**arg(22, 1131683))
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 21', 'p2', [l(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch21.ogg"
get_char('c21') '[convertstrid(1131684)]' (**arg(23, 1131684))
return "avg10356"