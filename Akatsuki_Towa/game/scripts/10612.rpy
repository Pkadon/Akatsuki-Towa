label avg10612:

$ play_music("ED6202.ogg")
scene avg_bg_201
$ update_narrator('c0')
window show
with fade_in
get_char('c0') '[convertstrid(1160570)]' (**arg(1, 1160570))
get_char('c13051') '[convertstrid(1160571)]' (**arg(2, 1160571))
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1160572)]' (**arg(3, 1160572))
hide p1
$ update_portrait('oc003_01 1', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1160573)]' (**arg(4, 1160573))
$ update_portrait('oc003_01 1', 'p3', [r(-6), dark], 5)
get_char('c13051') '[convertstrid(1160574)]' (**arg(5, 1160574))
hide p3
$ update_portrait('oc004_01 1', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1160575)]' (**arg(6, 1160575))
$ update_portrait('oc004_01 11', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1160576)]' (**arg(7, 1160576))
$ update_portrait('oc004_01 11', 'p4', [r(-5), dark], 5)
get_char('c13051') '[convertstrid(1160577)]' (**arg(8, 1160577))
hide p4
$ update_portrait('oc002_01 12', 'p2', [r(-3), r_shake, light], 6)
get_char('c23') '[convertstrid(1160578)]' (**arg(9, 1160578))
hide p2
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1160579)]' (**arg(10, 1160579))
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
get_char('c13051') '[convertstrid(1160580)]' (**arg(11, 1160580))
hide p1
$ update_portrait('oc003_01 13', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1160581)]' (**arg(12, 1160581))
$ update_portrait('oc003_01 13', 'p3', [r(-6), dark], 5)
get_char('c13051') '[convertstrid(1160582)]' (**arg(13, 1160582))
hide p3
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1160583)]' (**arg(14, 1160583))
hide p1
$ update_portrait('oc004_01 22', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1160584)]' (**arg(15, 1160584))
$ update_portrait('oc004_01 22', 'p4', [r(-5), dark], 5)
get_char('c13051') '[convertstrid(1160585)]' (**arg(16, 1160585))
get_char('c13051') '[convertstrid(1160586)]' (**arg(17, 1160586))
get_char('c13051') '[convertstrid(1160587)]' (**arg(18, 1160587))
hide p4
$ update_portrait('oc002_01 14', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1160588)]' (**arg(19, 1160588))
$ update_portrait('oc002_01 14', 'p2', [r(-3), dark], 5)
$ update_portrait('oc003_01 17', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1160589)]' (**arg(20, 1160589))
hide p3
get_char('c13051') '[convertstrid(1160590)]' (**arg(21, 1160590))
get_char('c13051') '[convertstrid(1160591)]' (**arg(22, 1160591))
hide p2
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1160592)]' (**arg(23, 1160592))
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 1', 'p4', [l(-5), light, flip], 6)
play sfxvoice "avg_vocal_li02.ogg"
get_char('c41') '[convertstrid(1160593)]' (**arg(24, 1160593))
$ update_portrait('oc004_01 1', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1160594)]' (**arg(25, 1160594))
hide p1
$ update_portrait('oc004_01 1', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc003_01 2', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1160595)]' (**arg(26, 1160595))
hide p4
$ update_portrait('oc003_01 2', 'p3', [r(-6), dark], 5)
get_char('c13051') '[convertstrid(1160596)]' (**arg(27, 1160596))
$ update_portrait('oc003_01 1', 'p3', [r(-6), light], 6)
play sfxvoice "avg_vocal_ro02.ogg"
get_char('c33') '[convertstrid(1160597)]' (**arg(28, 1160597))
$ update_portrait('oc003_01 1', 'p3', [r(-6), dark], 5)
get_char('c13051') '[convertstrid(1160598)]' (**arg(29, 1160598))
hide p3
$ update_portrait('oc002_01 22', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1160599)]' (**arg(30, 1160599))
$ update_portrait('oc002_01 22', 'p2', [r(-3), dark], 5)
get_char('c13051') '[convertstrid(1160600)]' (**arg(31, 1160600))
$ update_portrait('oc002_01 5', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1160601)]' (**arg(32, 1160601))
hide p2
$ update_portrait('oc001_01 22', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1160602)]' (**arg(33, 1160602))
return