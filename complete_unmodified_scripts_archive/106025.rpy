label avg106025(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('sc053_01 1', 'p60', [l(-32), light, flip], 6)
$ update_narrator('c601')
window show
with trans
get_char('c601') '[convertstrid(1219120)]' (**arg(1, 1219120))
$ update_portrait('sc053_01 5', 'p60', [l(-32), light, flip], 6)
get_char('c601') '[convertstrid(1219121)]' (**arg(2, 1219121))
$ update_portrait('sc053_01 5', 'p60', [l(-32), dark, flip], 5)
$ update_portrait('oc001_01 22', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1219122)]' (**arg(3, 1219122))
$ update_portrait('oc001_01 22', 'p1', [r(-2), dark], 5)
$ update_portrait('sc053_01 2', 'p60', [l(-32), light, flip], 6)
get_char('c601') '[convertstrid(1219123)]' (**arg(4, 1219123))
menu:
    extend ""
    '[convertstrid(1219124)]':
        call avg106026
    '[convertstrid(1219125)]':
        call avg106027
    '[convertstrid(1219126)]':
        call avg106028
return _return