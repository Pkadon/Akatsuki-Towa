label avg26015(trans=fade_in):

$ play_music("ED6301.ogg")
scene placeholderbackground
$ update_narrator('c23')
$ update_portrait('oc002_01 14', 'p2', [r(-3), light], 6)
window show
with trans
$ update_portrait('oc002_01 14', 'p2', [r(-3), r_shake, light], 6)
get_char('c23') '[convertstrid(1215595)]' (**arg(1, 1215595))
$ update_portrait('oc002_01 14', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 18', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1215596)]' (**arg(2, 1215596))
$ update_portrait('oc001_01 18', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc002_01 10', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1215597)]' (**arg(3, 1215597))
$ update_portrait('oc002_01 5', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1215598)]' (**arg(4, 1215598))
$ update_portrait('oc002_01 5', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 8', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1215599)]' (**arg(5, 1215599))
$ update_portrait('oc001_01 8', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc002_01 10', 'p2', [r(-3), r_shake, light], 6)
get_char('c23') '[convertstrid(1215600)]' (**arg(6, 1215600))
hide p1
hide p2
play sfx2 "other_7002.ogg"
get_char('c0') '[convertstrid(1215745)]' (**arg(7, 1215745))
get_char('c0') '[convertstrid(1215601)]' (**arg(8, 1215601))
get_char('c0') '[convertstrid(1215602)]' (**arg(9, 1215602))
get_char('c0') '[convertstrid(1215603)]' (**arg(10, 1215603))
return "avg26015"