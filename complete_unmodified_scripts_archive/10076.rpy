label avg10076:

$ play_music("ED6103.ogg")
scene avg_bg_023
$ update_narrator('c6893')
window show
with fade_in
play sfx2 "other_7047.ogg"
get_char('c6893') '[convertstrid(1005232)]' (**arg(1, 1005232))
$ update_portrait('oc001_01 10', 'p1', [l_entrance(-2), light, flip], 6)
get_char('c11') '[convertstrid(1005233)]' (**arg(2, 1005233))
$ update_portrait('oc001_01 10', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc002_01 10', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1005234)]' (**arg(3, 1005234))
hide p2
get_char('c6893') '[convertstrid(1005235)]' (**arg(4, 1005235))
get_char('c6893') '[convertstrid(1005236)]' (**arg(5, 1005236))
hide p1
$ update_portrait('sc039_01 1', 'p46', [l(-13), light, flip], 6)
get_char('c461') '[convertstrid(1005237)]' (**arg(6, 1005237))
$ update_portrait('sc039_01 1', 'p46', [l(-13), dark, flip], 5)
get_char('c6893') '[convertstrid(1005238)]' (**arg(7, 1005238))
get_char('c6893') '[convertstrid(1005239)]' (**arg(8, 1005239))
get_char('c6893') '[convertstrid(1005240)]' (**arg(9, 1005240))
get_char('c6893') '[convertstrid(1005241)]' (**arg(10, 1005241))
get_char('c6893') '[convertstrid(1005242)]' (**arg(11, 1005242))
hide p46
$ update_portrait('oc001_01 4', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1005243)]' (**arg(12, 1005243))
$ update_portrait('oc001_01 4', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc002_01 4', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1005244)]' (**arg(13, 1005244))
hide p1
hide p2
play sfx2 "other_7047.ogg"
get_char('c0') '[convertstrid(1005245)]' (**arg(14, 1005245))
get_char('c6991') '[convertstrid(1005246)]' (**arg(15, 1005246))
get_char('c6893') '[convertstrid(1005247)]' (**arg(16, 1005247))
get_char('c6991') '[convertstrid(1005248)]' (**arg(17, 1005248))
$ update_portrait('sc040_01 1', 'p47', [r(-9), light], 6)
get_char('c473') '[convertstrid(1005249)]' (**arg(18, 1005249))
$ update_portrait('sc040_01 1', 'p47', [r(-9), dark], 5)
get_char('c6991') '[convertstrid(1005252)]' (**arg(19, 1005252))
hide p47
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1005253)]' (**arg(20, 1005253))
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
get_char('c6991') '[convertstrid(1005254)]' (**arg(21, 1005254))
get_char('c6991') '[convertstrid(1005255)]' (**arg(22, 1005255))
hide p1
$ update_portrait('oc002_01 4', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1005256)]' (**arg(23, 1005256))
$ update_portrait('oc002_01 10', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1005257)]' (**arg(24, 1005257))
$ update_portrait('oc002_01 10', 'p2', [r(-3), dark], 5)
get_char('c6991') '[convertstrid(1005258)]' (**arg(25, 1005258))
$ update_portrait('oc001_01 1', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1005259)]' (**arg(26, 1005259))
$ update_portrait('oc001_01 1', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc002_01 7', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1005260)]' (**arg(27, 1005260))
$ update_portrait('oc002_01 7', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 4', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1005261)]' (**arg(28, 1005261))
return