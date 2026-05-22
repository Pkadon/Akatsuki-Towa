label avg12665:

$ play_music("ed7150.ogg")
scene avg_bg_013
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
play sfx2 "other_7064.ogg"
c13 '[convertstrid(1166601)]'
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1166602)]'
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 4', 'p2', [l(-3), light, flip], 6)
c21 '[convertstrid(1166603)]'
hide p2
c13671 '[convertstrid(1166604)]'
$ update_portrait('oc004_01 4', 'p4', [l(-5), light, flip], 6)
c41 '[convertstrid(1166605)]'
$ update_portrait('oc004_01 4', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1166606)]'
hide p4
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
play sfx2 "other_7085.ogg"
c5001 '[convertstrid(1166607)]' with shake
$ update_portrait('oc001_01 9', 'p1', [r(-2), r_shake, light], 6)
c13 '[convertstrid(1166608)]'
$ update_portrait('oc001_01 9', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 12', 'p2', [l(-3), light, flip], 6)
c21 '[convertstrid(1166609)]'
hide p2
hide p1
c0 '[convertstrid(1166610)]'
play sfx2 "other_7085.ogg"
c13681 '[convertstrid(1166611)]' with shake
c0 '[convertstrid(1166612)]'
$ update_portrait('oc004_01 16', 'p4', [l(-5), l_shake, light, flip], 6)
c41 '[convertstrid(1166613)]'
$ update_portrait('oc004_01 16', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc001_01 23', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1166614)]'
$ update_portrait('oc001_01 23', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 8', 'p4', [l(-5), light, flip], 6)
c41 '[convertstrid(1166615)]'
return