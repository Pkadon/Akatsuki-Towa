label avg20076:

play music "ed7150.ogg"
scene avg_bg_018
$ update_portrait('oc001_01 4', 'p1', [l(-2), light, flip], 6)
$ update_narrator('c11')
window show
with fade_in
c11 '[convertstrid(1003971)]'
play music "ed7111.ogg"
scene avg_bg_012
$ update_narrator('c6591')
with fade
play sfx2 "other_7042.ogg"
c6591 '[convertstrid(1003972)]'
$ update_portrait('oc001_01 2', 'p1', [r_entrance(-2), light], 5)
c13 '[convertstrid(1003973)]'
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
c6591 '[convertstrid(1003974)]'
hide p1
$ update_portrait('oc002_01 14', 'p2', [r(-3), light], 5)
play sfxvoice "avg_vocal_ch06.ogg"
c23 '[convertstrid(1003975)]'
hide p2
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 5)
c13 '[convertstrid(1003976)]'
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
c6591 '[convertstrid(1003977)]'
c6591 '[convertstrid(1003978)]'
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 5)
c13 '[convertstrid(1003979)]'
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
c6591 '[convertstrid(1003980)]'
play sfx2 "other_7022.ogg"
c6591 '[convertstrid(1003981)]'
hide p1
$ update_portrait('oc004_01 4', 'p4', [r(-5), light], 5)
c43 '[convertstrid(1003982)]'
$ update_portrait('oc004_01 4', 'p4', [r(-5), dark], 5)
c6591 '[convertstrid(1003983)]'
hide p4
$ update_portrait('oc003_01 4', 'p3', [r(-6), light], 5)
c33 '[convertstrid(1003984)]'
$ update_portrait('oc003_01 4', 'p3', [r(-6), dark], 5)
c6591 '[convertstrid(1003985)]'
hide p3
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 5)
c13 '[convertstrid(1003986)]'
return