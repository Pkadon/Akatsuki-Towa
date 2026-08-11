label avg102021(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('sc012_01 4', 'p20', [l(-16), light, flip], 6)
$ update_narrator('c201')
window show
with trans
get_char('c201') '[convertstrid(1218685)]' (**arg(1, 1218685))
$ update_portrait('sc012_01 4', 'p20', [l(-16), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1218686)]' (**arg(2, 1218686))
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('sc012_01 1', 'p20', [l(-16), light, flip], 6)
get_char('c201') '[convertstrid(1218687)]' (**arg(3, 1218687))
menu:
    extend ""
    '[convertstrid(1218688)]':
        call avg102022
    '[convertstrid(1218689)]':
        call avg102023
    '[convertstrid(1218690)]':
        call avg102024
return _return