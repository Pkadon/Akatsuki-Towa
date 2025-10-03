label avg20011:

$ play_music("ed7150.ogg")
scene avg_bg_023
$ update_narrator('c0')
window show
with fade_in
c0 '[convertstrid(1000499)]'
c0 '[convertstrid(1000500)]'
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1000501)]'
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1000502)]'
return