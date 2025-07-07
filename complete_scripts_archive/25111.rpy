label avg25111:
stop music

scene placeholderbackground
show oc002_01 3 as p2 at mid(-3), light, zorder 5
with fade
play sfx2 "elc_5002.ogg"
play sfxvoice "bcv_oc002_hurt_01.ogg"
c23 '[textdict[1210329]]'
hide p2
show oc001_01 2 as p1 at mid(-2), light, zorder 5
c13 '[textdict[1210330]]'
hide p1
show oc002_01 7 as p2 at mid(-3), light, zorder 5
play sfxvoice "avg_vocal_ch31.ogg"
c23 '[textdict[1210331]]'
return