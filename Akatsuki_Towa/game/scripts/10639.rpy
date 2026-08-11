label avg10639(trans=fade_in):

$ play_music("ED6105.ogg")
scene avg_bg_202
$ update_portrait('oc003_01 1', 'p3', [r(-6), light], 6)
$ update_narrator('c33')
window show
with trans
play sfx2 "other_7071.ogg"
get_char('c33') '[convertstrid(1164174)]' (**arg(1, 1164174))
$ update_portrait('oc003_01 1', 'p3', [r(-6), dark], 5)
play sfx2 "other_7072.ogg"
get_char('c7011') '[convertstrid(1164175)]' (**arg(2, 1164175))
get_char('c7011') '[convertstrid(1164176)]' (**arg(3, 1164176))
hide p3
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1164177)]' (**arg(4, 1164177))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 8', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1164178)]' (**arg(5, 1164178))
hide p4
get_char('c7011') '[convertstrid(1164179)]' (**arg(6, 1164179))
hide p1
$ update_portrait('oc003_01 1', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1164180)]' (**arg(7, 1164180))
$ update_portrait('oc003_01 1', 'p3', [r(-6), dark], 5)
get_char('c7011') '[convertstrid(1164181)]' (**arg(8, 1164181))
$ update_portrait('oc003_01 8', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1164182)]' (**arg(9, 1164182))
hide p3
$ update_portrait('oc002_01 6', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1164183)]' (**arg(10, 1164183))
$ update_portrait('oc002_01 6', 'p2', [r(-3), dark], 5)
get_char('c7011') '[convertstrid(1164184)]' (**arg(11, 1164184))
hide p2
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1164185)]' (**arg(12, 1164185))
return "avg10639"