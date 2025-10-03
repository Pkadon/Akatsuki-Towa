label avg20051:

$ play_music("ed7151.ogg")
scene avg_bg_027
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
c13 '[convertstrid(1002787)]'
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1002788)]'
hide p1
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
with fade
play sfx2 "other_7085.ogg"
c13 '[convertstrid(1002789)]'
$ play_music("ed7511.ogg")
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 9', 'p2', [l(-3), r_shake, light, flip], 6)
c21 '[convertstrid(1002790)]'
$ update_portrait('oc002_01 9', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r_midback(-2), light], 6)
play sfx2 "other_7007.ogg"
play sfxvoice "avg_vocal_na20.ogg"
c13 '[convertstrid(1002791)]'
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 7', 'p2', [l(-3), r_shake, light, flip], 6)
c21 '[convertstrid(1002792)]'
$ update_portrait('oc002_01 7', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 9', 'p1', [r(-2), l_shake, light], 6)
c13 '[convertstrid(1002793)]'
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1002794)]'
hide p2
hide p1
play sfx2 "other_7085.ogg"
c0 '[convertstrid(1002795)]'
c0 '[convertstrid(1002796)]'
$ play_music("ed7151.ogg")
$ update_portrait('oc004_01 1', 'p4', [l_entrance(-5), light, flip], 6)
c41 '[convertstrid(1002797)]'
$ update_portrait('oc004_01 1', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1002798)]'
hide p4
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 5', 'p2', [l(-3), light, flip], 6)
c21 '[convertstrid(1002799)]'
$ update_portrait('oc002_01 5', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1002800)]'
return