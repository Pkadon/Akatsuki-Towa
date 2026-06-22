label avg20046:

$ play_music("ED6505.ogg")
scene avg_bg_027
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
$ update_narrator('c21')
window show
with fade_in
play sfx2 "other_7064.ogg"
play sfxvoice "avg_vocal_ch12.ogg"
get_char('c21') '[convertstrid(1002724)]' (**arg(1, 1002724))
$ update_portrait('oc002_01 1', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1002725)]' (**arg(2, 1002725))
$ update_portrait('oc002_01 1', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1002726)]' (**arg(3, 1002726))
hide p2
hide p1
$ update_narrator('c5943')
with fade
get_char('c5943') '[convertstrid(1002727)]' (**arg(4, 1002727))
get_char('c5943') '[convertstrid(1002728)]' (**arg(5, 1002728))
$ update_portrait('st017_01 2', 'p216', [l(-18), light, flip], 6)
get_char('c2161') '[convertstrid(1002729)]' (**arg(6, 1002729))
$ update_portrait('st017_01 2', 'p216', [l(-18), dark, flip], 5)
$ update_portrait('st018_01 4', 'p217', [r(-16), light], 6)
get_char('c2173') '[convertstrid(1002730)]' (**arg(7, 1002730))
hide p216
$ update_portrait('st018_01 4', 'p217', [r(-16), dark], 5)
$ update_portrait('st016_01 2', 'p215', [l(-8), light, flip], 6)
get_char('c2151') '[convertstrid(1002731)]' (**arg(8, 1002731))
$ update_portrait('st016_01 1', 'p215', [l(-8), light, flip], 6)
get_char('c2151') '[convertstrid(1002732)]' (**arg(9, 1002732))
hide p217
$ update_portrait('st016_01 1', 'p215', [l(-8), dark, flip], 5)
get_char('c5943') '[convertstrid(1002733)]' (**arg(10, 1002733))
get_char('c5943') '[convertstrid(1002734)]' (**arg(11, 1002734))
hide p215
$ update_portrait('st017_01 1', 'p216', [l(-18), light, flip], 6)
get_char('c2161') '[convertstrid(1002735)]' (**arg(12, 1002735))
hide p216
$ update_portrait('st016_01 5', 'p215', [l(-8), light, flip], 6)
get_char('c2151') '[convertstrid(1002736)]' (**arg(13, 1002736))
$ update_portrait('st016_01 2', 'p215', [l(-8), light, flip], 6)
get_char('c2151') '[convertstrid(1002737)]' (**arg(14, 1002737))
hide p215
$ update_portrait('st014_01 2', 'p213', [l(-18), light, flip], 6)
get_char('c2131') '[convertstrid(1002738)]' (**arg(15, 1002738))
$ update_portrait('st014_01 2', 'p213', [l(-18), dark, flip], 5)
get_char('c5943') '[convertstrid(1002739)]' (**arg(16, 1002739))
hide p213
$ update_portrait('st016_01 2', 'p215', [l(-8), light, flip], 6)
get_char('c2151') '[convertstrid(1002740)]' (**arg(17, 1002740))
$ update_portrait('st016_01 2', 'p215', [l(-8), dark, flip], 5)
get_char('c5943') '[convertstrid(1002741)]' (**arg(18, 1002741))
$ update_portrait('st016_01 1', 'p215', [l(-8), light, flip], 6)
get_char('c2151') '[convertstrid(1002742)]' (**arg(19, 1002742))
$ update_portrait('st016_01 1', 'p215', [l(-8), dark, flip], 5)
get_char('c5943') '[convertstrid(1002743)]' (**arg(20, 1002743))
get_char('c5943') '[convertstrid(1002744)]' (**arg(21, 1002744))
hide p215
$ update_portrait('oc002_01 13', 'p2', [l(-3), light, flip], 6)
$ update_narrator('c21')
with fade
play sfxvoice "avg_vocal_ch08.ogg"
get_char('c21') '[convertstrid(1002745)]' (**arg(22, 1002745))
return