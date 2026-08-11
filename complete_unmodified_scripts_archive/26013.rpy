label avg26013(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with trans
get_char('c13') '[convertstrid(1215580)]' (**arg(1, 1215580))
hide p1
$ update_portrait('oc002_01 4', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1215581)]' (**arg(2, 1215581))
$ update_portrait('oc002_01 4', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1215582)]' (**arg(3, 1215582))
hide p2
$ update_portrait('oc001_01 3', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1215583)]' (**arg(4, 1215583))
hide p1
$ update_portrait('oc002_01 12', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1215584)]' (**arg(5, 1215584))
hide p2
$ update_portrait('oc001_01 12', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1215585)]' (**arg(6, 1215585))
hide p1
play sfx2 "other_7002.ogg"
get_char('c0') '[convertstrid(1215744)]' (**arg(7, 1215744))
get_char('c0') '[convertstrid(1215586)]' (**arg(8, 1215586))
get_char('c0') '[convertstrid(1215587)]' (**arg(9, 1215587))
get_char('c0') '[convertstrid(1215588)]' (**arg(10, 1215588))
return "avg26013"