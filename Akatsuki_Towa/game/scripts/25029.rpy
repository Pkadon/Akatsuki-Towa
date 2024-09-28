label avg25029:
stop music

scene placeholderbackground
with fade
play sfx2 "common_select.ogg"
play sfxvoice "avg_vocal_ch04.ogg"
show oc002_01 4 as c2portrait at centerpos(-3), zorder 5
c23 '[textdict[1210071]]'
play sfxvoice "avg_vocal_na02.ogg"
hide c2portrait
show oc001_01 7 as c1portrait at centerpos(-2), zorder 5
c13 '[textdict[1210072]]'
hide c1portrait
show uc001_01 1 as c2000portrait at centerpos(-2), zorder 5
c20003 '[textdict[1210073]]'
return