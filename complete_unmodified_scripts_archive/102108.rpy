label avg102108(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('sc013_01 5', 'p21', [l(-12), light, flip], 6)
$ update_narrator('c211')
window show
with trans
get_char('c211') '[convertstrid(1218830)]' (**arg(1, 1218830))
$ update_portrait('sc013_01 5', 'p21', [l(-12), dark, flip], 5)
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1218831)]' (**arg(2, 1218831))
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
$ update_portrait('sc013_01 1', 'p21', [l(-12), light, flip], 6)
get_char('c211') '[convertstrid(1218832)]' (**arg(3, 1218832))
menu:
    extend ""
    '[convertstrid(1218833)]':
        call avg102109
    '[convertstrid(1218834)]':
        call avg102110
    '[convertstrid(1218835)]':
        call avg102111
return _return