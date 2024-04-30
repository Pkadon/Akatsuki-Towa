label avg25113:
scene placeholderbackground
nobody "(Scene 1)"
stop music

scene placeholderbackground
with fade
play sfx2 "common_tag_2.ogg"
c00 '[textdict[str(1210338)]]'
play sfxvoice "bcv_oc002_hurt_02.ogg"
show oc002_01 12 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[str(1210339)]]'
hide c2portrait
show oc001_01 4 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[str(1210340)]]'
scene placeholderbackground
with fade
stop music
nobody "(Scene 2)"
stop music

scene placeholderbackground
with fade
c00 '[textdict[str(1210341)]]'
menu:
    "[textdict[str(1210240)]]":
        call avg25116
    "[textdict[str(1210241)]]":
        call avg25115
return