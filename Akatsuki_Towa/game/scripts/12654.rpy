label avg12654:

$ play_music("ED6105.ogg")
scene avg_bg_023
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
c13 '[convertstrid(1166344)]'
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
c13351 '[convertstrid(1166345)]'
hide p1
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
c23 '[convertstrid(1166346)]'
$ update_portrait('oc002_01 9', 'p2', [r(-3), r_shake, light], 6)
play sfx2 "other_7087.ogg"
c23 '[convertstrid(1166347)]'
$ update_portrait('oc002_01 9', 'p2', [r(-3), dark], 5)
$ update_portrait('oc003_01 17', 'p3', [l(-6), light, flip], 6)
c31 '[convertstrid(1166348)]'
hide p2
$ update_portrait('oc003_01 17', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc004_01 17', 'p4', [r(-5), light], 6)
c43 '[convertstrid(1166349)]'
hide p3
$ update_portrait('oc004_01 17', 'p4', [r(-5), dark], 5)
c13351 '[convertstrid(1166350)]'
c13351 '[convertstrid(1166351)]'
c13351 '[convertstrid(1166352)]'
$ update_portrait('oc003_01 2', 'p3', [l(-6), light, flip], 6)
c31 '[convertstrid(1166353)]'
$ update_portrait('oc003_01 2', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc004_01 10', 'p4', [r(-5), light], 6)
c43 '[convertstrid(1166354)]'
$ update_portrait('oc004_01 1', 'p4', [r(-5), light], 6)
c43 '[convertstrid(1166355)]'
$ update_portrait('oc004_01 1', 'p4', [r(-5), dark], 5)
$ update_portrait('oc003_01 8', 'p3', [l(-6), light, flip], 6)
c31 '[convertstrid(1166356)]'
hide p3
c13351 '[convertstrid(1166357)]'
hide p4
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1166358)]'
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
c13351 '[convertstrid(1166359)]'
c13351 '[convertstrid(1166360)]'
c13351 '[convertstrid(1166361)]'
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
c31 '[convertstrid(1166362)]'
hide p1
$ update_portrait('oc003_01 4', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc002_01 9', 'p2', [r(-3), light], 6)
c23 '[convertstrid(1166363)]'
return