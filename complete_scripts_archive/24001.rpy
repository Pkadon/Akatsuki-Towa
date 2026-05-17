label avg24001:

$ play_music("ED6104.ogg")
scene avg_bg_011
$ update_narrator('c9641')
window show
with fade_in
c9641 '[convertstrid(1200000)]'
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1200001)]'
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
c9641 '[convertstrid(1200002)]'
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1200003)]'
return