label avg101221(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('sc004_01 4', 'p12', [l(-12), light, flip], 6)
$ update_narrator('c121')
window show
with trans
get_char('c121') '[convertstrid(1220719)]' (**arg(1, 1220719))
$ update_portrait('sc004_01 4', 'p12', [l(-12), dark, flip], 5)
$ update_portrait('oc001_01 12', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1220720)]' (**arg(2, 1220720))
$ update_portrait('oc001_01 12', 'p1', [r(-2), dark], 5)
$ update_portrait('sc004_01 3', 'p12', [l(-12), light, flip], 6)
get_char('c121') '[convertstrid(1220721)]' (**arg(3, 1220721))
$ update_portrait('sc004_01 3', 'p12', [l(-12), dark, flip], 5)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1220722)]' (**arg(4, 1220722))
menu:
    extend ""
    '[convertstrid(1220723)]':
        call avg101222
    '[convertstrid(1220724)]':
        call avg101223
    '[convertstrid(1220725)]':
        call avg101224
return _return