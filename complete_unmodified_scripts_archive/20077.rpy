label avg20077(trans=fade_in):

$ play_music("ed7150.ogg")
scene avg_bg_006
$ update_narrator('c2031')
$ update_portrait('st003_01 2', 'p203', [l(-7), light, flip], 6)
window show
with trans
$ update_portrait('st003_01 2', 'p203', [l(-7), l_shake, light, flip], 6)
play sfx2 "other_7042.ogg"
get_char('c2031') '[convertstrid(1003987)]' (**arg(1, 1003987))
$ update_portrait('st003_01 2', 'p203', [l(-7), dark, flip], 5)
$ update_portrait('st007_01 2', 'p207', [r_entrance(-6), l_shake, light], 6)
get_char('c2073') '[convertstrid(1003988)]' (**arg(2, 1003988))
hide p203
$ update_portrait('st007_01 2', 'p207', [r(-6), dark], 5)
$ update_portrait('oc004_01 10', 'p4', [l(-5), light, flip], 6)
play sfxvoice "avg_vocal_li28.ogg"
get_char('c41') '[convertstrid(1003989)]' (**arg(3, 1003989))
$ update_portrait('oc004_01 10', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('st007_01 2', 'p207', [r(-6), light], 6)
get_char('c2073') '[convertstrid(1003990)]' (**arg(4, 1003990))
hide p4
$ update_portrait('st007_01 2', 'p207', [r(-6), dark], 5)
$ update_portrait('oc001_01 10', 'p1', [l(-2), light, flip], 6)
play sfxvoice "avg_vocal_na20.ogg"
get_char('c11') '[convertstrid(1003991)]' (**arg(5, 1003991))
hide p1
hide p207
get_char('c0') '[convertstrid(1003992)]' (**arg(6, 1003992))
$ update_portrait('st003_01 2', 'p203', [r(-7), light], 6)
play sfx2 "other_7004.ogg"
get_char('c2033') '[convertstrid(1003993)]' (**arg(7, 1003993))
$ update_portrait('st003_01 1', 'p203', [r(-7), light], 6)
get_char('c2033') '[convertstrid(1003994)]' (**arg(8, 1003994))
$ update_portrait('st003_01 1', 'p203', [r(-7), light], 6)
get_char('c2033') '[convertstrid(1003995)]' (**arg(9, 1003995))
$ update_portrait('st003_01 1', 'p203', [r(-7), light], 6)
get_char('c2033') '[convertstrid(1003996)]' (**arg(10, 1003996))
$ update_portrait('st003_01 1', 'p203', [r(-7), dark], 5)
$ update_portrait('oc002_01 18', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1003997)]' (**arg(11, 1003997))
hide p203
$ update_portrait('oc002_01 18', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1003998)]' (**arg(12, 1003998))
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1003999)]' (**arg(13, 1003999))
return "avg20077"