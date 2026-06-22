label avg20075:

$ play_music("ed7150.ogg")
scene avg_bg_056
$ update_portrait('oc001_01 4', 'p1', [l(-2), light, flip], 6)
$ update_narrator('c11')
window show
with fade_in
get_char('c11') '[convertstrid(1003960)]' (**arg(1, 1003960))
hide p1
$ update_narrator('c6561')
with fade
play sfx2 "other_7042.ogg"
get_char('c6561') '[convertstrid(1003961)]' (**arg(2, 1003961))
get_char('c6483') '[convertstrid(1003962)]' (**arg(3, 1003962))
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1003963)]' (**arg(4, 1003963))
hide p1
$ update_portrait('oc003_01 1', 'p3', [r(-6), light], 6)
play sfxvoice "avg_vocal_ro02.ogg"
get_char('c33') '[convertstrid(1003964)]' (**arg(5, 1003964))
$ update_portrait('oc003_01 1', 'p3', [r(-6), dark], 5)
get_char('c6501') '[convertstrid(1003965)]' (**arg(6, 1003965))
get_char('c6561') '[convertstrid(1003966)]' (**arg(7, 1003966))
get_char('c6561') '[convertstrid(1003967)]' (**arg(8, 1003967))
hide p3
get_char('c6503') '[convertstrid(1003968)]' (**arg(9, 1003968))
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1003969)]' (**arg(10, 1003969))
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1003970)]' (**arg(11, 1003970))
return