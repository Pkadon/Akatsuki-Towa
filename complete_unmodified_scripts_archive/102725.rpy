label avg102725:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
get_char('c13') '[convertstrid(1219507)]' (**arg(1, 1219507))
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('sc019_01 1', 'p27', [l(-18), light, flip], 6)
get_char('c271') '[convertstrid(1219508)]' (**arg(2, 1219508))
$ update_portrait('sc019_01 4', 'p27', [l(-18), light, flip], 6)
get_char('c271') '[convertstrid(1219509)]' (**arg(3, 1219509))
menu:
    extend ""
    '[convertstrid(1219510)]':
        call avg102726
    '[convertstrid(1219511)]':
        call avg102727
    '[convertstrid(1219512)]':
        call avg102728
return