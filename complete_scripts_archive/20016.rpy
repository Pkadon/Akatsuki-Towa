label avg20016:
stop music

play music "ED6518.ogg"
scene placeholderbackground
with fade
play sfx2 "common_cancel.ogg"
play sfxvoice "avg_vocal_ch08.ogg"
show oc002_01 8 as c2portrait at centerpos(-3), zorder 5
c23 '[textdict[1000950]]'
play sfxvoice "avg_vocal_na06.ogg"
hide c2portrait
show oc001_01 8 as c1portrait at centerpos(-2), zorder 5
c13 '[textdict[1000951]]'
return