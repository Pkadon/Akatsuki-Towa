label avg26025(trans=fade_in):

$ play_music("ED6201.ogg")
scene avg_bg_004
$ update_portrait('oc001_01 4', 'p1', [l(-2), light, flip], 6)
$ update_narrator('c11')
window show
with trans
get_char('c11') '[convertstrid(1215665)]' (**arg(1, 1215665))
$ update_portrait('oc001_01 4', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc002_01 2', 'p2', [r_midback(-3), light], 6)
get_char('c23') '[convertstrid(1215666)]' (**arg(2, 1215666))
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 7', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1215667)]' (**arg(3, 1215667))
$ update_portrait('oc001_01 7', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc002_01 8', 'p2', [r(-3), r_shake, light], 6)
get_char('c23') '[convertstrid(1215668)]' (**arg(4, 1215668))
return "avg26025"