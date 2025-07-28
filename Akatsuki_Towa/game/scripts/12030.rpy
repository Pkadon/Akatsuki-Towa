label avg12030:

play music "ed7150.ogg"
scene avg_bg_015
$ update_narrator('c9721')
window show
with fade_in
play sfx2 "other_7047.ogg"
c9721 '[convertstrid(1120128)]'
$ update_portrait('oc002_01 1', 'p2', [r(-3), light], 6)
c23 '[convertstrid(1120129)]'
hide p2
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1120130)]'
hide p1
c0 '[convertstrid(1120131)]'
c9721 '[convertstrid(1120132)]'
c9721 '[convertstrid(1120133)]'
$ update_portrait('oc002_01 5', 'p2', [r(-3), r_shake, light], 6)
play sfxvoice "avg_vocal_ch06.ogg"
c23 '[convertstrid(1120134)]'
$ update_portrait('oc002_01 5', 'p2', [r(-3), dark], 5)
c9721 '[convertstrid(1120136)]'
$ update_portrait('oc001_01 4', 'p1', [l(-2), light, flip], 6)
c11 '[convertstrid(1120137)]'
$ update_portrait('oc001_01 4', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc002_01 18', 'p2', [r(-3), light], 6)
c23 '[convertstrid(1120138)]'
$ update_portrait('oc002_01 18', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 7', 'p1', [l(-2), light, flip], 6)
c11 '[convertstrid(1120139)]'
$ update_portrait('oc001_01 7', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc002_01 5', 'p2', [r(-3), light], 6)
c23 '[convertstrid(1120140)]'
return