label avg102004:

stop music
scene placeholderbackground
$ update_portrait('sc012_01 2', 'p20', [l(-16), light, flip], 6)
$ update_narrator('c201')
window show
with fade_in
get_char('c201') '[convertstrid(1218639)]' (**arg(1, 1218639))
$ update_portrait('sc012_01 2', 'p20', [l(-16), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1218640)]' (**arg(2, 1218640))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('sc012_01 4', 'p20', [l(-16), light, flip], 6)
get_char('c201') '[convertstrid(1218641)]' (**arg(3, 1218641))
menu:
    extend ""
    '[convertstrid(1218642)]':
        call avg102005
    '[convertstrid(1218643)]':
        call avg102006
    '[convertstrid(1218644)]':
        call avg102007
return