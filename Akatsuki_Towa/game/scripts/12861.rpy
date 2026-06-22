label avg12861:

$ play_music("ed6323.ogg")
scene avg_bg_219
$ update_portrait('oc003_01 20', 'p3', [l(-6), light, flip], 6)
$ update_narrator('c31')
window show
with fade_in
get_char('c31') '[convertstrid(1188961)]' (**arg(1, 1188961))
hide p3
get_char('c0') '[convertstrid(1188962)]' (**arg(2, 1188962))
$ update_portrait('oc001_01 19', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1188963)]' (**arg(3, 1188963))
$ update_portrait('oc001_01 19', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 15', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1188964)]' (**arg(4, 1188964))
hide p2
hide p1
get_char('c0') '[convertstrid(1188965)]' (**arg(5, 1188965))
$ update_portrait('oc002_01 10', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1188966)]' (**arg(6, 1188966))
$ update_portrait('oc002_01 10', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc003_01 8', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1188967)]' (**arg(7, 1188967))
scene avg_bg_070
$ update_narrator('c0')
with fade
get_char('c0') '[convertstrid(1188968)]' (**arg(8, 1188968))
get_char('c0') '[convertstrid(1188969)]' (**arg(9, 1188969))
get_char('c0') '[convertstrid(1188970)]' (**arg(10, 1188970))
return