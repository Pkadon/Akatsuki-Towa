label avg10638(trans=fade_in):

$ play_music("ed6324.ogg")
scene avg_bg_070
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
window show
with trans
play sfx2 "fight_6027.ogg"
get_char('c13') '[convertstrid(1164155)]' (**arg(1, 1164155))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('sc010_01 1', 'p18', [l(-10), light, flip], 6)
get_char('c181') '[convertstrid(1164156)]' (**arg(2, 1164156))
hide p1
$ update_portrait('sc010_01 1', 'p18', [l(-10), dark, flip], 5)
$ update_portrait('oc002_01 14', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1164157)]' (**arg(3, 1164157))
hide p2
$ update_portrait('oc003_01 4', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1164158)]' (**arg(4, 1164158))
hide p18
$ update_portrait('oc003_01 4', 'p3', [r(-6), dark], 5)
$ update_portrait('st061_01 5', 'p1304', [l_entrance(-2), light, flip], 6)
get_char('c13041') '[convertstrid(1164159)]' (**arg(5, 1164159))
hide p1304
$ update_portrait('oc002_01 4', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1164160)]' (**arg(6, 1164160))
hide p3
$ update_portrait('oc002_01 4', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1164161)]' (**arg(7, 1164161))
hide p1
$ update_portrait('oc004_01 4', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1164162)]' (**arg(8, 1164162))
hide p2
$ update_portrait('oc004_01 4', 'p4', [r(-5), dark], 5)
$ update_portrait('sc010_01 4', 'p18', [l(-10), light, flip], 6)
get_char('c181') '[convertstrid(1164163)]' (**arg(9, 1164163))
hide p4
$ update_portrait('sc010_01 4', 'p18', [l(-10), dark, flip], 5)
$ update_portrait('oc003_01 4', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1164164)]' (**arg(10, 1164164))
$ update_portrait('oc003_01 4', 'p3', [r(-6), dark], 5)
$ update_portrait('sc010_01 4', 'p18', [l(-10), light, flip], 6)
get_char('c181') '[convertstrid(1164165)]' (**arg(11, 1164165))
$ update_portrait('sc010_01 4', 'p18', [l(-10), light, flip], 6)
get_char('c181') '[convertstrid(1164166)]' (**arg(12, 1164166))
hide p3
$ update_portrait('sc010_01 4', 'p18', [l(-10), dark, flip], 5)
$ update_portrait('oc004_01 11', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1164167)]' (**arg(13, 1164167))
$ update_portrait('oc004_01 11', 'p4', [r(-5), dark], 5)
$ update_portrait('sc010_01 4', 'p18', [l(-10), light, flip], 6)
get_char('c181') '[convertstrid(1164168)]' (**arg(14, 1164168))
hide p18
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1164169)]' (**arg(15, 1164169))
hide p4
$ update_portrait('oc003_01 4', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1164170)]' (**arg(16, 1164170))
hide p3
hide p1
get_char('c0') '[convertstrid(1164171)]' (**arg(17, 1164171))
get_char('c0') '[convertstrid(1164172)]' (**arg(18, 1164172))
return "avg10638"