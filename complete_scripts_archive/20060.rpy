label avg20060:

$ play_music("ed7151.ogg")
scene avg_bg_027
$ update_narrator('c4971')
window show
with fade_in
play sfx2 "other_7071.ogg"
c4971 '[convertstrid(1002996)]'
c4971 '[convertstrid(1002997)]'
$ update_portrait('oc001_01 9', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1002998)]'
$ update_portrait('oc001_01 9', 'p1', [r(-2), dark], 5)
c4971 '[convertstrid(1002999)]'
$ update_portrait('oc001_01 18', 'p1', [r(-2), light], 6)
play sfx2 "other_7073.ogg"
c13 '[convertstrid(1003000)]'
$ update_portrait('oc001_01 3', 'p1', [r(-2), r_shake, light], 6)
c13 '[convertstrid(1003001)]'
return