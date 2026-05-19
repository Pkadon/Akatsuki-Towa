label avg24014:

$ play_music("ed7105.ogg")
scene avg_bg_064
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
c13 '[convertstrid(1200061)]'
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
c7421 '[convertstrid(1200062)]'
$ update_portrait('oc001_01 5', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1200063)]'
return