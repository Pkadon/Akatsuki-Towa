label avg20075:

$ play_music("ed7150.ogg")
scene avg_bg_056
$ update_portrait('oc001_01 4', 'p1', [l(-2), light, flip], 6)
$ update_narrator('c11')
window show
with fade_in
c11 '[convertstrid(1003960)]'
hide p1
$ update_narrator('c6561')
with fade
play sfx2 "other_7042.ogg"
c6561 '[convertstrid(1003961)]'
c6483 '[convertstrid(1003962)]'
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1003963)]'
hide p1
$ update_portrait('oc003_01 1', 'p3', [r(-6), light], 6)
play sfxvoice "avg_vocal_ro02.ogg"
c33 '[convertstrid(1003964)]'
$ update_portrait('oc003_01 1', 'p3', [r(-6), dark], 5)
c6501 '[convertstrid(1003965)]'
c6561 '[convertstrid(1003966)]'
c6561 '[convertstrid(1003967)]'
hide p3
c6503 '[convertstrid(1003968)]'
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1003969)]'
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1003970)]'
return