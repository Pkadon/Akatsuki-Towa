label avg25137:
stop music

scene placeholderbackground
with fade
play sfxvoice "bcv_oc001_com_01.ogg"
show oc001_01 2 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[1210422]]'
play sfx2 "fight_6025.ogg"
hide c1portrait
show oc002_01 12 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[1210423]]'
play sfx2 "common_tag_2.ogg"
hide c2portrait
show oc001_01 4 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[1210424]]'
return