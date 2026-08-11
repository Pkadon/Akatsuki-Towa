label avg102704(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
window show
with trans
get_char('c13') '[convertstrid(1219451)]' (**arg(1, 1219451))
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('sc019_01 3', 'p27', [l(-18), light, flip], 6)
get_char('c271') '[convertstrid(1219452)]' (**arg(2, 1219452))
$ update_portrait('sc019_01 1', 'p27', [l(-18), light, flip], 6)
get_char('c271') '[convertstrid(1219453)]' (**arg(3, 1219453))
menu:
    extend ""
    '[convertstrid(1219454)]':
        call avg102705
    '[convertstrid(1219455)]':
        call avg102706
    '[convertstrid(1219456)]':
        call avg102707
return _return