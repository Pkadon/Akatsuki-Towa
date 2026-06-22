label avg101125:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
get_char('c13') '[convertstrid(1220456)]' (**arg(1, 1220456))
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
$ update_portrait('sc003_01 2', 'p11', [l(-4), light, flip], 6)
get_char('c111') '[convertstrid(1220457)]' (**arg(2, 1220457))
$ update_portrait('sc003_01 2', 'p11', [l(-4), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1220458)]' (**arg(3, 1220458))
menu:
    extend ""
    '[convertstrid(1220459)]':
        call avg101126
    '[convertstrid(1220460)]':
        call avg101127
    '[convertstrid(1220461)]':
        call avg101128
return