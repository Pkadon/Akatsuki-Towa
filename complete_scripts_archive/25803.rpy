label avg25803:
stop music

scene placeholderbackground
window show
with fade_in
play sfx2 "common_tag_2.ogg"
c0 '[textdict[1211254]]'
show oc002_01 12 as p2 at mid(-3), light, zorder 5
play sfxvoice "avg_vocal_ch11.ogg"
c23 '[textdict[1211255]]'
hide p2
show oc001_01 18 as p1 at mid(-2), light, zorder 5
c13 '[textdict[1211256]]'
hide p1
show oc002_01 7 as p2 at mid(-3), light, zorder 5
play sfxvoice "avg_vocal_ch31.ogg"
c23 '[textdict[1211257]]'
hide p2
show oc001_01 8 as p1 at mid(-2), light, zorder 5
play sfxvoice "avg_vocal_na05.ogg"
c13 '[textdict[1211258]]'
return