label avg10538:

$ play_music("ED6301.ogg")
scene avg_bg_102
$ update_portrait('oc003_01 17', 'p3', [l(-6), light, flip], 6)
$ update_narrator('c31')
window show
with fade_in
c31 '[convertstrid(1152579)]'
$ update_portrait('oc003_01 17', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1152580)]'
hide p3
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
c12341 '[convertstrid(1152581)]'
hide p1
$ update_portrait('sc021_01 1', 'p29', [r(-17), light], 6)
c293 '[convertstrid(1152582)]'
hide p29
$ update_portrait('oc002_01 14', 'p2', [r(-3), r_shake, light], 6)
c23 '[convertstrid(1152583)]'
$ update_portrait('oc002_01 14', 'p2', [r(-3), dark], 5)
$ update_portrait('oc004_01 4', 'p4', [l(-5), light, flip], 6)
c41 '[convertstrid(1152584)]'
hide p4
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
c31 '[convertstrid(1152585)]'
return