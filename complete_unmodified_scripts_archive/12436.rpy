label avg12436(trans=fade_in):

$ play_music("ed7566.ogg")
scene avg_bg_036
$ update_portrait('sc046_01 4', 'p1004', [l(-5), light, flip], 6)
$ update_narrator('c10041')
window show
with trans
get_char('c10041') '[convertstrid(1143138)]' (**arg(1, 1143138))
$ update_portrait('sc046_01 4', 'p1004', [l(-5), dark, flip], 5)
$ update_portrait('oc002_01 4', 'p2', [r_entrance(-3), r_shake, light], 6)
get_char('c23') '[convertstrid(1143139)]' (**arg(2, 1143139))
hide p1004
$ update_portrait('oc002_01 4', 'p2', [r(-3), dark], 5)
$ update_portrait('oc003_01 17', 'p3', [l(-6), light, flip], 6)
play sfxvoice "avg_vocal_ro09.ogg"
get_char('c31') '[convertstrid(1143140)]' (**arg(3, 1143140))
hide p3
$ update_portrait('sc046_01 4', 'p1004', [l(-5), light, flip], 6)
get_char('c10041') '[convertstrid(1143141)]' (**arg(4, 1143141))
hide p2
$ update_portrait('sc046_01 4', 'p1004', [l(-5), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1143142)]' (**arg(5, 1143142))
$ update_portrait('oc001_01 16', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1143143)]' (**arg(6, 1143143))
hide p1004
$ update_portrait('oc001_01 16', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 17', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1143144)]' (**arg(7, 1143144))
hide p3
$ update_portrait('sc046_01 4', 'p1004', [l(-5), light, flip], 6)
get_char('c10041') '[convertstrid(1143145)]' (**arg(8, 1143145))
$ update_portrait('sc046_01 4', 'p1004', [l(-5), light, flip], 6)
get_char('c10041') '[convertstrid(1143146)]' (**arg(9, 1143146))
hide p1
$ update_portrait('sc046_01 4', 'p1004', [l(-5), dark, flip], 5)
$ update_portrait('oc002_01 5', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1143147)]' (**arg(10, 1143147))
hide p2
$ update_portrait('oc001_01 2', 'p1', [r(-2), r_shake, light], 6)
get_char('c13') '[convertstrid(1143148)]' (**arg(11, 1143148))
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1143149)]' (**arg(12, 1143149))
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('sc046_01 4', 'p1004', [l(-5), light, flip], 6)
get_char('c10041') '[convertstrid(1143150)]' (**arg(13, 1143150))
$ update_portrait('sc046_01 4', 'p1004', [l(-5), light, flip], 6)
get_char('c10041') '[convertstrid(1143151)]' (**arg(14, 1143151))
$ update_portrait('sc046_01 4', 'p1004', [l(-5), light, flip], 6)
get_char('c10041') '[convertstrid(1143152)]' (**arg(15, 1143152))
hide p1
$ update_portrait('sc046_01 4', 'p1004', [l(-5), dark, flip], 5)
$ update_portrait('oc002_01 21', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1143153)]' (**arg(16, 1143153))
hide p2
$ update_portrait('oc001_01 17', 'p1', [r(-2), r_shake, light], 6)
get_char('c13') '[convertstrid(1143154)]' (**arg(17, 1143154))
$ update_portrait('oc001_01 17', 'p1', [r(-2), dark], 5)
$ update_portrait('sc046_01 1', 'p1004', [l(-5), light, flip], 6)
get_char('c10041') '[convertstrid(1143155)]' (**arg(18, 1143155))
hide p1
$ update_portrait('sc046_01 1', 'p1004', [l(-5), dark, flip], 5)
$ update_portrait('oc002_01 8', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1143156)]' (**arg(19, 1143156))
hide p2
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1143157)]' (**arg(20, 1143157))
hide p1004
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 5', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1143158)]' (**arg(21, 1143158))
hide p3
hide p1
$ update_portrait('sc046_01 4', 'p1004', [l(-5), light, flip], 6)
$ update_narrator('c10041')
with fade
get_char('c10041') '[convertstrid(1143159)]' (**arg(22, 1143159))
$ update_portrait('sc046_01 4', 'p1004', [l(-5), dark, flip], 5)
get_char('c11123') '[convertstrid(1143160)]' (**arg(23, 1143160, size=(1.2))) with shake
return "avg12436"