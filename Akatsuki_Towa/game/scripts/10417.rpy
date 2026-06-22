label avg10417:

$ play_music("ed7516.ogg")
scene avg_bg_078
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
$ update_narrator('c21')
window show
with fade_in
play sfx2 "common_select.ogg"
get_char('c21') '[convertstrid(1140938)]' (**arg(1, 1140938))
$ update_portrait('oc002_01 10', 'p2', [l(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch10.ogg"
get_char('c21') '[convertstrid(1140939)]' (**arg(2, 1140939))
$ update_portrait('oc002_01 10', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1140940)]' (**arg(3, 1140940))
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1140945)]' (**arg(4, 1140945))
$ update_portrait('oc001_01 16', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1140946)]' (**arg(5, 1140946))
hide p2
$ update_portrait('oc001_01 16', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 7', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1140947)]' (**arg(6, 1140947))
$ update_portrait('oc003_01 7', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1140948)]' (**arg(7, 1140948))
$ update_portrait('oc003_01 1', 'p3', [l(-6), light, flip], 6)
play sfxvoice "avg_vocal_ro02.ogg"
get_char('c31') '[convertstrid(1140949)]' (**arg(8, 1140949))
$ update_portrait('oc003_01 1', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 5', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1140950)]' (**arg(9, 1140950))
$ update_portrait('oc001_01 17', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1140951)]' (**arg(10, 1140951))
hide p3
$ update_portrait('oc001_01 17', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 14', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1140952)]' (**arg(11, 1140952))
$ update_portrait('oc002_01 17', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1140953)]' (**arg(12, 1140953))
$ update_portrait('oc002_01 12', 'p2', [l(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch11.ogg"
get_char('c21') '[convertstrid(1140954)]' (**arg(13, 1140954))
hide p2
$ update_portrait('oc004_01 11', 'p4', [l(-5), light, flip], 6)
play sfxvoice "avg_vocal_li16.ogg"
get_char('c41') '[convertstrid(1140955)]' (**arg(14, 1140955))
$ update_portrait('oc004_01 11', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1140956)]' (**arg(15, 1140956))
$ update_portrait('oc001_01 5', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na19.ogg"
get_char('c13') '[convertstrid(1140957)]' (**arg(16, 1140957))
$ update_portrait('oc001_01 5', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 12', 'p4', [l(-5), l_shake, light, flip], 6)
get_char('c41') '[convertstrid(1140958)]' (**arg(17, 1140958))
hide p4
$ update_portrait('oc003_01 17', 'p3', [l(-6), light, flip], 6)
play sfxvoice "avg_vocal_ro03.ogg"
get_char('c31') '[convertstrid(1140959)]' (**arg(18, 1140959))
hide p1
$ update_portrait('oc003_01 17', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc004_01 18', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1140960)]' (**arg(19, 1140960))
$ update_portrait('oc004_01 11', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1140961)]' (**arg(20, 1140961))
hide p4
$ update_portrait('oc001_01 11', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na15.ogg"
get_char('c13') '[convertstrid(1140962)]' (**arg(21, 1140962))
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1140963)]' (**arg(22, 1140963))
hide p3
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 21', 'p4', [l(-5), l_shake, light, flip], 6)
get_char('c41') '[convertstrid(1140964)]' (**arg(23, 1140964))
hide p1
$ update_portrait('oc004_01 21', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc002_01 5', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1140965)]' (**arg(24, 1140965))
hide p4
$ update_portrait('oc002_01 5', 'p2', [r(-3), dark], 5)
$ update_portrait('st053_01 1', 'p1007', [l(-12), light, flip], 6)
get_char('c10071') '[convertstrid(1140966)]' (**arg(25, 1140966))
hide p2
$ update_portrait('st053_01 1', 'p1007', [l(-12), dark, flip], 5)
$ update_portrait('oc004_01 1', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1140967)]' (**arg(26, 1140967))
hide p1007
$ update_portrait('oc004_01 1', 'p4', [r(-5), dark], 5)
get_char('c11041') '[convertstrid(1140968)]' (**arg(27, 1140968))
hide p4
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1140969)]' (**arg(28, 1140969))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 8', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1140970)]' (**arg(29, 1140970))
return