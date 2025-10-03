label avg10524:

$ play_music("ED6100.ogg")
scene avg_bg_078
$ update_narrator('c0')
window show
with fade_in
c0 '[convertstrid(1152103)]'
c0 '[convertstrid(1152104)]'
c0 '[convertstrid(1152105)]'
c12301 '[convertstrid(1152106)]'
c12293 '[convertstrid(1152107)]' (what_size=(gui.text_size*1.2)) with shake
c12301 '[convertstrid(1152108)]'
$ update_portrait('oc004_01 4', 'p4', [r_entrance(-5), light], 6)
c43 '[convertstrid(1152109)]'
$ update_portrait('oc004_01 4', 'p4', [r(-5), light], 6)
c43 '[convertstrid(1152110)]'
$ update_portrait('oc004_01 4', 'p4', [r(-5), dark], 5)
c12291 '[convertstrid(1152111)]'
$ update_portrait('oc004_01 4', 'p4', [r(-5), light], 6)
c43 '[convertstrid(1152112)]'
$ update_portrait('oc004_01 4', 'p4', [r(-5), dark], 5)
c12301 '[convertstrid(1152113)]'
$ update_portrait('oc004_01 11', 'p4', [r(-5), light], 6)
c43 '[convertstrid(1152114)]'
$ update_portrait('oc004_01 11', 'p4', [r(-5), dark], 5)
c12311 '[convertstrid(1152115)]'
hide p4
c12293 '[convertstrid(1152116)]'
c12311 '[convertstrid(1152117)]'
c12293 '[convertstrid(1152118)]'
c12301 '[convertstrid(1152119)]'
$ update_portrait('oc004_01 4', 'p4', [r(-5), light], 6)
c43 '[convertstrid(1152120)]'
$ update_portrait('oc004_01 4', 'p4', [r(-5), dark], 5)
c12301 '[convertstrid(1152121)]'
$ update_portrait('oc002_01 6', 'p2', [l(-3), l_shake, light, flip], 6)
c21 '[convertstrid(1152122)]'
hide p4
$ update_portrait('oc002_01 6', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1152123)]'
return