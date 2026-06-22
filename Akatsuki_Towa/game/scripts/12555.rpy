label avg12555:

$ play_music("ED6523.ogg")
scene avg_bg_081
$ update_narrator('c12411')
window show
with fade_in
get_char('c12411') '[convertstrid(1153059)]' (**arg(1, 1153059))
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
play sfxvoice "bcv_oc001_hurt_01.ogg"
get_char('c13') '[convertstrid(1153060)]' (**arg(2, 1153060))
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 17', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1153061)]' (**arg(3, 1153061))
hide p1
$ update_portrait('oc003_01 17', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc002_01 10', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1153062)]' (**arg(4, 1153062))
hide p3
$ update_portrait('oc002_01 10', 'p2', [r(-3), dark], 5)
$ update_portrait('oc004_01 23', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1153063)]' (**arg(5, 1153063))
hide p4
get_char('c12411') '[convertstrid(1153064)]' (**arg(6, 1153064))
$ update_portrait('sc025_01 1', 'p622', [l_entrance(-1), light, flip], 6)
get_char('c6221') '[convertstrid(1153065)]' (**arg(7, 1153065))
hide p2
$ update_portrait('sc025_01 1', 'p622', [l(-1), dark, flip], 5)
$ update_portrait('oc001_01 12', 'p1', [r(-2), r_shake, light], 6)
get_char('c13') '[convertstrid(1153066)]' (**arg(8, 1153066))
hide p622
$ update_portrait('oc001_01 12', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 12', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1153067)]' (**arg(9, 1153067))
hide p2
$ update_portrait('oc003_01 8', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1153068)]' (**arg(10, 1153068))
hide p1
$ update_portrait('oc003_01 8', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc004_01 8', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1153069)]' (**arg(11, 1153069))
hide p3
hide p4
$ update_narrator('c12413')
with fade
get_char('c12413') '[convertstrid(1153070)]' (**arg(12, 1153070))
$ update_portrait('sc025_01 1', 'p622', [l(-1), light, flip], 6)
get_char('c6221') '[convertstrid(1153071)]' (**arg(13, 1153071))
$ update_portrait('sc025_01 1', 'p622', [l(-1), dark, flip], 5)
$ update_portrait('oc001_01 12', 'p1', [r(-2), r_shake, light], 6)
get_char('c13') '[convertstrid(1153072)]' (**arg(14, 1153072))
hide p622
$ update_portrait('oc001_01 12', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 8', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1153073)]' (**arg(15, 1153073))
hide p1
$ update_portrait('oc003_01 8', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc002_01 14', 'p2', [r(-3), r_shake, light], 6)
get_char('c23') '[convertstrid(1153074)]' (**arg(16, 1153074))
hide p2
$ update_portrait('oc001_01 12', 'p1', [r(-2), r_shake, light], 6)
get_char('c13') '[convertstrid(1153075)]' (**arg(17, 1153075))
hide p3
$ update_portrait('oc001_01 12', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 7', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1153076)]' (**arg(18, 1153076))
hide p4
hide p1
$ update_narrator('c12413')
with fade
get_char('c12413') '[convertstrid(1153077)]' (**arg(19, 1153077))
$ update_portrait('sc025_01 1', 'p622', [l(-1), light, flip], 6)
get_char('c6221') '[convertstrid(1153078)]' (**arg(20, 1153078))
$ update_portrait('sc025_01 4', 'p622', [l(-1), light, flip], 6)
get_char('c6221') '[convertstrid(1153079)]' (**arg(21, 1153079))
hide p622
get_char('c12411') '[convertstrid(1153080)]' (**arg(22, 1153080))
return