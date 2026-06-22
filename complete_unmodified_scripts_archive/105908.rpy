label avg105908:

stop music
scene placeholderbackground
$ update_portrait('sc052_01 3', 'p59', [l(-25), light, flip], 6)
$ update_narrator('c591')
window show
with fade_in
get_char('c591') '[convertstrid(1219268)]' (**arg(1, 1219268))
$ update_portrait('sc052_01 3', 'p59', [l(-25), dark, flip], 5)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1219269)]' (**arg(2, 1219269))
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('sc052_01 5', 'p59', [l(-25), light, flip], 6)
get_char('c591') '[convertstrid(1219270)]' (**arg(3, 1219270))
$ update_portrait('sc052_01 5', 'p59', [l(-25), dark, flip], 5)
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1219271)]' (**arg(4, 1219271))
menu:
    extend ""
    '[convertstrid(1219272)]':
        call avg105909
    '[convertstrid(1219273)]':
        call avg105910
    '[convertstrid(1219274)]':
        call avg105911
return