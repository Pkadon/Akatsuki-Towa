label avg25137:
stop music

scene placeholderbackground
with fade
play sfxvoice "bcv_oc001_com_01.ogg"
show oc001_01 2 as p1 at mid(-2), light, zorder 5
c13 '[textdict[1210422]]'
play sfx2 "fight_6025.ogg"
hide p1
show oc002_01 12 as p2 at mid(-3), light, zorder 5
c23 '[textdict[1210423]]'
play sfx2 "common_tag_2.ogg"
hide p2
show oc001_01 4 as p1 at mid(-2), light, zorder 5
c13 '[textdict[1210424]]'
return