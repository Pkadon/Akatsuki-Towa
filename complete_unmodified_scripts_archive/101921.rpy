label avg101921(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('sc011_01 2', 'p19', [l(-1), light, flip], 6)
$ update_narrator('c191')
window show
with trans
get_char('c191') '[convertstrid(1218383)]' (**arg(1, 1218383))
$ update_portrait('sc011_01 2', 'p19', [l(-1), dark, flip], 5)
$ update_portrait('oc001_01 23', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1218384)]' (**arg(2, 1218384))
$ update_portrait('oc001_01 23', 'p1', [r(-2), dark], 5)
$ update_portrait('sc011_01 4', 'p19', [l(-1), light, flip], 6)
get_char('c191') '[convertstrid(1218385)]' (**arg(3, 1218385))
menu:
    extend ""
    '[convertstrid(1218386)]':
        call avg101922
    '[convertstrid(1218387)]':
        call avg101923
    '[convertstrid(1218388)]':
        call avg101924
return _return