label avg14039:

$ play_music("ed7110.ogg")
scene avg_bg_015
$ update_portrait('oc002_01 5', 'p2', [l(-3), light, flip], 6)
$ update_narrator('c21')
window show
with fade_in
get_char('c21') '[convertstrid(1202760)]' (**arg(1, 1202760))
$ update_portrait('oc002_01 8', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1202761)]' (**arg(2, 1202761))
$ update_portrait('oc002_01 8', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1202762)]' (**arg(3, 1202762))
hide p2
$ update_portrait('oc001_01 7', 'p1', [r(-2), dark], 5)
get_char('c7521') '[convertstrid(1202763)]' (**arg(4, 1202763))
hide p1
$ update_portrait('oc002_01 21', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1202764)]' (**arg(5, 1202764))
$ update_portrait('oc002_01 21', 'p2', [r(-3), dark], 5)
get_char('c7521') '[convertstrid(1202765)]' (**arg(6, 1202765))
$ update_portrait('oc002_01 6', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1202766)]' (**arg(7, 1202766))
$ update_portrait('oc002_01 6', 'p2', [r(-3), dark], 5)
get_char('c7521') '[convertstrid(1202767)]' (**arg(8, 1202767))
get_char('c7521') '[convertstrid(1202768)]' (**arg(9, 1202768))
hide p2
get_char('c0') '[convertstrid(1202769)]' (**arg(10, 1202769))
return