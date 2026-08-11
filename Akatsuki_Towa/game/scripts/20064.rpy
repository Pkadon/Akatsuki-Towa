label avg20064(trans=fade_in):

$ play_music("ed7151.ogg")
scene avg_bg_034
$ update_portrait('oc002_01 12', 'p2', [l(-3), light, flip], 6)
$ update_narrator('c21')
window show
with trans
play sfx2 "other_7062.ogg"
get_char('c21') '[convertstrid(1003263)]' (**arg(1, 1003263))
$ update_portrait('oc002_01 8', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1003264)]' (**arg(2, 1003264))
$ update_portrait('oc002_01 8', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1003265)]' (**arg(3, 1003265))
hide p2
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1003266)]' (**arg(4, 1003266))
hide p1
$ update_portrait('oc003_01 4', 'p3', [l(-6), dark, flip], 5)
get_char('c6063') '[convertstrid(1003267)]' (**arg(5, 1003267))
hide p3
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch10.ogg"
get_char('c21') '[convertstrid(1003268)]' (**arg(6, 1003268))
hide p2
$ update_portrait('oc001_01 1', 'p1', [l(-2), light, flip], 6)
play sfxvoice "avg_vocal_na15.ogg"
get_char('c11') '[convertstrid(1003269)]' (**arg(7, 1003269))
$ update_portrait('oc001_01 1', 'p1', [l(-2), dark, flip], 5)
get_char('c6063') '[convertstrid(1003270)]' (**arg(8, 1003270))
get_char('c6073') '[convertstrid(1003271)]' (**arg(9, 1003271))
hide p1
$ update_portrait('oc002_01 10', 'p2', [l(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch25.ogg"
get_char('c21') '[convertstrid(1003272)]' (**arg(10, 1003272))
hide p2
$ update_portrait('oc004_01 7', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1003273)]' (**arg(11, 1003273))
$ update_portrait('oc004_01 7', 'p4', [l(-5), dark, flip], 5)
get_char('c6083') '[convertstrid(1003274)]' (**arg(12, 1003274))
get_char('c6083') '[convertstrid(1003275)]' (**arg(13, 1003275))
get_char('c6083') '[convertstrid(1003276)]' (**arg(14, 1003276))
hide p4
$ update_portrait('oc001_01 10', 'p1', [l(-2), light, flip], 6)
play sfxvoice "avg_vocal_na20.ogg"
get_char('c11') '[convertstrid(1003277)]' (**arg(15, 1003277))
$ update_portrait('oc001_01 10', 'p1', [l(-2), dark, flip], 5)
get_char('c6083') '[convertstrid(1003278)]' (**arg(16, 1003278))
get_char('c6083') '[convertstrid(1003279)]' (**arg(17, 1003279))
hide p1
$ update_portrait('oc003_01 2', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1003280)]' (**arg(18, 1003280))
$ update_portrait('oc003_01 2', 'p3', [l(-6), dark, flip], 5)
get_char('c6093') '[convertstrid(1003281)]' (**arg(19, 1003281))
get_char('c6093') '[convertstrid(1003282)]' (**arg(20, 1003282))
hide p3
$ update_portrait('oc001_01 7', 'p1', [l(-2), light, flip], 6)
play sfxvoice "avg_vocal_na02.ogg"
get_char('c11') '[convertstrid(1003283)]' (**arg(21, 1003283))
$ update_portrait('oc001_01 7', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc003_01 7', 'p3', [r(-6), r_shake, light], 6)
get_char('c33') '[convertstrid(1003284)]' (**arg(22, 1003284))
hide p1
$ update_portrait('oc003_01 7', 'p3', [r(-6), dark], 5)
$ update_portrait('oc002_01 10', 'p2', [l(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch23.ogg"
get_char('c21') '[convertstrid(1003285)]' (**arg(23, 1003285))
$ update_portrait('oc002_01 10', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1003286)]' (**arg(24, 1003286))
hide p3
$ update_portrait('oc002_01 10', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc004_01 10', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1003287)]' (**arg(25, 1003287))
hide p2
hide p4
$ update_narrator('c6101')
$ update_portrait('st029_01 3', 'p610', [l(-28), light, flip], 6)
with fade
$ update_portrait('st029_01 3', 'p610', [l(-28), l_shake, light, flip], 6)
get_char('c6101') '[convertstrid(1003288)]' (**arg(26, 1003288))
$ update_portrait('st029_01 3', 'p610', [l(-28), dark, flip], 5)
$ update_portrait('sc071_01 2', 'p611', [r(-20), light], 6)
get_char('c6113') '[convertstrid(1003289)]' (**arg(27, 1003289))
$ update_portrait('sc071_01 2', 'p611', [r(-20), dark], 5)
$ update_portrait('st029_01 2', 'p610', [l(-28), l_shake, light, flip], 6)
get_char('c6101') '[convertstrid(1003290)]' (**arg(28, 1003290))
hide p610
hide p611
$ update_portrait('oc003_01 4', 'p3', [r(-6), light], 6)
$ update_narrator('c33')
with fade
get_char('c33') '[convertstrid(1003291)]' (**arg(29, 1003291))
$ update_portrait('oc003_01 4', 'p3', [r(-6), dark], 5)
$ update_portrait('oc001_01 4', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1003292)]' (**arg(30, 1003292))
hide p3
$ update_portrait('oc001_01 4', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc004_01 4', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1003293)]' (**arg(31, 1003293))
hide p1
$ update_portrait('oc004_01 4', 'p4', [r(-5), dark], 5)
$ update_portrait('oc002_01 9', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1003294)]' (**arg(32, 1003294))
return "avg20064"