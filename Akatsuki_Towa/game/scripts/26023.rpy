label avg26023(trans=fade_in):

$ play_music("ED6201.ogg")
scene avg_bg_004
$ update_narrator('c23')
$ update_portrait('oc002_01 12', 'p2', [r(-3), light], 6)
window show
with trans
$ update_portrait('oc002_01 12', 'p2', [r(-3), r_shake, light], 6)
get_char('c23') '[convertstrid(1215654)]' (**arg(1, 1215654))
$ update_portrait('oc002_01 12', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 7', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1215655)]' (**arg(2, 1215655))
return "avg26023"