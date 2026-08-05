label avg12223:

$ play_music("ED6105.ogg")
scene avg_bg_036
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
get_char('c13') '[convertstrid(1120997)]' (**arg(1, 1120997))
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('sc039_01 1', 'p46', [l(-13), light, flip], 6)
get_char('c461') '[convertstrid(1120998)]' (**arg(2, 1120998))
hide p46
play sfx2 "other_7077.ogg"
get_char('c50101') '[convertstrid(1120999)]' (**arg(3, 1120999))
hide p1
$ update_portrait('oc002_01 13', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1121000)]' (**arg(4, 1121000))
hide p2
play sfx2 "other_7086.ogg"
get_char('c0') '[convertstrid(1121002)]' (**arg(5, 1121002))
$ update_portrait('st026_01 5', 'p225', [l(-14), light, flip], 6)
get_char('c2251') '[convertstrid(1121003)]' (**arg(6, 1121003))
$ update_portrait('st026_01 5', 'p225', [l(-14), dark, flip], 5)
$ update_portrait('oc002_01 14', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1121004)]' (**arg(7, 1121004))
hide p225
$ update_portrait('oc002_01 14', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 2', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1121005)]' (**arg(8, 1121005))
hide p2
$ update_portrait('oc001_01 2', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('sc039_01 2', 'p46', [r(-13), light], 6)
get_char('c463') '[convertstrid(1121006)]' (**arg(9, 1121006))
$ update_portrait('sc039_01 2', 'p46', [r(-13), dark], 5)
$ update_portrait('oc001_01 12', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1121007)]' (**arg(10, 1121007))
hide p46
$ update_portrait('oc001_01 12', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc004_01 8', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1121008)]' (**arg(11, 1121008))
$ update_portrait('oc004_01 8', 'p4', [r(-5), dark], 5)
$ update_portrait('oc001_01 12', 'p1', [l(-2), l_shake, light, flip], 6)
get_char('c11') '[convertstrid(1121009)]' (**arg(12, 1121009))
hide p4
$ update_portrait('oc001_01 12', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc002_01 5', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1121487)]' (**arg(13, 1121487))
$ update_portrait('oc002_01 5', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 24', 'p1', [l(-2), l_shake, light, flip], 6)
play sfx2 "other_7007.ogg"
get_char('c11') '[convertstrid(1121010)]' (**arg(14, 1121010))
hide p2
$ update_portrait('oc001_01 24', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('sc039_01 2', 'p46', [r(-13), light], 6)
get_char('c463') '[convertstrid(1121011)]' (**arg(15, 1121011))
hide p1
$ update_portrait('sc039_01 2', 'p46', [r(-13), dark], 5)
$ update_portrait('oc002_01 7', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1121012)]' (**arg(16, 1121012))
$ update_portrait('oc002_01 7', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('sc039_01 2', 'p46', [r(-13), light], 6)
get_char('c463') '[convertstrid(1121488)]' (**arg(17, 1121488))
hide p46
$ update_portrait('st026_01 1', 'p225', [r(-14), light], 6)
get_char('c2253') '[convertstrid(1121013)]' (**arg(18, 1121013))
hide p2
$ update_portrait('st026_01 1', 'p225', [r(-14), dark], 5)
$ update_portrait('oc001_01 7', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1121014)]' (**arg(19, 1121014))
hide p225
$ update_portrait('oc001_01 7', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc002_01 5', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1121015)]' (**arg(20, 1121015))
hide p1
hide p2
get_char('c0') '[convertstrid(1121016)]' (**arg(21, 1121016))
return