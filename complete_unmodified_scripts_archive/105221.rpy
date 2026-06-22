label avg105221:

stop music
scene placeholderbackground
$ update_portrait('sc052_01 1', 'p59', [l(-25), light, flip], 6)
$ update_narrator('c591')
window show
with fade_in
get_char('c591') '[convertstrid(1219308)]' (**arg(1, 1219308))
$ update_portrait('sc052_01 1', 'p59', [l(-25), light, flip], 6)
get_char('c591') '[convertstrid(1219309)]' (**arg(2, 1219309))
$ update_portrait('sc052_01 1', 'p59', [l(-25), dark, flip], 5)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1219310)]' (**arg(3, 1219310))
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('sc052_01 5', 'p59', [l(-25), light, flip], 6)
get_char('c591') '[convertstrid(1219311)]' (**arg(4, 1219311))
menu:
    extend ""
    '[convertstrid(1219312)]':
        call avg105222
    '[convertstrid(1219313)]':
        call avg105223
    '[convertstrid(1219314)]':
        call avg105224
return