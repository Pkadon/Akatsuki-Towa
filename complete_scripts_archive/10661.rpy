label avg10661:

play music "ed9999.ogg"
scene avg_bg_070
$ update_narrator('c0')
window show
with fade_in
play sfx2 "other_7018.ogg"
c0 '[convertstrid(1165584)]'
scene avg_bg_001
$ update_portrait('sc008_01 4', 'p16', [l(-18), light, flip], 6)
$ update_narrator('c161')
with fade
c161 '[convertstrid(1165585)]'
$ update_portrait('sc008_01 4', 'p16', [l(-18), light, flip], 6)
c161 '[convertstrid(1165586)]'
$ update_portrait('sc008_01 4', 'p16', [l(-18), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1165587)]'
hide p16
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 4', 'p2', [l(-3), light, flip], 6)
c21 '[convertstrid(1165588)]'
hide p2
hide p1
c0 '[convertstrid(1165589)]'
$ update_portrait('oc004_01 4', 'p4', [r(-5), light], 6)
c43 '[convertstrid(1165590)]'
$ update_portrait('oc004_01 4', 'p4', [r(-5), dark], 5)
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
c31 '[convertstrid(1165591)]'
hide p4
$ update_portrait('oc003_01 4', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1165592)]'
hide p1
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
c23 '[convertstrid(1165593)]'
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
c31 '[convertstrid(1165594)]'
hide p2
$ update_portrait('oc003_01 4', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('st061_01 1', 'p1304', [r(-2), light], 6)
c13043 '[convertstrid(1165595)]'
return