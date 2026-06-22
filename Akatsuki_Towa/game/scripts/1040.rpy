label avg1040:

$ play_music("ed7201.ogg")
scene avg_bg_010
$ update_portrait('oc002_01 8', 'p2', [l(-3), light, flip], 6)
$ update_narrator('c21')
window show
with fade_in
get_char('c21') '[convertstrid(2100628)]' (**arg(1, 2100628))
$ update_portrait('oc002_01 8', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2100629)]' (**arg(2, 2100629))
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(2100630)]' (**arg(3, 2100630))
hide p2
$ update_portrait('sc046_01 1', 'p53', [l_entrance(-5), light, flip], 6)
get_char('c531') '[convertstrid(2100631)]' (**arg(4, 2100631))
$ update_portrait('sc046_01 1', 'p53', [l(-5), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2100632)]' (**arg(5, 2100632))
hide p53
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(2100633)]' (**arg(6, 2100633))
$ update_portrait('sc049_01 1', 'p56', [l(-8), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2100634)]' (**arg(7, 2100634))
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(2100635)]' (**arg(8, 2100635))
hide p56
$ update_portrait('sc046_01 1', 'p53', [l(-5), light, flip], 6)
get_char('c531') '[convertstrid(2100636)]' (**arg(9, 2100636))
hide p1
$ update_portrait('sc046_01 1', 'p53', [l(-5), dark, flip], 5)
$ update_portrait('oc002_01 12', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(2100637)]' (**arg(10, 2100637))
hide p2
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2100638)]' (**arg(11, 2100638))
hide p53
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 10', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(2100639)]' (**arg(12, 2100639))
return