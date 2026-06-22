label avg1108:

$ play_music("ed7106.ogg")
scene avg_bg_013
$ update_narrator('c0')
window show
with fade_in
get_char('c0') '[convertstrid(2102659)]' (**arg(1, 2102659))
get_char('c7481') '[convertstrid(2102660)]' (**arg(2, 2102660))
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2102661)]' (**arg(3, 2102661))
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 1', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(2102662)]' (**arg(4, 2102662))
hide p3
$ update_portrait('oc002_01 14', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(2102663)]' (**arg(5, 2102663))
hide p1
$ update_portrait('oc002_01 14', 'p2', [l(-3), dark, flip], 5)
get_char('c10893') '[convertstrid(2102664)]' (**arg(6, 2102664))
hide p2
get_char('c7481') '[convertstrid(2102665)]' (**arg(7, 2102665))
get_char('c0') '[convertstrid(2102666)]' (**arg(8, 2102666))
$ update_portrait('oc002_01 8', 'p2', [r(-3), light], 6)
play sfxvoice "bcv_oc002_c02_01.ogg"
get_char('c23') '[convertstrid(2102667)]' (**arg(9, 2102667))
$ update_portrait('oc002_01 8', 'p2', [r(-3), dark], 5)
$ update_portrait('st004_01 5', 'p204', [l(4), light, flip], 6)
get_char('c2041') '[convertstrid(2102668)]' (**arg(10, 2102668))
return