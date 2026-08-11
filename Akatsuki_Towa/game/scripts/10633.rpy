label avg10633(trans=fade_in):

$ play_music("ED6105.ogg")
scene avg_bg_023
$ update_narrator('c5001')
window show
with trans
get_char('c5001') '[convertstrid(1164029)]' (**arg(1, 1164029))
get_char('c5001') '[convertstrid(1164030)]' (**arg(2, 1164030))
get_char('c13351') '[convertstrid(1164031)]' (**arg(3, 1164031))
$ update_portrait('oc001_01 22', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1164032)]' (**arg(4, 1164032))
hide p1
get_char('c0') '[convertstrid(1164033)]' (**arg(5, 1164033))
get_char('c13351') '[convertstrid(1164034)]' (**arg(6, 1164034))
$ update_portrait('oc002_01 22', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1164035)]' (**arg(7, 1164035))
hide p2
$ update_portrait('st061_01 5', 'p1304', [r(-2), light], 6)
get_char('c13043') '[convertstrid(1164036)]' (**arg(8, 1164036))
$ update_portrait('st061_01 5', 'p1304', [r(-2), dark], 5)
$ update_portrait('oc004_01 2', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1164037)]' (**arg(9, 1164037))
$ update_portrait('oc004_01 2', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('st061_01 1', 'p1304', [r(-2), light], 6)
get_char('c13043') '[convertstrid(1164038)]' (**arg(10, 1164038))
hide p4
$ update_portrait('st061_01 1', 'p1304', [r(-2), dark], 5)
get_char('c13351') '[convertstrid(1164039)]' (**arg(11, 1164039))
$ update_portrait('st061_01 5', 'p1304', [r(-2), light], 6)
get_char('c13043') '[convertstrid(1164040)]' (**arg(12, 1164040))
$ update_portrait('st061_01 5', 'p1304', [r(-2), dark], 5)
get_char('c13351') '[convertstrid(1164041)]' (**arg(13, 1164041))
get_char('c13351') '[convertstrid(1164042)]' (**arg(14, 1164042))
get_char('c13351') '[convertstrid(1164043)]' (**arg(15, 1164043))
hide p1304
$ update_portrait('sc010_01 2', 'p18', [r(-10), light], 6)
get_char('c183') '[convertstrid(1164044)]' (**arg(16, 1164044))
$ update_portrait('sc010_01 2', 'p18', [r(-10), dark], 5)
get_char('c13351') '[convertstrid(1164045)]' (**arg(17, 1164045))
get_char('c13351') '[convertstrid(1164046)]' (**arg(18, 1164046))
hide p18
$ update_portrait('st061_01 6', 'p1304', [r(-2), light], 6)
get_char('c13043') '[convertstrid(1164047)]' (**arg(19, 1164047))
$ update_portrait('st061_01 6', 'p1304', [r(-2), dark], 5)
$ update_portrait('oc003_01 17', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1164048)]' (**arg(20, 1164048))
hide p1304
$ update_portrait('oc003_01 17', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
play sfx2 "other_7004.ogg"
get_char('c23') '[convertstrid(1164049)]' (**arg(21, 1164049))
hide p3
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
get_char('c13351') '[convertstrid(1164050)]' (**arg(22, 1164050))
get_char('c13351') '[convertstrid(1164051)]' (**arg(23, 1164051))
hide p2
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1164052)]' (**arg(24, 1164052))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
get_char('c13351') '[convertstrid(1164053)]' (**arg(25, 1164053))
hide p1
$ update_portrait('oc004_01 4', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1164054)]' (**arg(26, 1164054))
$ update_portrait('oc004_01 4', 'p4', [r(-5), dark], 5)
get_char('c13351') '[convertstrid(1164055)]' (**arg(27, 1164055))
get_char('c13351') '[convertstrid(1164056)]' (**arg(28, 1164056))
hide p4
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1164057)]' (**arg(29, 1164057))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
get_char('c13351') '[convertstrid(1164058)]' (**arg(30, 1164058))
get_char('c13351') '[convertstrid(1164059)]' (**arg(31, 1164059))
hide p1
$ update_portrait('oc002_01 6', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1164060)]' (**arg(32, 1164060))
hide p2
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1164061)]' (**arg(33, 1164061))
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
get_char('c13351') '[convertstrid(1164062)]' (**arg(34, 1164062))
return "avg10633"