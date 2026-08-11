label avg102025(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('sc012_01 4', 'p20', [l(-16), light, flip], 6)
$ update_narrator('c201')
window show
with trans
get_char('c201') '[convertstrid(1218695)]' (**arg(1, 1218695))
$ update_portrait('sc012_01 4', 'p20', [l(-16), dark, flip], 5)
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1218696)]' (**arg(2, 1218696))
$ update_portrait('oc001_01 7', 'p1', [r(-2), dark], 5)
$ update_portrait('sc012_01 1', 'p20', [l(-16), light, flip], 6)
get_char('c201') '[convertstrid(1218697)]' (**arg(3, 1218697))
menu:
    extend ""
    '[convertstrid(1218698)]':
        call avg102026
    '[convertstrid(1218699)]':
        call avg102027
    '[convertstrid(1218700)]':
        call avg102028
return _return