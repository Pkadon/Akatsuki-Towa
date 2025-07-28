label avg20070:

play music "ed7150.ogg"
scene avg_bg_018
$ update_narrator('c13')
window show
with fade_in
$ update_portrait('oc001_01 2', 'p1', [r_entrance(-2), light], 6)
play sfx2 "other_7064.ogg"
c13 '[convertstrid(1003886)]'
hide p1
c6483 '[convertstrid(1003887)]'
c6491 '[convertstrid(1003888)]'
c6503 '[convertstrid(1003889)]'
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na02.ogg"
c13 '[convertstrid(1003890)]'
$ update_portrait('oc001_01 7', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 8', 'p4', [l(-5), light, flip], 6)
play sfxvoice "avg_vocal_li17.ogg"
c41 '[convertstrid(1003891)]'
hide p4
hide p1
$ update_narrator('c0')
with fade
play sfx2 "other_7021.ogg"
c0 '[convertstrid(1003892)]'
play sfx2 "other_7004.ogg"
c6491 '[convertstrid(1003893)]'
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1003894)]'
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
c6491 '[convertstrid(1003895)]'
c6491 '[convertstrid(1003896)]'
c6491 '[convertstrid(1003897)]'
hide p1
$ update_portrait('oc002_01 17', 'p2', [r(-3), light], 6)
c23 '[convertstrid(1003898)]'
$ update_portrait('oc002_01 17', 'p2', [r(-3), dark], 5)
play sfx2 "other_7021.ogg"
c6511 '[convertstrid(1003899)]'
c6511 '[convertstrid(1003900)]'
c6511 '[convertstrid(1003901)]'
c6491 '[convertstrid(1003902)]'
hide p2
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1003903)]'
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1003904)]'
return