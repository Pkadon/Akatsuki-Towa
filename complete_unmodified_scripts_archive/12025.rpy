label avg12025(trans=fade_in):

$ play_music("ed7106.ogg")
scene avg_bg_008
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
window show
with trans
get_char('c13') '[convertstrid(1120042)]' (**arg(1, 1120042))
hide p1
$ update_portrait('sc011_01 3', 'p19', [r(-1), r_shake, light], 6)
get_char('c193') '[convertstrid(1120043)]' (**arg(2, 1120043))
$ update_portrait('sc011_01 3', 'p19', [r(-1), dark], 5)
$ update_portrait('sc012_01 3', 'p20', [l(-16), light, flip], 6)
get_char('c201') '[convertstrid(1120044)]' (**arg(3, 1120044))
$ update_portrait('sc012_01 3', 'p20', [l(-16), dark, flip], 5)
$ update_portrait('sc011_01 2', 'p19', [r(-1), r_shake, light], 6)
get_char('c193') '[convertstrid(1120045)]' (**arg(4, 1120045))
hide p19
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
play sfxvoice "avg_vocal_ch16.ogg"
get_char('c23') '[convertstrid(1120046)]' (**arg(5, 1120046))
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
$ update_portrait('sc012_01 2', 'p20', [l(-16), light, flip], 6)
get_char('c201') '[convertstrid(1120047)]' (**arg(6, 1120047))
hide p2
$ update_portrait('sc012_01 2', 'p20', [l(-16), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1120048)]' (**arg(7, 1120048))
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('sc012_01 5', 'p20', [l(-16), light, flip], 6)
get_char('c201') '[convertstrid(1120049)]' (**arg(8, 1120049))
hide p20
$ update_portrait('sc011_01 4', 'p19', [l(-1), light, flip], 6)
get_char('c191') '[convertstrid(1120050)]' (**arg(9, 1120050))
$ update_portrait('sc011_01 4', 'p19', [l(-1), dark, flip], 5)
$ update_portrait('oc001_01 12', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1120051)]' (**arg(10, 1120051))
hide p1
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1120052)]' (**arg(11, 1120052))
hide p19
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
$ update_portrait('sc012_01 4', 'p20', [l(-16), light, flip], 6)
get_char('c201') '[convertstrid(1120053)]' (**arg(12, 1120053))
hide p2
$ update_portrait('sc012_01 4', 'p20', [l(-16), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1120054)]' (**arg(13, 1120054))
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('sc012_01 4', 'p20', [l(-16), light, flip], 6)
get_char('c201') '[convertstrid(1120055)]' (**arg(14, 1120055))
$ update_portrait('sc012_01 4', 'p20', [l(-16), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1121385)]' (**arg(15, 1121385))
hide p20
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('sc011_01 4', 'p19', [l(-1), light, flip], 6)
get_char('c191') '[convertstrid(1121386)]' (**arg(16, 1121386))
hide p19
$ update_portrait('sc012_01 2', 'p20', [l(-16), light, flip], 6)
get_char('c201') '[convertstrid(1121387)]' (**arg(17, 1121387))
$ update_portrait('sc012_01 4', 'p20', [l(-16), light, flip], 6)
get_char('c201') '[convertstrid(1121388)]' (**arg(18, 1121388))
$ update_portrait('sc012_01 4', 'p20', [l(-16), dark, flip], 5)
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1121389)]' (**arg(19, 1121389))
hide p20
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
$ update_portrait('sc011_01 2', 'p19', [l(-1), light, flip], 6)
get_char('c191') '[convertstrid(1121390)]' (**arg(20, 1121390))
return "avg12025"