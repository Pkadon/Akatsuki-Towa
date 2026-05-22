label avg12525:

$ play_music("ED6100.ogg")
scene avg_bg_023
$ update_narrator('c0')
window show
with fade_in
c0 '[convertstrid(1151441)]'
c12021 '[convertstrid(1151442)]'
$ update_portrait('sc005_01 1', 'p13', [l(-17), light, flip], 6)
c131 '[convertstrid(1151443)]'
$ update_portrait('sc005_01 1', 'p13', [l(-17), dark, flip], 5)
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
c23 '[convertstrid(1151444)]'
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
$ update_portrait('sc005_01 4', 'p13', [l(-17), light, flip], 6)
c131 '[convertstrid(1151445)]'
hide p2
$ update_portrait('sc005_01 4', 'p13', [l(-17), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1151446)]'
hide p13
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 17', 'p3', [l(-6), light, flip], 6)
c31 '[convertstrid(1151447)]'
hide p1
$ update_portrait('oc003_01 17', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc004_01 23', 'p4', [r(-5), light], 6)
c43 '[convertstrid(1151448)]'
hide p3
$ update_portrait('oc004_01 23', 'p4', [r(-5), dark], 5)
$ update_portrait('st040_01 1', 'p239', [l_entrance(-19), light, flip], 6)
c2391 '[convertstrid(1151449)]'
hide p4
$ update_portrait('st040_01 1', 'p239', [l(-19), dark, flip], 5)
$ update_portrait('oc002_01 8', 'p2', [r(-3), light], 6)
c23 '[convertstrid(1151450)]'
hide p239
hide p2
$ update_portrait('sc005_01 1', 'p13', [r(-17), light], 6)
$ update_narrator('c133')
with fade
c133 '[convertstrid(1151451)]'
$ update_portrait('sc005_01 1', 'p13', [r(-17), dark], 5)
c12021 '[convertstrid(1151452)]'
$ update_portrait('sc005_01 1', 'p13', [r(-17), light], 6)
c133 '[convertstrid(1151453)]'
$ update_portrait('sc005_01 1', 'p13', [r(-17), dark], 5)
c12021 '[convertstrid(1151454)]'
c12021 '[convertstrid(1151455)]'
c12021 '[convertstrid(1151456)]'
$ update_portrait('sc005_01 2', 'p13', [r(-17), r_shake, light], 6)
c133 '[convertstrid(1151457)]'
$ update_portrait('sc005_01 2', 'p13', [r(-17), dark], 5)
c12021 '[convertstrid(1151458)]'
c12021 '[convertstrid(1151459)]'
return