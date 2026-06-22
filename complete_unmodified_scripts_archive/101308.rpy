label avg101308:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 22', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
get_char('c13') '[convertstrid(1220970)]' (**arg(1, 1220970))
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1220971)]' (**arg(2, 1220971))
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('sc005_01 1', 'p13', [l(-17), light, flip], 6)
get_char('c131') '[convertstrid(1220972)]' (**arg(3, 1220972))
$ update_portrait('sc005_01 1', 'p13', [l(-17), dark, flip], 5)
$ update_portrait('oc001_01 12', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1220973)]' (**arg(4, 1220973))
menu:
    extend ""
    '[convertstrid(1220974)]':
        call avg101309
    '[convertstrid(1220975)]':
        call avg101310
    '[convertstrid(1220976)]':
        call avg101311
return