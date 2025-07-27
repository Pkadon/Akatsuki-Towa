label avg12232:

play music "ed7105.ogg"
scene avg_bg_023
$ update_portrait('oc001_01 18', 'p1', [r(-2), light], 5)
$ update_narrator('c13')
window show
with fade_in
play sfx2 "common_cancel.ogg"
c13 '[convertstrid(1121117)]'
$ update_portrait('oc001_01 18', 'p1', [r(-2), dark], 5)
c6891 '[convertstrid(1121118)]'
return