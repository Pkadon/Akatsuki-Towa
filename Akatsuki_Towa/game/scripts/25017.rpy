label avg25017:

stop music
scene placeholderbackground
$ update_portrait('oc002_01 9', 'p2', [mid(-3), light], 6)
$ update_narrator('c23')
window show
with fade_in
get_char('c23') '[convertstrid(1210036)]' (**arg(1, 1210036))
hide p2
$ update_portrait('oc001_01 9', 'p1', [mid(-2), light], 6)
play sfx2 "other_7079.ogg"
get_char('c13') '[convertstrid(1210037)]' (**arg(2, 1210037))
hide p1
$ update_portrait('oc002_01 4', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1210038)]' (**arg(3, 1210038))
menu:
    extend ""
    '[convertstrid(1214998)]':
        call avg25027
    '[convertstrid(1215000)]':
        call avg25026
return