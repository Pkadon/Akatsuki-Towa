label avg12637:

play music "ed7203.ogg"
scene avg_bg_070
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
c13 '[convertstrid(1162973)]'
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
c13251 '[convertstrid(1162974)]'
hide p1
$ update_portrait('oc004_01 4', 'p4', [r(-5), light], 6)
c43 '[convertstrid(1162975)]'
$ update_portrait('oc004_01 4', 'p4', [r(-5), dark], 5)
$ update_portrait('oc002_01 4', 'p2', [l(-3), light, flip], 6)
c21 '[convertstrid(1162976)]'
hide p4
$ update_portrait('oc002_01 4', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1162977)]'
hide p2
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
c13251 '[convertstrid(1162978)]'
hide p1
$ update_portrait('oc003_01 1', 'p3', [r(-6), light], 6)
c33 '[convertstrid(1162979)]'
play music "ed7511.ogg"
$ update_portrait('oc003_01 1', 'p3', [r(-6), dark], 5)
play sfx2 "other_7079.ogg"
c13091 '[convertstrid(1162980)]' with shake
hide p3
c13253 '[convertstrid(1162981)]'
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
play sfx2 "fight_6024.ogg"
c13 '[convertstrid(1162982)]'
return