label avg106021:

stop music
scene placeholderbackground
$ update_portrait('sc053_01 1', 'p60', [l(-32), light, flip], 6)
$ update_narrator('c601')
window show
with fade_in
get_char('c601') '[convertstrid(1219108)]' (**arg(1, 1219108))
$ update_portrait('sc053_01 2', 'p60', [l(-32), light, flip], 6)
get_char('c601') '[convertstrid(1219109)]' (**arg(2, 1219109))
$ update_portrait('sc053_01 2', 'p60', [l(-32), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1219110)]' (**arg(3, 1219110))
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('sc053_01 4', 'p60', [l(-32), light, flip], 6)
get_char('c601') '[convertstrid(1219111)]' (**arg(4, 1219111))
$ update_portrait('sc053_01 4', 'p60', [l(-32), light, flip], 6)
get_char('c601') '[convertstrid(1219112)]' (**arg(5, 1219112))
menu:
    extend ""
    '[convertstrid(1219113)]':
        call avg106022
    '[convertstrid(1219114)]':
        call avg106023
    '[convertstrid(1219115)]':
        call avg106024
return