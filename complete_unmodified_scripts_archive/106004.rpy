label avg106004(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('sc053_01 2', 'p60', [l(-32), light, flip], 6)
$ update_narrator('c601')
window show
with trans
get_char('c601') '[convertstrid(1219056)]' (**arg(1, 1219056))
$ update_portrait('sc053_01 2', 'p60', [l(-32), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1219057)]' (**arg(2, 1219057))
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('sc053_01 1', 'p60', [l(-32), light, flip], 6)
get_char('c601') '[convertstrid(1219058)]' (**arg(3, 1219058))
$ update_portrait('sc053_01 4', 'p60', [l(-32), light, flip], 6)
get_char('c601') '[convertstrid(1219059)]' (**arg(4, 1219059))
menu:
    extend ""
    '[convertstrid(1219060)]':
        call avg106005
    '[convertstrid(1219061)]':
        call avg106006
    '[convertstrid(1219062)]':
        call avg106007
return _return