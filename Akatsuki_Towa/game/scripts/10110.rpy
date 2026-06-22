label avg10110:

$ play_music("ed7516.ogg")
scene avg_bg_014
$ update_portrait('oc001_01 2', 'p1', [l(-2), light, flip], 6)
$ update_narrator('c11')
window show
with fade_in
play sfx2 "other_7071.ogg"
get_char('c11') '[convertstrid(1006182)]' (**arg(1, 1006182))
$ update_portrait('oc001_01 1', 'p1', [l(-2), light, flip], 6)
play sfx2 "other_7072.ogg"
get_char('c11') '[convertstrid(1006183)]' (**arg(2, 1006183))
$ update_portrait('oc001_01 1', 'p1', [l(-2), dark, flip], 5)
get_char('c5243') '[convertstrid(1006184)]' (**arg(3, 1006184))
$ update_portrait('oc001_01 6', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1006185)]' (**arg(4, 1006185))
$ update_portrait('oc001_01 6', 'p1', [l(-2), dark, flip], 5)
get_char('c5243') '[convertstrid(1006186)]' (**arg(5, 1006186))
$ update_portrait('oc001_01 2', 'p1', [l(-2), light, flip], 6)
play sfx2 "other_7073.ogg"
get_char('c11') '[convertstrid(1006187)]' (**arg(6, 1006187))
$ update_portrait('oc001_01 1', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1006188)]' (**arg(7, 1006188))
scene avg_bg_023
$ update_portrait('sc051_01 2', 'p58', [l(-32), light, flip], 6)
$ update_narrator('c581')
with fade
play sfx2 "other_7047.ogg"
get_char('c581') '[convertstrid(1006189)]' (**arg(8, 1006189))
$ update_portrait('sc051_01 2', 'p58', [l(-32), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1006190)]' (**arg(9, 1006190))
hide p58
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('sc050_01 1', 'p57', [l(-19), light, flip], 6)
get_char('c571') '[convertstrid(1006191)]' (**arg(10, 1006191))
hide p1
$ update_portrait('sc050_01 1', 'p57', [l(-19), dark, flip], 5)
$ update_portrait('oc002_01 8', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1006192)]' (**arg(11, 1006192))
hide p57
$ update_portrait('oc002_01 8', 'p2', [r(-3), dark], 5)
$ update_portrait('sc049_01 1', 'p56', [l_entrance(-8), light, flip], 6)
get_char('c561') '[convertstrid(1006193)]' (**arg(12, 1006193))
$ update_portrait('sc049_01 8', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(1006194)]' (**arg(13, 1006194))
$ update_portrait('sc049_01 2', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(1006195)]' (**arg(14, 1006195))
hide p2
$ update_portrait('sc049_01 2', 'p56', [l(-8), dark, flip], 5)
$ update_portrait('oc003_01 1', 'p3', [r(-6), light], 6)
play sfxvoice "avg_vocal_ro02.ogg"
get_char('c33') '[convertstrid(1006196)]' (**arg(15, 1006196))
hide p56
$ update_portrait('oc003_01 1', 'p3', [r(-6), dark], 5)
$ update_portrait('oc004_01 1', 'p4', [l(-5), light, flip], 6)
play sfxvoice "avg_vocal_li03.ogg"
get_char('c41') '[convertstrid(1006197)]' (**arg(16, 1006197))
hide p4
$ update_portrait('sc049_01 5', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(1006198)]' (**arg(17, 1006198))
hide p3
$ update_portrait('sc049_01 5', 'p56', [l(-8), dark, flip], 5)
$ update_portrait('sc050_01 1', 'p57', [r(-19), light], 6)
get_char('c573') '[convertstrid(1006199)]' (**arg(18, 1006199))
hide p56
$ update_portrait('sc050_01 1', 'p57', [r(-19), dark], 5)
$ update_portrait('oc002_01 8', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1006200)]' (**arg(19, 1006200))
$ update_portrait('oc002_01 10', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1006201)]' (**arg(20, 1006201))
hide p57
$ update_portrait('oc002_01 10', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('sc051_01 4', 'p58', [r(-32), light], 6)
get_char('c583') '[convertstrid(1006202)]' (**arg(21, 1006202))
hide p2
$ update_portrait('sc051_01 4', 'p58', [r(-32), dark], 5)
$ update_portrait('oc001_01 4', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1006203)]' (**arg(22, 1006203))
hide p58
$ update_portrait('oc001_01 4', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('sc052_01 4', 'p59', [r(-25), light], 6)
get_char('c593') '[convertstrid(1006204)]' (**arg(23, 1006204))
hide p1
$ update_portrait('sc052_01 4', 'p59', [r(-25), dark], 5)
$ update_portrait('sc053_01 4', 'p60', [l(-32), light, flip], 6)
get_char('c601') '[convertstrid(1006205)]' (**arg(24, 1006205))
hide p60
$ update_portrait('oc001_01 8', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1001773)]' (**arg(25, 1001773))
hide p59
$ update_portrait('oc001_01 8', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc004_01 2', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1006207)]' (**arg(26, 1006207))
hide p1
$ update_portrait('oc004_01 2', 'p4', [r(-5), dark], 5)
$ update_portrait('oc003_01 5', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1006208)]' (**arg(27, 1006208))
$ update_portrait('oc003_01 8', 'p3', [l(-6), light, flip], 6)
play sfxvoice "avg_vocal_ro13.ogg"
get_char('c31') '[convertstrid(1006209)]' (**arg(28, 1006209))
hide p4
$ update_portrait('oc003_01 8', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc002_01 10', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1006210)]' (**arg(29, 1006210))
hide p3
$ update_portrait('oc002_01 10', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 8', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1006211)]' (**arg(30, 1006211))
$ update_portrait('oc001_01 8', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc002_01 7', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1006212)]' (**arg(31, 1006212))
$ update_portrait('oc002_01 4', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1006213)]' (**arg(32, 1006213))
hide p1
$ update_portrait('oc002_01 4', 'p2', [r(-3), dark], 5)
$ update_portrait('oc004_01 7', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1006214)]' (**arg(33, 1006214))
hide p2
$ update_portrait('oc004_01 7', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc003_01 8', 'p3', [r(-6), light], 6)
play sfxvoice "avg_vocal_ro13.ogg"
get_char('c33') '[convertstrid(1006215)]' (**arg(34, 1006215))
$ update_portrait('oc003_01 1', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1006216)]' (**arg(35, 1006216))
hide p4
$ update_portrait('oc003_01 1', 'p3', [r(-6), dark], 5)
$ update_portrait('oc001_01 5', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1006217)]' (**arg(36, 1006217))
$ update_portrait('oc001_01 5', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc003_01 1', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1006218)]' (**arg(37, 1006218))
$ update_portrait('oc003_01 1', 'p3', [r(-6), dark], 5)
$ update_portrait('oc001_01 1', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1006219)]' (**arg(38, 1006219))
hide p3
$ update_portrait('oc001_01 1', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('sc049_01 2', 'p56', [r(-8), light], 6)
get_char('c563') '[convertstrid(1006220)]' (**arg(39, 1006220))
$ update_portrait('sc049_01 2', 'p56', [r(-8), dark], 5)
$ update_portrait('oc001_01 1', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1006221)]' (**arg(40, 1006221))
$ update_portrait('oc001_01 4', 'p1', [l(-2), light, flip], 6)
play sfxvoice "avg_vocal_na10.ogg"
get_char('c11') '[convertstrid(1006222)]' (**arg(41, 1006222))
menu:
    extend ""
    '[convertstrid(1006223)]':
        call avg10111
    '[convertstrid(1006224)]':
        call avg10112
    '[convertstrid(1006225)]':
        call avg10111
return