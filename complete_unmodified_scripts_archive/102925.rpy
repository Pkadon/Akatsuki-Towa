label avg102925(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
window show
with trans
get_char('c13') '[convertstrid(1219964)]' (**arg(1, 1219964))
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
$ update_portrait('sc021_01 4', 'p29', [l(-17), light, flip], 6)
get_char('c291') '[convertstrid(1219965)]' (**arg(2, 1219965))
$ update_portrait('sc021_01 3', 'p29', [l(-17), light, flip], 6)
get_char('c291') '[convertstrid(1219966)]' (**arg(3, 1219966))
menu:
    extend ""
    '[convertstrid(1219967)]':
        call avg102926
    '[convertstrid(1219968)]':
        call avg102927
    '[convertstrid(1219969)]':
        call avg102928
return _return