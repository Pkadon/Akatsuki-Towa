label avg20098:

play music "ed7104.ogg"
scene avg_bg_037
$ update_narrator('c11')
window show
with fade_in
$ update_portrait('oc001_01 2', 'p1', [l_entrance(-2), light, flip], 6)
play sfx2 "other_7043.ogg"
c11 '[convertstrid(1004834)]'
$ update_portrait('oc001_01 2', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc002_01 10', 'p2', [r(-3), light], 6)
c23 '[convertstrid(1004835)]'
$ update_portrait('oc002_01 10', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 8', 'p1', [l(-2), light, flip], 6)
play sfxvoice "avg_vocal_na06.ogg"
c11 '[convertstrid(1004836)]'
return