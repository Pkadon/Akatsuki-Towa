label avg100125:

stop music
scene placeholderbackground
$ update_portrait('sc001_01 2', 'p9', [mid(-11), light], 5)
window show
with fade_in
c93 '[textdict[1218088]]'
hide p9
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 5)
play sfxvoice "bcv_oc002_win_02.ogg"
c13 '[textdict[1218089]]'
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
$ update_portrait('sc001_01 1', 'p9', [l(-11), light, flip], 6)
c91 '[textdict[1218090]]'
$ update_portrait('sc001_01 5', 'p9', [l(-11), light, flip], 6)
c91 '[textdict[1218091]]'
$ update_portrait('sc001_01 5', 'p9', [l(-11), dark, flip], 6)
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 5)
play sfxvoice "bcv_oc002_win_02.ogg"
c13 '[textdict[1218092]]'
menu:
    extend ""
    "[textdict[1218093]]":
        call avg100126
    "[textdict[1218094]]":
        call avg100127
    "[textdict[1218095]]":
        call avg100128
return