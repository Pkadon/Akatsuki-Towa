label avg20104:

play music "ED6103.ogg"
scene avg_bg_037
$ update_narrator('c6941')
window show
with fade_in
c6941 '[convertstrid(1005074)]'
c6953 '[convertstrid(1005075)]'
c6941 '[convertstrid(1005076)]'
c6953 '[convertstrid(1005077)]'
c6953 '[convertstrid(1005078)]'
c6941 '[convertstrid(1005079)]'
c6953 '[convertstrid(1005080)]'
c6941 '[convertstrid(1005081)]'
c6941 '[convertstrid(1005082)]'
$ update_portrait('oc002_01 4', 'p2', [l_entrance(-3), light, flip], 6)
c21 '[convertstrid(1005083)]'
$ update_portrait('oc002_01 4', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1005084)]'
hide p2
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
c6951 '[convertstrid(1005085)]'
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1005086)]'
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
c6941 '[convertstrid(1005087)]'
c6951 '[convertstrid(1005091)]'
hide p1
$ update_portrait('sc040_01 2', 'p47', [r(-9), light], 6)
c473 '[convertstrid(1005092)]'
$ update_portrait('sc040_01 2', 'p47', [r(-9), dark], 5)
c6951 '[convertstrid(1005093)]'
$ update_portrait('sc040_01 1', 'p47', [r(-9), light], 6)
c473 '[convertstrid(1005094)]'
$ update_portrait('sc040_01 1', 'p47', [r(-9), dark], 5)
c6951 '[convertstrid(1005095)]'
c6941 '[convertstrid(1005096)]'
hide p47
$ update_portrait('oc001_01 12', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na21.ogg"
c13 '[convertstrid(1005097)]'
$ update_portrait('oc001_01 12', 'p1', [r(-2), dark], 5)
c6951 '[convertstrid(1005098)]'
c6941 '[convertstrid(1005099)]'
hide p1
$ update_portrait('oc002_01 6', 'p2', [r(-3), light], 6)
c23 '[convertstrid(1005100)]'
$ update_portrait('oc002_01 6', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 7', 'p1', [l(-2), light, flip], 6)
c11 '[convertstrid(1005101)]'
return