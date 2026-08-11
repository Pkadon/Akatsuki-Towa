label avg20108(trans=fade_in):

$ play_music("ED6105.ogg")
scene avg_bg_036
$ update_portrait('st026_01 5', 'p700', [l(-14), light, flip], 6)
$ update_narrator('c7001')
window show
with trans
get_char('c7001') '[convertstrid(1005324)]' (**arg(1, 1005324))
$ update_portrait('st026_01 5', 'p700', [l(-14), dark, flip], 5)
$ update_portrait('oc002_01 6', 'p2', [r(-3), r_shake, light], 6)
get_char('c23') '[convertstrid(1005325)]' (**arg(2, 1005325))
hide p700
$ update_portrait('oc002_01 6', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 10', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1005326)]' (**arg(3, 1005326))
$ update_portrait('oc001_01 11', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1005327)]' (**arg(4, 1005327))
hide p2
$ update_portrait('oc001_01 11', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('sc039_01 2', 'p46', [r(-13), light], 6)
get_char('c463') '[convertstrid(1005328)]' (**arg(5, 1005328))
$ update_portrait('sc039_01 2', 'p46', [r(-13), dark], 5)
$ update_portrait('oc001_01 2', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1005329)]' (**arg(6, 1005329))
hide p46
$ update_portrait('oc001_01 2', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('sc007_01 2', 'p15', [r(-17), light], 6)
get_char('c153') '[convertstrid(1005330)]' (**arg(7, 1005330))
$ update_portrait('sc007_01 2', 'p15', [r(-17), dark], 5)
$ update_portrait('oc001_01 12', 'p1', [l(-2), l_shake, light, flip], 6)
get_char('c11') '[convertstrid(1005332)]' (**arg(8, 1005332))
$ update_portrait('oc001_01 12', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1005333)]' (**arg(9, 1005333))
hide p15
$ update_portrait('oc001_01 12', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1005334)]' (**arg(10, 1005334))
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 12', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1005335)]' (**arg(11, 1005335))
hide p2
$ update_portrait('oc001_01 12', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('sc039_01 5', 'p46', [r(-13), light], 6)
get_char('c463') '[convertstrid(1005336)]' (**arg(12, 1005336))
hide p1
$ update_portrait('sc039_01 5', 'p46', [r(-13), dark], 5)
$ update_portrait('oc002_01 7', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1005337)]' (**arg(13, 1005337))
$ update_portrait('oc002_01 7', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('sc039_01 4', 'p46', [r(-13), r_shake, light], 6)
get_char('c463') '[convertstrid(1005338)]' (**arg(14, 1005338))
hide p46
$ update_portrait('oc001_01 12', 'p1', [r(-2), r_shake, light], 6)
get_char('c13') '[convertstrid(1005339)]' (**arg(15, 1005339))
$ update_portrait('oc001_01 12', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 7', 'p2', [l(-3), l_shake, light, flip], 6)
get_char('c21') '[convertstrid(1005340)]' (**arg(16, 1005340))
hide p1
$ update_portrait('oc002_01 7', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('st026_01 1', 'p700', [r(-14), light], 6)
get_char('c7003') '[convertstrid(1005341)]' (**arg(17, 1005341))
hide p2
$ update_portrait('st026_01 1', 'p700', [r(-14), dark], 5)
$ update_portrait('oc001_01 10', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1005342)]' (**arg(18, 1005342))
hide p700
$ update_portrait('oc001_01 10', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc002_01 5', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1005343)]' (**arg(19, 1005343))
hide p1
hide p2
get_char('c0') '[convertstrid(1005344)]' (**arg(20, 1005344))
return "avg20108"