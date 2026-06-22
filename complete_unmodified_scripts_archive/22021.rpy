label avg22021:

$ play_music("ed7105.ogg")
scene placeholderbackground
$ update_portrait('sc049_01 5', 'p56', [mid(-8), light], 6)
$ update_narrator('c563')
window show
with fade_in
get_char('c563') '[convertstrid(1120002)]' (**arg(1, 1120002))
hide p56
$ update_portrait('oc001_01 8', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1120003)]' (**arg(2, 1120003))
hide p1
$ update_portrait('sc049_01 1', 'p56', [mid(-8), light], 6)
play sfx2 "other_7091.ogg"
get_char('c563') '[convertstrid(1120004)]' (**arg(3, 1120004))
hide p56
$ update_portrait('sc050_01 1', 'p57', [mid(-19), light], 6)
get_char('c573') '[convertstrid(1120005)]' (**arg(4, 1120005))
hide p57
$ update_portrait('sc052_01 5', 'p59', [mid(-25), light], 6)
get_char('c593') '[convertstrid(1120006)]' (**arg(5, 1120006))
hide p59
$ update_portrait('oc002_01 12', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1120007)]' (**arg(6, 1120007))
menu:
    extend ""
    '[convertstrid(1120008)]':
        call avg22022
    '[convertstrid(1120009)]':
        call avg22023
return