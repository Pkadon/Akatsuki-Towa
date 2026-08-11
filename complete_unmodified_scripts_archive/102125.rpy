label avg102125(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('sc013_01 3', 'p21', [l(-12), light, flip], 6)
$ update_narrator('c211')
window show
with trans
get_char('c211') '[convertstrid(1218879)]' (**arg(1, 1218879))
$ update_portrait('sc013_01 3', 'p21', [l(-12), dark, flip], 5)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1218880)]' (**arg(2, 1218880))
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('sc013_01 1', 'p21', [l(-12), light, flip], 6)
get_char('c211') '[convertstrid(1218881)]' (**arg(3, 1218881))
menu:
    extend ""
    '[convertstrid(1218882)]':
        call avg102126
    '[convertstrid(1218883)]':
        call avg102127
    '[convertstrid(1218884)]':
        call avg102128
return _return