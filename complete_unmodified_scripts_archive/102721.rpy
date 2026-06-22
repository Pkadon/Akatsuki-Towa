label avg102721:

stop music
scene placeholderbackground
$ update_portrait('sc019_01 2', 'p27', [l(-18), light, flip], 6)
$ update_narrator('c271')
window show
with fade_in
get_char('c271') '[convertstrid(1219497)]' (**arg(1, 1219497))
$ update_portrait('sc019_01 2', 'p27', [l(-18), dark, flip], 5)
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1219498)]' (**arg(2, 1219498))
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
$ update_portrait('sc019_01 1', 'p27', [l(-18), light, flip], 6)
get_char('c271') '[convertstrid(1219499)]' (**arg(3, 1219499))
menu:
    extend ""
    '[convertstrid(1219500)]':
        call avg102722
    '[convertstrid(1219501)]':
        call avg102723
    '[convertstrid(1219502)]':
        call avg102724
return