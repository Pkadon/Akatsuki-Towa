label avg102104(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('sc013_01 1', 'p21', [l(-12), light, flip], 6)
$ update_narrator('c211')
window show
with trans
get_char('c211') '[convertstrid(1218820)]' (**arg(1, 1218820))
$ update_portrait('sc013_01 4', 'p21', [l(-12), light, flip], 6)
get_char('c211') '[convertstrid(1218821)]' (**arg(2, 1218821))
$ update_portrait('sc013_01 4', 'p21', [l(-12), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1218822)]' (**arg(3, 1218822))
menu:
    extend ""
    '[convertstrid(1218823)]':
        call avg102105
    '[convertstrid(1218824)]':
        call avg102106
    '[convertstrid(1218825)]':
        call avg102107
return _return