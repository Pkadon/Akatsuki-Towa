label avg20099:

play music "ed7104.ogg"
scene avg_bg_037
$ update_narrator('c6831')
window show
with fade_in
play sfx2 "other_7064.ogg"
c6831 '[convertstrid(1004837)]'
c6843 '[convertstrid(1004838)]'
c6831 '[convertstrid(1004839)]'
c6843 '[convertstrid(1004840)]'
c6831 '[convertstrid(1004841)]'
c6831 '[convertstrid(1004842)]'
c6853 '[convertstrid(1004843)]'
c6861 '[convertstrid(1004844)]'
c6853 '[convertstrid(1004845)]'
c6861 '[convertstrid(1004846)]'
c6853 '[convertstrid(1004847)]'
$ update_portrait('oc001_01 1', 'p1', [l_entrance(-2), light, flip], 6)
play sfxvoice "avg_vocal_na15.ogg"
c11 '[convertstrid(1004848)]'
$ update_portrait('oc001_01 1', 'p1', [l(-2), dark, flip], 6)
$ update_portrait('sc039_01 1', 'p46', [r(-13), light], 5)
c463 '[convertstrid(1004849)]'
return