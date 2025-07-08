label avg12232:
stop music

play music "ed7105.ogg"
scene avg_bg_023
$ update_portrait('oc001_01 18', 'p1', [r(-2), light], 5)
window show
with fade_in
play sfx2 "common_cancel.ogg"
c13 '[textdict[1121117]]'
hide p1
$ update_portrait('oc001_01 18', 'p1', [r(-2), dark], 5)
c6891 '[textdict[1121118]]'
return