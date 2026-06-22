label avg12552:

$ play_music("ED6304.ogg")
scene avg_bg_081
$ update_portrait('oc003_01 17', 'p3', [l(-6), light, flip], 6)
$ update_narrator('c31')
window show
with fade_in
play sfxvoice "avg_vocal_ro14.ogg"
get_char('c31') '[convertstrid(1153011)]' (**arg(1, 1153011))
$ update_portrait('oc003_01 17', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc004_01 10', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1153012)]' (**arg(2, 1153012))
$ update_portrait('oc004_01 4', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1153013)]' (**arg(3, 1153013))
hide p4
$ update_portrait('oc002_01 8', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1153014)]' (**arg(4, 1153014))
hide p2
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1153015)]' (**arg(5, 1153015))
hide p3
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('sc025_01 5', 'p622', [l_entrance(-1), light, flip], 6)
get_char('c6221') '[convertstrid(1153016)]' (**arg(6, 1153016))
$ update_portrait('sc025_01 5', 'p622', [l(-1), dark, flip], 5)
$ update_portrait('oc001_01 12', 'p1', [r(-2), r_shake, light], 6)
get_char('c13') '[convertstrid(1153017)]' (**arg(7, 1153017))
$ update_portrait('oc001_01 12', 'p1', [r(-2), dark], 5)
$ update_portrait('sc025_01 5', 'p622', [l(-1), light, flip], 6)
get_char('c6221') '[convertstrid(1153018)]' (**arg(8, 1153018))
$ update_portrait('sc025_01 1', 'p622', [l(-1), light, flip], 6)
get_char('c6221') '[convertstrid(1153019)]' (**arg(9, 1153019))
hide p1
$ update_portrait('sc025_01 1', 'p622', [l(-1), dark, flip], 5)
$ update_portrait('oc002_01 5', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1153020)]' (**arg(10, 1153020))
hide p2
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1153021)]' (**arg(11, 1153021))
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('sc025_01 5', 'p622', [l(-1), light, flip], 6)
get_char('c6221') '[convertstrid(1153022)]' (**arg(12, 1153022))
$ update_portrait('sc025_01 5', 'p622', [l(-1), light, flip], 6)
get_char('c6221') '[convertstrid(1153023)]' (**arg(13, 1153023))
hide p1
$ update_portrait('sc025_01 5', 'p622', [l(-1), dark, flip], 5)
get_char('c12413') '[convertstrid(1153024)]' (**arg(14, 1153024))
$ update_portrait('sc025_01 4', 'p622', [l(-1), light, flip], 6)
get_char('c6221') '[convertstrid(1153025)]' (**arg(15, 1153025))
$ update_portrait('sc025_01 4', 'p622', [l(-1), dark, flip], 5)
get_char('c12413') '[convertstrid(1153026)]' (**arg(16, 1153026))
hide p622
$ update_narrator('c12411')
with fade
get_char('c12411') '[convertstrid(1153027)]' (**arg(17, 1153027))
$ update_portrait('oc002_01 14', 'p2', [r(-3), r_shake, light], 6)
get_char('c23') '[convertstrid(1153028)]' (**arg(18, 1153028))
hide p2
$ update_portrait('oc001_01 8', 'p1', [r_entrance(-2), light], 6)
play sfxvoice "avg_vocal_na04_b.ogg"
get_char('c13') '[convertstrid(1153029)]' (**arg(19, 1153029))
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
get_char('c12411') '[convertstrid(1153030)]' (**arg(20, 1153030))
get_char('c12411') '[convertstrid(1153031)]' (**arg(21, 1153031))
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1153032)]' (**arg(22, 1153032))
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 17', 'p3', [l_entrance(-6), light, flip], 6)
get_char('c31') '[convertstrid(1153033)]' (**arg(23, 1153033))
hide p1
$ update_portrait('oc003_01 17', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc004_01 4', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1153034)]' (**arg(24, 1153034))
return