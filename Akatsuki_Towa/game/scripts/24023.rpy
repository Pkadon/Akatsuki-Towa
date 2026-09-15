label avg24023(trans=fade_in):

$ play_music("ed7105.ogg")
scene avg_bg_041
$ update_portrait('oc005_01 1', 'p5', [r(-6), light], 6)
$ update_narrator('c53')
window show
with trans
get_char('c53') '[convertstrid(1200097)]' (**arg(1, 1200097))
$ update_portrait('oc005_01 1', 'p5', [r(-6), dark], 5)
get_char('c7591') '[convertstrid(1200098)]' (**arg(2, 1200098))
$ update_portrait('oc005_01 8', 'p5', [r(-6), light], 6)
get_char('c53') '[convertstrid(1200099)]' (**arg(3, 1200099))
$ update_portrait('oc005_01 8', 'p5', [r(-6), dark], 5)
get_char('c7591') '[convertstrid(1200100)]' (**arg(4, 1200100))
$ update_portrait('oc005_01 8', 'p5', [r(-6), light], 6)
get_char('c53') '[convertstrid(1200101)]' (**arg(5, 1200101))
return "avg24023"