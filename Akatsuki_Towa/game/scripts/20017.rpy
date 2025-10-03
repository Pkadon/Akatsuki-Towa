label avg20017:

$ play_music("ED6101.ogg")
scene avg_bg_064
$ update_narrator('c13')
window show
with fade_in
$ update_portrait('oc001_01 11', 'p1', [r_entrance(-2), light], 6)
play sfx2 "other_7017.ogg"
c13 '[convertstrid(1001028)]'
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
play sfx2 "other_7064.ogg"
c13 '[convertstrid(1001029)]'
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1001030)]'
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 1', 'p2', [l(-3), light, flip], 6)
c21 '[convertstrid(1001031)]'
return