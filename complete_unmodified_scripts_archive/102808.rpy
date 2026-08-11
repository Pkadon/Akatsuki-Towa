label avg102808(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
window show
with trans
get_char('c13') '[convertstrid(1219734)]' (**arg(1, 1219734))
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('sc020_01 5', 'p28', [l(-10), light, flip], 6)
get_char('c281') '[convertstrid(1219735)]' (**arg(2, 1219735))
$ update_portrait('sc020_01 5', 'p28', [l(-10), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1219736)]' (**arg(3, 1219736))
menu:
    extend ""
    '[convertstrid(1219737)]':
        call avg102809
    '[convertstrid(1219738)]':
        call avg102810
    '[convertstrid(1219739)]':
        call avg102811
return _return