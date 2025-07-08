label avg25104:
stop music

scene placeholderbackground
show oc002_01 2 as p2 at mid(-3), light, zorder 5
window show
with fade_in
play sfxvoice "avg_vocal_ch12.ogg"
c23 '[textdict[1210294]]'
hide p2
show oc001_01 8 as p1 at mid(-2), light, zorder 5
play sfxvoice "avg_vocal_na06.ogg"
c13 '[textdict[1210295]]'
hide p1
show oc001_01 1 as p1 at mid(-2), light, zorder 5
play sfx2 "common_tag_2.ogg"
c13 '[textdict[1210296]]'
return